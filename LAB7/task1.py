from requests import *
print('---Задание 1---')
lat = 60.09
lon = 29.96
weather = get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=814f5a1ac26fdac37a5875bbf2bdf697').json()
print('Погода в Сестрорецке:')
print(f"{weather['weather'][0]['description']}\nВлажность: {weather['main']['humidity']}\nДавление: {weather['main']['pressure']}\n")

print('---Задание 2---')
position = get('http://api.open-notify.org/iss-now.json').json()
people = get('http://api.open-notify.org/astros.json').json()
print(f"Координаты МКС: {position['iss_position']['latitude']} {position['iss_position']['longitude']}")
print(f"Количество людей в космосе сейчас: {len(people['people'])}\nСписок:")
counter = 0
for i in people['people']:
    counter += 1
    print(counter, i['name'])