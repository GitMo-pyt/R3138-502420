WHITE = '\u001b[47m'
END = '\u001b[0m'
RED = '\u001b[41m'
BLACK = '\u001b[37m'



#1) Флаг Швейцарии
dlin = 26
print(RED + ' ' * dlin + END)
print(RED + ' ' * (dlin // 2 - 2) + WHITE + '    ' + RED + ' ' * (dlin // 2 - 2) + END)
print(RED + ' ' * (dlin // 2 - 5) + WHITE + '          ' + RED + ' ' * (dlin // 2 - 5) + END)
print(RED + ' ' * (dlin // 2 - 2) + WHITE + '    ' + RED + ' ' * (dlin // 2 - 2) + END)
print(RED + ' ' * dlin + END)
print() #разделитель







#2) Потвторяющийся узор
povt = 10 # Количество повторений узора
a2 = ['. . . 111111111 . . .',
'. . 1 . . . . . 1 . .',
'. 1 . . . . . . . 1 .',
'1 . . . . . . . . . 1',
'1 . . . . . . . . . 1',
'1 . . . . . . . . . 1',
'. 1 . . . . . . . 1 .',
'. . 1 . . . . . 1 . .',
'. . .1111111111 . . .']

for i in a2:
    s2 = ''
    for j in i:
        if j == '1':
            s2 += RED + ' ' + END
        else:
            s2 += WHITE + ' ' + END
    s = s2 * 2
    print(s2 * povt)
print()







#3) График функции
a3 = []
for y in range(30, -1, -1):
    m = ['.'] * 91
    m[3 * y] = '1' # Здесь функция x = 3 * y, вот откуда она взялась: Данная функция => y=x/3 => x = 3*y
    a3.append(''.join(m))

for i in a3:
    s3 = ''
    for j in i:
        if j == '1':
            s3 += RED + ' ' + END
        else:
            s3 += WHITE + ' ' + END
    print(s3)
print()








#4) Диаграмма (горизонатальная столбчатая)
counter1, counter2 = 0, 0
for i in open('sequence.txt'):
    if -3 <= float(i) <= 3:
        counter1 += 1
    else:
        counter2 += 1
res = counter1 / counter2
a4 = '1' * int(100 * res) + '.' * (100 - int(100 * res))

s4 = ''
for j in a4:
    if j == '1':
        s4 += RED + ' ' + END
    else:
        s4 += BLACK + ' ' + END

print('|' + '=' * 100 + '|')
print('|' + s4 + '|')
print('|' + '=' * 100 + '|')
