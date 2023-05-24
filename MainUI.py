import tkinter as tk
from tkinter import Menu
from PIL import Image
import pystray


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.image = Image.open("image.ico")
        self.window.iconbitmap('image.ico')
        self.menu = (pystray.MenuItem('Развернуть', self.show_window, default = True), pystray.MenuItem('Закрыть', self.quit_window))
        self.main_menu = Menu()
        self.main_menu.add_cascade(label="Файл")
        self.main_menu.add_cascade(label="Настройки")
        self.main_menu.add_cascade(label="Выход", command = self.window.quit)
        self.window.config(menu=self.main_menu)
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.mainloop()

    def quit_window(self, icon):
        self.icon.stop()
        self.window.destroy()


    def show_window(self, icon):
        self.icon.stop()
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.after(0, self.window.deiconify)


    def withdraw_window(self):
        self.window.withdraw()
        self.icon = pystray.Icon("name", self.image, "title", self.menu)
        self.icon.run()


if __name__ in '__main__':
    Gui()