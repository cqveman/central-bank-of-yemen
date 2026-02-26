import ttkbootstrap as tb

from views.b_form_view import BuildForm


class RegisterView(BuildForm):

    def __init__(self, parent, app):
        super().__init__(parent, app, title="Create Account")

        self.username = tb.StringVar()
        self.first_name = tb.StringVar()
        self.middle_name = tb.StringVar()
        self.last_name = tb.StringVar()
        self.dob = tb.StringVar()
        self.gender = tb.StringVar()
        self.address = tb.StringVar()
        self.phone = tb.StringVar()
        self.email = tb.StringVar()
        self.password = tb.StringVar()

        # Account section
        self.build_field("Username", self.username)
        self.build_field("Email", self.email)
        self.build_field("Password", self.password, show="*")

        # Personal info
        self.build_row([
            ("First Name", self.first_name, {}),
            ("Middle Name", self.middle_name, {}),
            ("Last Name", self.last_name, {}),
        ])

        cols = self.build_row([
            ("Date of Birth (YYYY-MM-DD)", self.dob, {}),
            ("Gender", self.gender, {"state": "readonly"}),
        ])

        gender_col, gender_entry = cols[1]
        gender_entry.destroy()

        tb.Combobox(
            gender_col,
            textvariable=self.gender,
            values=["Male", "Female"],
            state="readonly"
        ).pack(fill="x")

        # Contact
        self.build_field("Residential Address", self.address)
        self.build_field("Phone Number", self.phone)

        # Buttons
        tb.Button(
            self.card,
            text="Register",
            bootstyle="success",
            command=self.app.user_controller.on_register_clicked
        ).pack(fill="x", pady=(25, 8))

        tb.Button(
            self.card,
            text="Already have an account?",
            bootstyle="link",
            command=lambda: self.app.show_frame("LoginView")
        ).pack()

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
