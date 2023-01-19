from tkinter import *
import string
import random
import os

window = Tk()
window.title('Генератор паролей')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 300  # смещение от середины
h = h - 200
window.minsize(600, 400)
# window.maxsize(550, 350)
window.geometry('600x400+{}+{}'.format(w, h))  # задали размеры окна to center window
photo = PhotoImage(file='./data/index.png')  # create object photo
window.iconphoto(False, photo)  # не работает отображение иконки фото в верхней части !!!
# window.config(bg='#464646')  # цвет фона окна

'''импортируем в строковом варинте буквы и цифры для будующей обработки и добавления в список'''
lowerstring = string.ascii_lowercase
apperstring = string.ascii_uppercase
numer = string.digits
punctuation = string.punctuation
password_string = []  # собераем символы из которых в дальнейшем будет генерироваться пароль
spisok_generate_pass = []  # список уже с генерированными паролями для сохранения его на компьютере пользователя


def abc_funcktion():
    if enabled_abc.get() == 1:  # изменения состояния кнопки - true or false, как изменять состояние в обратную сторону
        global password_string
        password_string.insert(0, lowerstring)  # изменение состояния глобальной переменной
        print(password_string)
    else:
        password_string.pop(0)
        print(password_string)


def ABC_funcktion():
    if enabled_ABC.get() == 1:  # изменения состояния кнопки - true or false, как изменять состояние в обратную сторону
        global password_string
        password_string.insert(1, apperstring)  # изменение состояния глобальной переменной
        print(password_string)
    else:
        for i in range(len(password_string)):
            if password_string[i] == apperstring:
                password_string.pop(i)
        print(password_string)


def num_funcktion():
    if enabled_num.get() == 1:  # изменения состояния кнопки - true or false, как изменять состояние в обратную сторону
        global password_string
        password_string.insert(1, numer)  # изменение состояния глобальной переменной
        print(password_string)
    else:
        for i in range(len(password_string)):
            if password_string[i] == numer:
                password_string.pop(i)
        print(password_string)


def simbols_funcktion():
    if enabled_sumbol.get() == 1:  # изменения состояния кнопки - true or false, как изменять состояние в обратную сторону
        global password_string
        password_string.insert(1, punctuation)  # изменение состояния глобальной переменной
        print(password_string)
    else:
        for i in range(len(password_string)):
            if password_string[i] == punctuation:
                password_string.pop(i)
        print(password_string)


def generate_password():  # generate password
    if len(password_string) == 0:  # проверка списка по длинне чтобы было из чего собирать пароль,и обрабатывает пустое значение
        table_name.insert(0, 'Выберите несколько параметров для генерации')
    else:
        table_name.delete(0,
                          'end')  # это должно было очистить содержимое окна,перед выводом в него сгеенерированного результата
        string_pass = ''
        global count_pass  # количество паролей для генерации - число
        global len_pass  # длинна сгенерированных пароля
        global spisok_generate_pass

        spisok_generate_pass = []  # обнуляем список сохранения для очистки и формирования нового списка паролей

        label_len_pass["text"] = len_pass.get()  # длинна сгенерированных пароля
        len_password = int(label_len_pass["text"])

        label_count_pass["text"] = count_pass.get()  # количество сгенерированных пароля
        count_password = int(label_count_pass["text"])

        for i in password_string:  # обработка полученных значений из списка
            for j in i:  # проход выбраного значения списка по симпвольно
                string_pass += j

        while count_password:
            passw = random.sample(string_pass, (len_password))  # в переменную помещается первый сгенерированный пароль
            spisok_generate_pass.append(
                ''.join(passw))  # сохраняются данные в список для будующего сохранения на компьютере
            table_name.insert(0, ''.join(passw))  # выводится пароль в строку номер -ind,значение - ''.join(passw).
            count_password += -1


def save_pass():  # функция сохранения сгенерованного пароля

    global spisok_generate_pass

    with open("./Generate_password.txt", "w+") as f:
        for i in spisok_generate_pass:
            f.write(i + '\n')


def about_autor():
    window = Tk()
    window.title("Об авторе")
    window.geometry('600x400+200+100')
    window.minsize(400, 400)
    window.config(bg='#464646')

    priv = Label(window, text="Программа написана для упрощения создания паролей на каждый день!",
                 height=2, width=60,  # высота и ширина по количеству знаков
                 font=('Arial', 12),
                 fg='lightblue',
                 bg='#464646')
    priv.grid(row=0, column=0)


Label(text="Приветствую тебя друг! Давай соберем тебе стойкий пароль!", font=('Arial', 14)).grid(row=0, column=0,
                                                                                                 columnspan=5, pady=10)
Label(text="Выбери подходящие тебе параметры:", font=('Arial', 14)).grid(row=1, column=0, columnspan=5, pady=10)

Label(text='Буквы нижнего регистра: ').grid(row=4, column=0, sticky=W)  # текст
enabled_abc = IntVar()
abc = Checkbutton(text='Да/Нет', command=abc_funcktion,
                  variable=enabled_abc)  # variable=enabled - обработка изменения состояния
abc.grid(row=4, column=1)  # bolean var

table_name = Listbox()  # Text(width=20,height=7)
table_name.grid(row=4, column=2, columnspan=2, rowspan=5, sticky=W + E + N + S,
                padx=5)  # rowspa and colomnspan - объединение ячеек
# scroll = Scrollbar(command=table_name.yview)
# scroll.grid(row=4, column=3,sticky=N+S+E)
# table_name.config(yscrollcommand=scroll.set)

Label(text='Буквы верхнего регистра: ').grid(row=5, column=0, sticky=W)
enabled_ABC = IntVar()
Checkbutton(text='Да/Нет', command=ABC_funcktion, variable=enabled_ABC).grid(row=5, column=1)

Label(text='Использовать цифры: ').grid(row=6, column=0, sticky=W)
enabled_num = IntVar()
Checkbutton(text='Да/Нет', command=num_funcktion, variable=enabled_num).grid(row=6, column=1)

Label(text='Использовать символы: ').grid(row=7, column=0, sticky=W)
enabled_sumbol = IntVar()
Checkbutton(text='Да/Нет', command=simbols_funcktion, variable=enabled_sumbol).grid(row=7, column=1)

Label(text="Длинна паролей:").grid(row=8, column=0, sticky=W)  # вытянуть количество from_ ?
len_pass = Spinbox(width=7, from_=1, to=100)
len_pass.grid(row=8, column=1, pady=20)
label_len_pass = Label()

Label(text="Количество паролей:").grid(row=9, column=0, sticky=W)  # вытянуть количество from_ ?
count_pass = Spinbox(width=7, from_=1, to=100)
count_pass.grid(row=9, column=1, pady=20)
label_count_pass = Label()

Button(text="Об авторе", command=about_autor).grid(row=10, column=0, pady=10, padx=10)
Button(text="Сгенерировать", command=generate_password).grid(row=10, column=2)
Button(text="Сохранить", command=save_pass).grid(row=10, column=3)

window.mainloop()

#hi