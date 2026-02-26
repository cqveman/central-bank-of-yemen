import ttkbootstrap as tb
import tkinter as tk

from controllers.user_controller import UserController
from views.register_view import RegisterView


class App(tb.Window):
    WIDTH = 800
    HEIGHT = 840

    def __init__(self, user_service):
        super().__init__()
        self.user_controller = UserController(self, user_service)

        self.iconbitmap('./app.ico')
        self.title('Central Bank of Yemen')

        self.center_window()
        self.minsize(App.WIDTH, App.HEIGHT)

        self.main = tb.Frame(self)
        self.main.pack(fill="both", expand=True, padx=50, pady=25)

        self.view_register()

    def view_register(self):
        for item in self.main.winfo_children():
            item.destroy()
        RegisterView(self.main, self)

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        left = int(screen_width / 2 - App.WIDTH / 2)
        top = int(screen_height / 2 - App.HEIGHT / 2)

        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+{left}+{top}")
