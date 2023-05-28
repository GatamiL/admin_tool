import tkinter as tk
from tkinter import *
from PIL import Image
import pystray
import random

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Admin tool')
        Gui.center_window(self.window, 1024, 768)
        self.image = Image.open("image.ico")
        self.window.iconbitmap('image.ico')
        self.menu = (pystray.MenuItem('Развернуть', self.show_window, default = True), pystray.MenuItem('Закрыть', self.quit_window))
        self.main_menu = Menu()
        self.main_menu.add_cascade(label="Файл")
        self.main_menu.add_cascade(label="Настройки", command = self.option_window)
        self.main_menu.add_cascade(label="Выход", command = self.window.destroy)
        self.window.config(menu=self.main_menu)
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.mainloop()

    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (width/2))
        y_cordinate = int((screen_height/2) - (height/2))
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

if __name__ in '__main__':
    Gui()