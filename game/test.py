from tkinter import *
from tkinter import ttk

root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("300x250")  # устанавливаем размеры окна
icon = PhotoImage(file="image/icon.ico")
root.iconphoto(False, icon)

label1 = Label(root, text="Введите ник первого игрока - ")  # создаем текстовую метку
label1.pack(side="top")  # размещаем метку вверху окна

label2 = Label(root, text="Введите ник второго игрока - ")  # создаем текстовую метку
label2.pack(side="top")

btn_enture = ttk.Button(text="Готово")
btn_enture.pack(anchor="s", fill = X, padx=50 , pady=20)

root.mainloop()