import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile #Функция сохранить как и открыть как
from tkinter.messagebox import showerror #Показ всех ошибок
from tkinter import messagebox #Уведомления приложения

from settings import * #Импортируем настройки

class Text_editor():
    def __init__(self):
        self.file_name = tkinter.NONE
 
    def new_file(self):
        self.file_name = "Без названия"
        text.delete("1.0", tkinter.END)

    def open_file(self):
        inp = askopenfile(mode="r")
        if inp is None:
            return
        data = inp.read()
        text.delete("1.0", tkinter.END)
        text.insert("1.0", data)

    def save_file(self):
        data = text.get("1.0", tkinter.END)
        output = open(self.file_name, "w", encoding="utf-8")
        output.write(data)
        output.close()

    def save_as_file(self):
        output = asksaveasfile(mode="w", defaultextension="txt")
        data = text.get("1.0", tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка", message="Ошибка при сохранении файла")

    def get_info(self):
        messagebox.showinfo("Справка", "Информация о нашем приложении!")


app = tkinter.Tk() #Создаю окно нашего приложения
app.title(APP_NAME) #Название приложения
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

text = tkinter.Text(app, width=WIDTH - 100, height=HEIGHT, wrap="word") #Создали поле с текстом
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) #Создали скролл
scroll.pack(side="right", fill="y") #Разместили скролл
text.configure(yscrollcommand=scroll.set) #Связь текста со скроллом
text.pack() #Разместили поле с текстом

menuBar = tkinter.Menu(app) #Создаем меню

editor = Text_editor()

app_menu = tkinter.Menu(menuBar) #Выпадающее меню у "Файл"
app_menu.add_command(label="Новый файл", command=editor.new_file)
app_menu.add_command(label="Открыть файл", command=editor.open_file)
app_menu.add_command(label="Сохранить", command=editor.save_file)
app_menu.add_command(label="Сохранить как", command=editor.save_as_file)

menuBar.add_cascade(label="Файл", menu=app_menu)
menuBar.add_cascade(label="Справка", command=editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)

app.config(menu=menuBar) #Публикуем меню


app.mainloop() #Бесконечный цикл нашего приложения