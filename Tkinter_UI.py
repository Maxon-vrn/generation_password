
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
import string
import random
import webbrowser

window = Tk()
window.title('Генератор паролей')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 300  # смещение от середины
h = h - 200
#window.minsize(600, 400)
# window.maxsize(550, 350)
window.geometry('600x350+{}+{}'.format(w, h))  # задали размеры окна to center window
window.resizable(False, False)  #отключение возможности раскрыть окно наполную или растянуть
#photo = PhotoImage(file='./data/index.png')  # create object photo
#window.iconphoto(False, photo)
# window.config(bg='#464646')  # цвет фона окна

#импортируем в строковом варинте буквы и цифры для будующей обработки и добавления в список
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
        #print(password_string) - проверка вывода в терминале


def ABC_funcktion():
    if enabled_ABC.get() == 1:  # изменения состояния кнопки - true or false, как изменять состояние в обратную сторону
        global password_string
        password_string.insert(1, apperstring)  # изменение состояния глобальной переменной
        print(password_string)
    else:
        for i in range(len(password_string)):
            if password_string[i] == apperstring:
                password_string.pop(i)
        #print(password_string) - проверка вывода в терминале


def num_funcktion():
    if enabled_num.get() == 1:  # изменения состояния кнопки - true or false, как изменять состояние в обратную сторону
        global password_string
        password_string.insert(1, numer)  # изменение состояния глобальной переменной
        print(password_string)
    else:
        for i in range(len(password_string)):
            if password_string[i] == numer:
                password_string.pop(i)
        #print(password_string) - проверка вывода в терминале


def simbols_funcktion():
    if enabled_sumbol.get() == 1:  # изменения состояния кнопки - true or false, как изменять состояние в обратную сторону
        global password_string
        password_string.insert(1, punctuation)  # изменение состояния глобальной переменной
        print(password_string)
    else:
        for i in range(len(password_string)):
            if password_string[i] == punctuation:
                password_string.pop(i)
        #print(password_string) - проверка вывода в терминале


def generate_password():  # generate password
    if len(password_string) == 0:  # проверка списка по длинне чтобы было из чего собирать пароль и обрабатывает пустое значение
        table_name.delete(0, 'end')
        table_name.insert(0, 'Выберите несколько параметров')
    else:
        table_name.delete(0,'end') #очищаем ранее появившиеся сообщение
        string_pass = ''
        global count_pass  # количество паролей для генерации - число
        global len_pass  # длинна сгенерированных пароля
        global spisok_generate_pass

        spisok_generate_pass = []  # обнуляем список сохранения для очистки и формирования нового списка паролей

        if count_pass.get():
            label_count_pass["text"] = count_pass.get()  # количество сгенерированных пароля
            count_password = int(label_count_pass["text"])
        else:
            table_name.delete(0, 'end')  # очистим окно перед выводом информации
            table_name.insert(0, 'Выберите количество паролей')

        if len_pass.get():
            label_len_pass["text"] = len_pass.get()  # длинна сгенерированных пароля
            len_password = int(label_len_pass["text"])
        else:
            table_name.delete(0, 'end')  # очистим окно перед выводом информации
            table_name.insert(0, 'Выберите длинну пароля')


        for i in password_string:  # обработка полученных значений из списка
            for j in i:  # проход выбраного значения списка по симпвольно
                string_pass += j

        if count_password > 0 and len_password > 0:
            while count_password:
                passw = random.sample(string_pass, (len_password))  # в переменную помещается первый сгенерированный пароль
                spisok_generate_pass.append(''.join(passw))  # сохраняются данные в список для будующего сохранения на компьютере
                table_name.insert(0, ''.join(passw))  # выводится пароль в строку номер -ind,значение - ''.join(passw).
                count_password += -1

        else:
            table_name.delete(0,'end')  #очистим окно перед выводом информации
            table_name.insert(0, 'Выберите количество символов для пароля и количество нужных паролей')


