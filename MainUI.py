import tkinter as tk
from tkinter import *
from PIL import Image
import pystray


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Admin tool')
        self.window.geometry("1024x768")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (1024/2))
        y_cordinate = int((screen_height/2) - (768/2))
        self.window.geometry("{}x{}+{}+{}".format(1024, 768, x_cordinate, y_cordinate))
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
        child_w.geometry("750x250")
        screen_width = child_w.winfo_screenwidth()
        screen_height = child_w.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (750/2))
        y_cordinate = int((screen_height/2) - (250/2))
        child_w.geometry("{}x{}+{}+{}".format(750, 250, x_cordinate, y_cordinate))
        child_w.title("Настройки")
        child_w.grab_set()

if __name__ in '__main__':
    Gui()