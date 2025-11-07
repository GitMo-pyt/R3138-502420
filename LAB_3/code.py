import tkinter as tk
import itertools as tls
from random import *

def get():
    label_e['text'] = keygen(entry.get())

def check(s = ''):
    if len(s) != 4 or not all(i in '0123456789' for i in s):
        return 0
    return 1

def keygen(first_part):
    if not check(first_part):
        return 'Неверный ввод'
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    s1 = [''.join(i) for i in tls.permutations(str(first_part[:3]))]
    s2 = [''.join(i) for i in tls.permutations(str(first_part[3: ]))]
    choice1 = int(choice(s1))
    choice2 = int(choice(s2))
    result += f'{choice1}{choice(alf)}{choice(alf)}-{choice2}{choice(alf)}{choice(alf)}-{str(choice1 + choice2).zfill(4)}'
    return result

window = tk.Tk()
window.title("KeyGen")
window.geometry(f"{int(800 * 0.75)}x{int(480 * 0.75)}")
window.resizable(False, False)
bg_img = tk.PhotoImage(file = 'img.png')




label_bg = tk.Label(window, image = bg_img) # Задний фон
label_bg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

entry = tk.Entry(window, font = 'Arial 20', width = 6) # Пользовательский ввод
entry.place(x = 260, y = 100)

btn = tk.Button(window, font = 'Arial 20', text='OK', width = 10, command = get) # Кнопка "OK"
btn.place(x = 220, y = 150)

label_e = tk.Label(window, bg='white', fg='black', width = 15, font = 'Arial 30') # Вывод
label_e.place(x = 130, y = 10)




window.mainloop()