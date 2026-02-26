import ttkbootstrap as tb


class LoginView(tb.Frame):
    NEW_FIELD_PADDING = 12
    LABEL_FONT = ("Ubuntu", 12)
    SMALL_FONT = ("Ubuntu", 8)

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.build_form()

    def build_form(self):
        self.form_frame = tb.Frame(self)
        self.form_frame.pack()

        self.build_username()
        self.build_password()
        self.build_buttons()

    def build_username(self):
        frame = tb.Frame(self.form_frame)

        frame.pack(fill="x", pady=LoginView.NEW_FIELD_PADDING)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure((0, 1), weight=1)

        self.username = tb.StringVar()

        tb.Label(frame, text="Username", font=LoginView.LABEL_FONT).grid(row=0, column=0, sticky="w")
        tb.Entry(frame, textvariable=self.username).grid(row=1, column=0, sticky="ew")

    def build_password(self):
        frame = tb.Frame(self.form_frame)

        frame.pack(fill="x", pady=LoginView.NEW_FIELD_PADDING)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure((0, 1), weight=1)

        self.password = tb.StringVar()

        tb.Label(frame, text="Password", font=LoginView.LABEL_FONT).grid(row=0, column=1, sticky="w")
        tb.Entry(frame, textvariable=self.password, show="*").grid(row=1, column=1, sticky="ew")

    def build_buttons(self):
        tb.Button(
            self.form_frame,
            text="Log in",
            command=self.app.user_controller.on_login_clicked
        ).pack(pady=LoginView.NEW_FIELD_PADDING)

    def get_form_data(self):
        return {
            "username": self.username.get(),
            "password": self.password.get(),
        }
