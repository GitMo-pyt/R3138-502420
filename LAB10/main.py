import json, time
import pyttsx3, pyaudio, vosk
import requests


class Speech:
    def __init__(self):
        self.speaker = 0
        self.tts = pyttsx3.init('sapi5')

    def set_voice(self, speaker):
        self.voices = self.tts.getProperty('voices')
        for count, voice in enumerate(self.voices):
            if count == 0:
                print('0')
                id = voice.id
            if speaker == count:
                id = voice.id
        return id

    def text2voice(self, speaker=0, text='Готов'):
        self.tts.setProperty('voice', self.set_voice(speaker))
        self.tts.say(text)
        self.tts.runAndWait()


class Recognize:
    def __init__(self):
        model = vosk.Model('vosk-model-small-ru-0.22')
        self.record = vosk.KaldiRecognizer(model, 16000)
        self.stream()

    def stream(self):
        pa = pyaudio.PyAudio()
        self.stream = pa.open(format=pyaudio.paInt16,
                         channels=1,
                         rate=16000,
                         input=True,
                         frames_per_buffer=8000)


    def listen(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.record.AcceptWaveform(data) and len(data) > 0:
                answer = json.loads(self.record.Result())
                if answer['text']:
                    yield answer['text']


def speak(text):
    speech = Speech()
    speech.text2voice(speaker=1, text=text)


def commands(command):
    global weather
    if command == 'погода':
        s1 = f'Temerature is {(int(weather[1][2:-2]) - 32) * 5 / 9}000'
        s2 = f',, and wind is {weather[2][3:-3]} meters per second'
        return s1[ :s1.index('.') + 2] + s2
    if command == 'ветер':
        return f'{weather[2][-3]} meters per second'
    if command == 'направление':
        return weather[2]
    if command == 'прогулка':
        if (int(weather[1][2:-2]) - 32) * 5 / 9 > 5 and int(weather[3][-3]) < 15:
            return 'yes'
        else:
            return 'no'
    if command == 'записать':
        file = open('weather.txt', 'w', encoding='UTF-8')
        file.write(f'Облачность: {weather[0]}\nТемпература: {weather[1]}\nВетер: {weather[2]}\nПрогулка: {commands("прогулка")}')
        return 'Done'
    if command == 'закрыть':
        exit()
    return 'Repeat please'



string_weather = requests.get('https://wttr.in/Saint-Petersburg?format=2').text
weather = string_weather.split()
rec = Recognize()
text_gen = rec.listen()
rec.stream.stop_stream()
speak('Starting')
time.sleep(0.5)
rec.stream.start_stream()
for text in text_gen:
    speak(commands(text))