def save_pass():  # функция сохранения сгенерованного пароля

    global spisok_generate_pass
    def save_text():    #сохранение текста
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        with open(file_name, "w+") as f:
            for i in spisok_generate_pass:
                f.write(i + '\n')

    def about():  # вызов окна подтверждения выполненной операции сохранения
        window = Toplevel()
        w = window.winfo_screenwidth()
        h = window.winfo_screenheight()
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 180  # смещение от середины
        h = h - 100
        window.geometry('400x200+{}+{}'.format(w, h))
        # window['bg'] = 'grey'
        window.overrideredirect(True)
        Label(window, text="Пароль успешно сохранен в текущей директории").pack(expand=1)
        window.after(5000, lambda: window.destroy())

    if len(spisok_generate_pass) > 0:
        save_text()
        about()

    else:   #обработкка исключений попытки сохранить пустое окно
        table_name.delete(0, 'end')  # очистим окно перед выводом информации
        table_name.insert(0, 'Вы ничего не сгенерировали!')
        table_name.insert(1, '1)Выберите параметры')
        table_name.insert(2, '2)Выберите количество символов')
        table_name.insert(3, '3)Выберите количество паролей')



def about_autor():
    window = Tk()
    window.title("Об авторе")
    window.geometry('600x300+200+100')
    window.resizable(False, False)

    def callback_max():
        webbrowser.open_new("https://t.me/Fisenko_Maxim")

    def callback_vera():
        webbrowser.open_new("https://t.me/VeraGran")

    Label(window, text="Программа написана для упрощения создания паролей на каждый день!",font=('Arial', 12)).grid(row=0, column=0,columnspan=7, padx=20,pady=20)

    Label(window,text='Написал программу: ').grid(row=2, column=0, sticky=W, padx=5,pady=5)
    Button(window,text='https://t.me/Fisenko_Maxim ',command=callback_max).grid(row=2, column=1, sticky=W)


    Label(window,text='Протестировала программу: ').grid(row=3, column=0, sticky=W, padx=5)
    Button(window,text='https://t.me/VeraGran ',command=callback_vera).grid(row=3, column=1, sticky=W)

    window.mainloop()



Label(text="Приветствую тебя друг! Давай соберем тебе стойкий пароль!", font=('Arial', 14)).grid(row=0, column=0,
                                                                                                 columnspan=7, padx=20)
Label(text="Выбери подходящие тебе параметры:", font=('Arial', 14)).grid(row=1, column=0, columnspan=5, pady=10)

Label(text='Буквы нижнего регистра: ').grid(row=4, column=0, sticky=W,padx=5)  # текст
enabled_abc = IntVar()
abc = Checkbutton(text='Да/Нет', command=abc_funcktion,variable=enabled_abc)
abc.grid(row=4, column=1)  # bolean var

table_name = Listbox()  # Text(width=20,height=7)
table_name.grid(row=4, column=2, columnspan=6, rowspan=6, sticky=W + E + N + S,padx=5)  # rowspa and colomnspan - объединение ячеек
scroll = Scrollbar(command=table_name.yview)
scroll.grid(row=4, column=6,columnspan=6,rowspan=6,sticky=W + E + N + S)
table_name.config(yscrollcommand=scroll.set)

Label(text='Буквы верхнего регистра: ').grid(row=5, column=0, sticky=W,padx=5)
enabled_ABC = IntVar()
Checkbutton(text='Да/Нет', command=ABC_funcktion, variable=enabled_ABC).grid(row=5, column=1)

Label(text='Использовать цифры: ').grid(row=6, column=0, sticky=W,padx=5)
enabled_num = IntVar()
Checkbutton(text='Да/Нет', command=num_funcktion, variable=enabled_num).grid(row=6, column=1)

Label(text='Использовать символы: ').grid(row=7, column=0, sticky=W,padx=5)
enabled_sumbol = IntVar()
Checkbutton(text='Да/Нет', command=simbols_funcktion, variable=enabled_sumbol).grid(row=7, column=1)

Label(text="Длина паролей:").grid(row=8, column=0, sticky=W,padx=5)
len_pass = Spinbox(width=7, from_=1, to=50)
len_pass.grid(row=8, column=1, pady=20)
label_len_pass = Label()

Label(text="Количество паролей:").grid(row=9, column=0, sticky=W,padx=5)
count_pass = Spinbox(width=7, from_=1, to=50)
count_pass.grid(row=9, column=1, pady=20)
label_count_pass = Label()

Button(text="Об авторе", command=about_autor).grid(row=10, column=0, pady=10, ipadx=10)
Button(text="Сгенерировать", command=generate_password).grid(row=10, column=2)
Button(text="Сохранить", command=save_pass).grid(row=10, column=3)

window.mainloop()
