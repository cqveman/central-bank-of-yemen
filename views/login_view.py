import ttkbootstrap as tb

from views.b_form_view import BuildForm


class LoginView(BuildForm):

    def __init__(self, parent, app):
        super().__init__(parent, app, title="Login")

        self.username = tb.StringVar()
        self.password = tb.StringVar()

        self.build_field("Username", self.username)
        self.build_field("Password", self.password, show="*")

        tb.Button(
            self.card,
            text="Login",
            bootstyle="primary",
            command=self.app.user_controller.on_login_clicked
        ).pack(fill="x", pady=(25, 8))

        tb.Button(
            self.card,
            text="Create new account",
            bootstyle="link",
            command=lambda: self.app.show_frame("RegisterView")
        ).pack()

    def get_form_data(self):
        return {
            "username": self.username.get().strip(),
            "password": self.password.get(),
        }
