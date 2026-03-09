import customtkinter as ct

from central_bank_of_yemen.views.widgets.button import Button
from central_bank_of_yemen.views.widgets.form_field import FormField
from central_bank_of_yemen.views.widgets.form_row import FormRow


class RegisterView(ct.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color='transparent')
        self.app = app

        # To make 'frame' stretch horizontally and stays in the middle of the page
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')

        self.build_header()

        self.username = ct.StringVar()
        self.first_name = ct.StringVar()
        self.middle_name = ct.StringVar()
        self.last_name = ct.StringVar()
        self.dob = ct.StringVar()
        self.gender = ct.StringVar()
        self.address = ct.StringVar()
        self.phone = ct.StringVar()
        self.email = ct.StringVar()
        self.password = ct.StringVar()

        self.build_frame()

    def build_header(self):
        header_frame = ct.CTkFrame(self, fg_color='transparent')
        header_frame.grid(row=0, column=0, sticky='nsew')

        header_frame.columnconfigure(0, weight=1)
        header_frame.rowconfigure((0, 1), weight=1)

        ct.CTkLabel(header_frame, text='Central Bank of Yemen', font=('Ubuntu', 28, 'bold')) \
            .grid(row=0, column=0)
        ct.CTkLabel(header_frame, text='Create User', font=('Ubuntu', 22)) \
            .grid(row=1, column=0)

    def build_frame(self):
        form_frame = ct.CTkScrollableFrame(self, fg_color='transparent')
        form_frame.grid(row=1, column=0, sticky='nsew')

        # For the form content
        form_frame.columnconfigure(0, weight=1)
        form_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), uniform='a')

        FormField(form_frame, 'Username', self.username, 0)
        FormRow(
            form_frame, 'Full Name', 1,
            (self.first_name, 'First Name'),
            (self.middle_name, 'Middle Name'),
            (self.last_name, 'Last Name'),
        )
        FormField(form_frame, 'Date of Birth', self.dob, 2)
        FormField(form_frame, 'Gender', self.gender, 3)
        FormField(form_frame, 'Address', self.address, 4)
        FormField(form_frame, 'Phone Number', self.phone, 5)
        FormField(form_frame, 'Email', self.email, 6)
        FormField(form_frame, 'Password', self.password, 7)

        Button(form_frame, 'Register', self.app.controller.auth.on_register_clicked, 8)

    def get_form_data(self):
        legal_name = " ".join(filter(None, [
            self.first_name.get().strip(),
            self.middle_name.get().strip(),
            self.last_name.get().strip(),
        ]))

        return {
            "username": self.username.get().strip(),
            "legal_name": legal_name,
            "date_of_birth": self.dob.get().strip(),
            "gender": self.gender.get(),
            "address": self.address.get().strip(),
            "phone_number": self.phone.get().strip(),
            "email": self.email.get().strip(),
            "password": self.password.get(),
        }
