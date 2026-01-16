import re

#Задание 1
task1 = list(map(lambda x: x.replace('\n', ''), open('task1-en.txt')))
answers1 = []
for line in task1:
    m1 = re.findall('\s[-A-z]+\.', line)
    for l in m1: answers1.append(l) if m1 != [] else None
for i in answers1:
    print(i)
input('Нажмите "Enter" для перехода к следующему заданию >>>')


#Задание 2
task2 = map(lambda x: x.replace('\n', ''), open('task2.txt', encoding='UTF-16LE'))
answers2 = []
for line in task2:
    m2 = re.findall('\d+x\d+', line)
    for l in m2: answers2.append(l) if m2 != [] else None
for i in answers2:
    print(i)
input('Нажмите "Enter" для перехода к следующему заданию >>>')


#Задание 3
task3 = list(open('task3.txt'))[0].split()
file = open('answer3_file.csv', 'w')
person = dict()
for line in task3:
    id = re.fullmatch('\d+', line)
    name = re.fullmatch('[A-Z][a-z]+', line)
    email = re.fullmatch('[^@]+@[A-z-]+\.[a-z]+', line)
    date = re.fullmatch('\d{4}-\d{2}-\d{2}', line)
    web = re.fullmatch('http{1}s?://.+', line)
    if id != None: person['id'] = line
    if name != None: person['name'] = line
    if email != None: person['email'] = line
    if date != None: person['date'] = line
    if web != None: person['web'] = line
    if len(person) == 5:
        file.write(f"{person['id']}; {person['name']}; {person['email']}; {person['date']}; {person['web']}\n")
        person = dict()
file.close()
print('Файл успешно создан. Название - answer3_file.csv')