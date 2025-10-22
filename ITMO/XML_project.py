import xml.dom.minidom as minidom

def data(ind): # Вытягивание данных по уже найденному тегу
    global xml_data
    for d, d_el in enumerate(xml_data[ind:]):
        if d_el == '<':
            return xml_data[ind:ind + d]

def search(i, el): #Поиск тегов
    global xml_data
    if el == 'N' and xml_data[i:i + 4] == 'Name' and xml_data[i - 1] != '/':
        name = data(i + 5)
        for c, c_el in enumerate(xml_data[i: ]):
            if c_el == 'C' and xml_data[i + c:i + c + 8] == 'CharCode' and xml_data[i + c - 1] != '/':
                ans = data(i + c + 9)
                return [name, ans]

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

answer = dict()
for ix, elx in enumerate(xml_data):
    res = search(ix, elx)
    if res != None:
        answer[res[0]] = res[1] # Вот здесь заполняется итоговый словарь

for i in answer: # Просто красивый вывод
    print(f'{i} - {answer[i]}')