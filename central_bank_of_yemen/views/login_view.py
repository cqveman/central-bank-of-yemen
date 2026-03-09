import customtkinter as ct

from central_bank_of_yemen.views.widgets.button import Button
from central_bank_of_yemen.views.widgets.form_field import FormField


class LoginView(ct.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color='transparent')
        self.app = app

        # To make 'frame' stretch horizontally and stays in the middle of the page
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')

        self.build_header()

        self.username = ct.StringVar()
        self.password = ct.StringVar()

        self.build_form()

    def build_header(self):
        header_frame = ct.CTkFrame(self, fg_color='transparent')
        header_frame.grid(row=0, column=0, sticky='nsew')

        header_frame.columnconfigure(0, weight=1)
        header_frame.rowconfigure((0, 1), weight=1)

        ct.CTkLabel(header_frame, text='Central Bank of Yemen', font=('Ubuntu', 28, 'bold')) \
            .grid(row=0, column=0)
        ct.CTkLabel(header_frame, text='Login', font=('Ubuntu', 22)) \
            .grid(row=0, rowspan=2, column=0)

    def build_form(self):
        form_frame = ct.CTkFrame(self, fg_color='transparent')
        form_frame.grid(row=1, column=0, sticky='nsew')

        # For the form content
        form_frame.columnconfigure(0, weight=1)
        form_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        FormField(form_frame, 'Username', self.username, 0)
        FormField(form_frame, 'Password', self.password, 1, show='*')

        Button(form_frame, 'Login', self.app.controller.auth.on_login_clicked, 2)
        Button(form_frame, 'Create new account', lambda: self.app.show_view("RegisterView"), 2, 2)

    def get_form_data(self):
        return {
            "username": self.username.get().strip(),
            "password": self.password.get(),
        }
