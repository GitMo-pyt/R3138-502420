import csv, difflib
file = open('books.csv')
table = csv.reader(file, delimiter=';')
table = list(table)
file.close()

def task1(dlin = 30, stolb = 'Название'):
    global table
    count = 0
    ind = table[0].index(stolb)
    return sum([(len(i[ind]) > 30) for i in table[1: ]])

def matches(s1, s2, bust):
    if not bust:
        return False
    s1 = s1.split()
    s2 = s2.split()
    for a in s1:
        if len(difflib.get_close_matches(a, s2)) > 0:
            return True
    return False

def search_author():
    global table
    ind = table[0].index('Автор (ФИО)')
    author = input('Введите автора (\'+\' в конце - расширенный поиск)...')
    bust = author[-1] == '+'
    while True:
        flag = True
        for i in table[1: ]:
            if int(i[6].split('.')[2].split()[0]) < 2018:
                continue
            x = difflib.get_close_matches(author, [i[ind - 1], i[ind]])
            if len(x) > 0:
                print(i)
                flag = False
            elif matches(author, i[ind], bust):
                print(i)
                flag = False
        if not flag: return 0
        elif (author := input('Ничего не найдено. Попробуйте снова или введите "exit" для выхода...')).lower() == 'exit': return 0
        bust = author[-1] == '+'

def generator():
    global table
    file = open('Links.txt', 'a')
    number = 0
    for i in range(803, 2704, 100):
        number += 1
        s = f'{number}. {table[i][3]}. {table[i][1]} - {int(table[i][6].split(".")[2].split()[0])}\n'
        file.write(s)
    file.close()
    print('Файл создан. Название: Links.txt')
search_author()