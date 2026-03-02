import ttkbootstrap as tb

from central_bank_of_yemen.controllers.app_controller import AppController
from central_bank_of_yemen.views.login_view import LoginView
from central_bank_of_yemen.views.register_view import RegisterView
from central_bank_of_yemen.views.user_dashboard_view import UserDashboardView


class App(tb.Window):
    WIDTH = 800
    HEIGHT = 950
    VIEWS = (RegisterView, LoginView, UserDashboardView)

    def __init__(self):
        super().__init__()
        self.controller = AppController(self)
        self.frames = {}

        self.iconbitmap('../app.ico')
        self.title('Central Bank of Yemen')

        self.center_window()
        self.minsize(App.WIDTH, App.HEIGHT)

        container = tb.Frame(self)
        container.pack(fill="both", expand=True, padx=50, pady=25)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in App.VIEWS:
            class_name = F.__name__
            frame = F(container, self)
            self.frames[class_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('LoginView')

    def show_frame(self, class_frame_name):
        self.frames[class_frame_name].tkraise()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        left = int(screen_width / 2 - App.WIDTH / 2)
        top = int(screen_height / 2 - App.HEIGHT / 2)

        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+{left}+{top - 50}")
