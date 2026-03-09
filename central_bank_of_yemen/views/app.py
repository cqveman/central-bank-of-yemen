import customtkinter as ct

from central_bank_of_yemen.controllers.app_controller import AppController
from central_bank_of_yemen.views.login_view import LoginView
from .settings import *

from central_bank_of_yemen.views.register_view import RegisterView


class App(ct.CTk):

    def __init__(self):
        super().__init__()
        self.controller = AppController(self)
        self.views = {}

        self.iconbitmap('../app.ico')
        self.title('Central Bank of Yemen')

        self.center_window()
        self.minsize(WIDTH, HEIGHT)

        container = ct.CTkFrame(self)
        container.pack(fill="both", expand=True, padx=32, pady=32)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        for v in (LoginView, RegisterView):
            view = v(container, self)
            self.views[v.__name__] = view
            view.grid(row=0, column=0, sticky="nsew")

        self.show_view('LoginView')

    def show_view(self, view):
        if view in self.views:
            self.views[view].tkraise()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        left = int(screen_width / 2 - WIDTH / 2)
        top = int(screen_height / 2 - HEIGHT / 2)

        self.geometry(f"{WIDTH}x{HEIGHT}+{left}+{top}")
