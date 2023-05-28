import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
from textwrap import wrap
from PIL import Image, ImageTk
import pystray

from plyer.utils import platform
from plyer import notification


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Admin tool')
        Gui.center_window(self.window, 1024, 805)
        self.image = Image.open("image.ico")
        self.window.iconbitmap('image.ico')
        StatusBar = Label(self.window, relief = RIDGE, text = "Готово. Последнее сканирование: (28.05.2023 20:00:47)")
        StatusBar.pack(side = BOTTOM, expand = YES, fill = X, anchor = SW, pady = (2,0))
        self.menu = (pystray.MenuItem('Развернуть', self.show_window, default = True), pystray.MenuItem('Сканировать', lambda: self.warning_popup("asdasdasd")),pystray.MenuItem('Закрыть', self.quit_window))
        self.main_menu = Menu()
        self.main_menu.add_cascade(label="Файл",command=lambda: self.warning_popup("asdasdasd"))
        self.main_menu.add_cascade(label="Настройки", command = self.option_window)
        self.main_menu.add_cascade(label="Выход", command = self.window.destroy)
        self.window.config(menu=self.main_menu)
        '''Версия с плитками
        for j in range(1,7):
            exec('self.frame_%s = Frame(self.window)' % j)
            exec('self.frame_%s.pack(pady=1)' % j)
            for i in range(1, 5):
                exec('self.label_%s = Label(self.frame_%s, width=35, height=8, bg="#00B341")' % (i+10*j, j))
                exec('self.label_%s.pack(side=LEFT, padx=1, pady=1)' % (i+10*j))
                exec('self.ip_%s = tk.Label(self.label_%s, text="192.168.999.999", bg="#00B341")' % (i+10*j,i+10*j))
                exec('self.ip_%s.place(x=1, y=1)' % (i+10*j))
                exec('self.ip_%s.config(font=("Courier", 13))' % (i+10*j))
                exec('self.name_%s = tk.Text(self.label_%s,width=24, height=3, bg="#00B341")' % (i+10*j,i+10*j))
                exec('self.name_%s.place(x=1, y=25)' % (i+10*j))
                exec('self.name_%s.config(font=("Courier", 13))' % (i+10*j))
                exec('self.name_%s.insert("1.0","Серверная Связистов Организации МММ!")' % (i+10*j))
                exec('self.name_%s.config(state=DISABLED)' % (i+10*j))
                exec('self.Check_%s = tk.Checkbutton(self.label_%s, text="Уведомлять при отключении", bg="#00B341")' % (i+10*j,i+10*j))
                exec('self.Check_%s.place(x=1, y=95)' % (i+10*j))
                exec('self.edit_%s = tk.Button(self.label_%s, text="Изменить")' % (i+10*j,i+10*j))
                exec('self.edit_%s.place(x=193, y=98)' % (i+10*j))
                exec('self.edit_%s.config(font=("Courier", 7))' % (i+10*j))
        '''
        '''Версия со списком'''

        self.edit = tk.Button(self.window, text="Добавить устройство")
        self.edit.pack(side=LEFT,padx=10, pady=10)
        self.edit = tk.Button(self.window, text="Изменить")
        self.edit.pack(side=LEFT,padx=10, pady=10)
        self.edit = tk.Button(self.window, text="Сканировать")
        self.edit.pack(side=LEFT,padx=10, pady=10)
        self.edit = tk.Button(self.window, text="Открыть в программе")
        self.edit.pack(side=LEFT,padx=10, pady=10)

        self.tree = ttk.Treeview(self.window, column=("id", "ip", "name", "status", "check","program"), show='headings', height=5)
        self.tree.heading("id", text="п/п")
        self.tree.column("id", minwidth=0, width=30, stretch=NO)
        self.tree.heading("# 2", text="IP")
        self.tree.column("#2", minwidth=0, width=100, stretch=NO)
        self.tree.heading("# 3", text="Наименование")
        self.tree.column("#3", minwidth=0, width=558, stretch=NO)
        self.tree.heading("# 4", text="Состояние")
        self.tree.column("#4", minwidth=0, width=70, stretch=NO)
        self.tree.heading("# 5", text="Следить")
        self.tree.column("#5", minwidth=0, width=60, stretch=NO)
        self.tree.heading("# 6", text="Программа")
        self.tree.column("#6", minwidth=0, width=201, stretch=NO)
        self.tree.place(x=1, y=60, width=1021, height=650)
        vsb = ttk.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        vsb.place(x=1003, y=85, height=623)
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("102", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("103", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("104", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","telnet"))
        self.tree.insert('', 'end', values=("105", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","telnet"))
        self.tree.insert('', 'end', values=("106", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","telnet"))
        self.tree.insert('', 'end', values=("100", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","telnet"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","telnet"))
        self.tree.insert('', 'end', values=("102", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","telnet"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("105", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("106", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("100", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("102", "192.168.254.254", "Сервер Программистов", "Оффлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("103", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("104", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("105", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("106", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("100", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("102", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("103", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Putty"))
        self.tree.insert('', 'end', values=("104", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("105", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("106", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("100", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("102", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("103", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("104", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("105", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("106", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("100", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("102", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("103", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("104", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("105", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("106", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("100", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("101", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("102", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("103", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("104", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("105", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))
        self.tree.insert('', 'end', values=("106", "192.168.254.254", "Сервер Программистов", "Онлайн","Да","Браузер"))

        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.mainloop()

    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (width/2))
        y_cordinate = int((screen_height/2) - (height/2))
        win.minsize(width, height)
        win.maxsize(width, height)
        win.geometry("{}x{}+{}+{}".format(width, height, x_cordinate, y_cordinate))

    def quit_window(self, icon):
        self.icon.stop()
        self.window.destroy()

    def show_window(self, icon):
        self.icon.stop()
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.after(0, self.window.deiconify)

    def withdraw_window(self):
        self.window.withdraw()
        self.icon = pystray.Icon("Admin tool", self.image, "Admin tool", self.menu)
        self.icon.run()
    
    def option_window(self):
        child_w = Toplevel(self.window)
        child_w.iconbitmap('image.ico')
        Gui.center_window(child_w, 750, 250)
        child_w.title("Настройки")
        child_w.grab_set()

    
    def warning_popup(self, devices):
        notification.notify(
        title='Внимание',
        message=f'Устройство {devices} недоступно',
        app_name='Admin tool',
        app_icon='warning.{}'.format(
            'ico' if platform == 'win' else 'png'
        ),
        timeout = 2
        )

if __name__ in '__main__':
    Gui()