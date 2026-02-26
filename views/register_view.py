import ttkbootstrap as tb
import tkinter as tk


class RegisterView(tb.Frame):
    NEW_FIELD_PADDING = 12
    LABEL_FONT = ("Ubuntu", 12)
    SMALL_FONT = ("Ubuntu", 8)

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        # self.pack(fill="both", expand=True)

        self.build_header()
        self.build_form()
        self.build_buttons()

    def build_header(self):
        header = tb.Frame(self)
        header.pack()

        tb.Label(header, text="Central Bank of Yemen", font=("Ubuntu", 24, "bold")).pack()
        tb.Label(header, text="Registration Form", font=("Ubuntu", 18)).pack(pady=RegisterView.NEW_FIELD_PADDING)

    def build_form(self):
        self.form_frame = tb.Frame(self)
        self.form_frame.pack()

        self.build_username()
        self.build_full_name()
        self.build_dob_gender()
        self.build_address_phone()
        self.build_email_password()

    def build_username(self):
        frame = tb.Frame(self.form_frame)

        frame.pack(fill="x", pady=RegisterView.NEW_FIELD_PADDING)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure((0, 1), weight=1)

        self.username = tb.StringVar()

        tb.Label(frame, text="Username", font=RegisterView.LABEL_FONT).grid(row=0, column=0, sticky="w")
        tb.Entry(frame, textvariable=self.username).grid(row=1, column=0, sticky="ew")

    def build_full_name(self):
        frame = tb.Frame(self.form_frame)

        frame.pack(fill="x", pady=RegisterView.NEW_FIELD_PADDING)
        frame.columnconfigure((0, 1, 2), weight=1)
        frame.rowconfigure((0, 1, 2), weight=1)

        self.first_name = tb.StringVar()
        self.middle_name = tb.StringVar()
        self.last_name = tb.StringVar()

        (tb.Label(frame, text="Full Name", font=RegisterView.LABEL_FONT)
         .grid(row=0, column=0, sticky="w", columnspan=3))

        tb.Entry(frame, textvariable=self.first_name).grid(row=1, column=0, sticky="ew")
        tb.Label(frame, text="First Name", font=RegisterView.SMALL_FONT).grid(row=2, column=0, sticky="w")

        (tb.Entry(frame, textvariable=self.middle_name)
         .grid(row=1, column=1, sticky="ew", padx=RegisterView.NEW_FIELD_PADDING))
        (tb.Label(frame, text="Middle Name", font=RegisterView.SMALL_FONT)
         .grid(row=2, column=1, sticky="w", padx=RegisterView.NEW_FIELD_PADDING))

        tb.Entry(frame, textvariable=self.last_name).grid(row=1, column=2, sticky="ew")
        tb.Label(frame, text="Last Name", font=RegisterView.SMALL_FONT).grid(row=2, column=2, sticky="w")

    def build_dob_gender(self):
        frame = tb.Frame(self.form_frame)

        frame.pack(fill="x", pady=self.NEW_FIELD_PADDING)
        frame.columnconfigure((0, 1), weight=1)
        frame.rowconfigure((0, 1, 2), weight=1)

        self.dob = tb.StringVar()
        self.gender = tb.StringVar()

        tb.Label(frame, text="Date of Birth", font=self.LABEL_FONT).grid(row=0, column=0, sticky="w")
        tb.Entry(frame, textvariable=self.dob).grid(row=1, column=0, sticky="ew")
        tb.Label(frame, text="Use format: YYYY-MM-DD", font=self.SMALL_FONT).grid(row=2, column=0, sticky="w")

        (tb.Label(frame, text="Gender", font=self.LABEL_FONT)
         .grid(row=0, column=1, sticky="w", padx=(RegisterView.NEW_FIELD_PADDING, 0)))
        tb.Combobox(
            frame,
            textvariable=self.gender,
            values=["Male", "Female", "Walmart Bag"],
            state="readonly"
        ).grid(row=1, column=1, sticky="ew", padx=(RegisterView.NEW_FIELD_PADDING, 0))

    def build_address_phone(self):
        frame = tb.Frame(self.form_frame)

        frame.pack(fill="x", pady=self.NEW_FIELD_PADDING)
        frame.columnconfigure(0, weight=4)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure((0, 1), weight=1)

        self.address = tb.StringVar()
        self.phone = tb.StringVar()

        tb.Label(frame, text="Residential Address", font=self.LABEL_FONT).grid(row=0, column=0, sticky="w")
        tb.Entry(frame, textvariable=self.address).grid(row=1, column=0, sticky="ew")

        (tb.Label(frame, text="Phone Number", font=self.LABEL_FONT)
         .grid(row=0, column=1, sticky="w", padx=(RegisterView.NEW_FIELD_PADDING, 0)))
        (tb.Entry(frame, textvariable=self.phone)
         .grid(row=1, column=1, sticky="ew", padx=(RegisterView.NEW_FIELD_PADDING, 0)))

    def build_email_password(self):
        frame = tb.Frame(self.form_frame)

        frame.pack(fill="x", pady=self.NEW_FIELD_PADDING)
        frame.columnconfigure((0, 1), weight=1)
        frame.rowconfigure((0, 1), weight=1)

        self.email = tb.StringVar()
        self.password = tb.StringVar()

        tb.Label(frame, text="Email", font=self.LABEL_FONT).grid(row=0, column=0, sticky="w")
        tb.Entry(frame, textvariable=self.email).grid(row=1, column=0, sticky="ew")

        (tb.Label(frame, text="Password", font=self.LABEL_FONT)
         .grid(row=0, column=1, sticky="w", padx=(RegisterView.NEW_FIELD_PADDING, 0)))
        (tb.Entry(frame, textvariable=self.password, show="*")
         .grid(row=1, column=1, sticky="ew", padx=(RegisterView.NEW_FIELD_PADDING, 0)))

    def build_buttons(self):
        tb.Button(
            self.form_frame,
            text="Register User",
            command=self.app.user_controller.on_register_clicked
        ).pack(pady=RegisterView.NEW_FIELD_PADDING)

    def get_form_data(self):
        return {
            "username": self.username.get(),
            "legal_name": f'{self.first_name.get()} {self.middle_name.get()} {self.last_name.get()}',
            "date_of_birth": self.dob.get(),
            "gender": self.gender.get(),
            "address": self.address.get(),
            "phone_number": self.phone.get(),
            "email": self.email.get(),
            "password": self.password.get(),
        }
