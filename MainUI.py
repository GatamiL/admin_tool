import tkinter as tk
from PIL import Image
import pystray


class Gui():
    def __init__(self):
        self.window = tk.Tk()
        self.image = Image.open("image.ico")
        self.window.iconbitmap('image.ico')
        self.menu = (pystray.MenuItem('Развернуть', self.show_window, default = True), pystray.MenuItem('Выйти', self.quit_window))
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