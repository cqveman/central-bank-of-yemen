import ttkbootstrap as tb

from controllers.user_controller import UserController


class App(tb.Window):
    def __init__(self, user_service):
        super().__init__()
        self.__user_controller = UserController(self, user_service)

        self.iconbitmap('./app.ico')
        self.title('Central Bank of Yemen')

        self.win_width = 800
        self.win_height = 800
        self.dis_width = self.winfo_screenwidth()
        self.dis_height = self.winfo_screenheight()

        left = int(self.dis_width / 2 - self.win_width / 2)
        top = int(self.dis_height / 2 - self.win_height / 2)
        self.geometry(f'{self.win_width}x{self.win_height}+{left}+{top}')

        # Upper frame
        self.upper_frame = tb.Frame(self)
        self.brand_label = tb.Label(self.upper_frame, text='Central Bank of Yemen', font='Ubuntu 24 bold')
        self.register_label = tb.Label(self.upper_frame, text='Registration Form', font='Ubuntu 18')
        # Layout
        self.brand_label.pack()
        self.register_label.pack(pady=10)
        self.upper_frame.pack(pady=30)

        # Main form frame
        self.form_frame = tb.Frame(self)
        self.form_frame.pack()

        # Username frame
        self.username_frame = tb.Frame(self.form_frame)
        self.username_label = tb.Label(self.username_frame, text='Username', font='Ubuntu 12')
        self.username = tb.StringVar()
        self.username_entry = tb.Entry(self.username_frame, textvariable=self.username)
        # Layout
        self.username_frame.columnconfigure(0, weight=1)
        self.username_frame.rowconfigure(0, weight=1)
        self.username_frame.rowconfigure(1, weight=1)
        self.username_label.grid(row=0, column=0, sticky='w', pady=5)
        self.username_entry.grid(row=1, column=0, sticky='w')
        self.username_frame.pack(pady=15, fill='x')

        # Name frame
        self.name_frame = tb.Frame(self.form_frame)
        self.name_label = tb.Label(self.name_frame, text='Full Name', font='Ubuntu 12')
        self.first_name_label = tb.Label(self.name_frame, text='First Name', font='Ubuntu 8')
        self.middle_name_label = tb.Label(self.name_frame, text='Middle Name', font='Ubuntu 8')
        self.last_name_label = tb.Label(self.name_frame, text='Last Name', font='Ubuntu 8')
        self.first_name = tb.StringVar()
        self.middle_name = tb.StringVar()
        self.last_name = tb.StringVar()
        self.first_name_entry = tb.Entry(self.name_frame, textvariable=self.first_name)
        self.middle_name_entry = tb.Entry(self.name_frame, textvariable=self.middle_name)
        self.last_name_entry = tb.Entry(self.name_frame, textvariable=self.last_name)
        # Layout
        self.name_frame.columnconfigure(0, weight=1)
        self.name_frame.columnconfigure(1, weight=1)
        self.name_frame.columnconfigure(2, weight=1)
        self.name_frame.rowconfigure(0, weight=1)
        self.name_frame.rowconfigure(1, weight=1)
        self.name_frame.rowconfigure(2, weight=1)
        self.name_label.grid(row=0, column=0, sticky='w', pady=5)
        self.first_name_entry.grid(row=1, column=0)
        self.middle_name_entry.grid(row=1, column=1, padx=5)
        self.last_name_entry.grid(row=1, column=2)
        self.first_name_label.grid(row=2, column=0, sticky='w', pady=5)
        self.middle_name_label.grid(row=2, column=1, sticky='w', pady=5, padx=5)
        self.last_name_label.grid(row=2, column=2, sticky='w', pady=5)
        self.name_frame.pack(pady=15, fill='x')

        # Date of birth and Gender frame
        self.dob_gender_frame = tb.Frame(self.form_frame)
        self.dob_label = tb.Label(self.dob_gender_frame, text='Date of Birth', font='Ubuntu 12')
        self.dob = tb.StringVar()
        self.dob_entry = tb.Entry(self.dob_gender_frame, textvariable=self.dob)
        self.dob_info_label = tb.Label(self.dob_gender_frame, text='Use format: YYYY-MM-DD', font='Ubuntu 8')
        self.gender_label = tb.Label(self.dob_gender_frame, text='Gender', font='Ubuntu 12')
        self._genders = ['Male', 'Female', 'Walmart Bag']
        self.gender = tb.StringVar()
        self.gender_combo = tb.Combobox(self.dob_gender_frame, textvariable=self.gender)
        self.gender_combo['values'] = self._genders
        # Layout
        self.dob_gender_frame.columnconfigure(0, weight=1)
        self.dob_gender_frame.columnconfigure(1, weight=1)
        self.dob_gender_frame.rowconfigure(0, weight=1)
        self.dob_gender_frame.rowconfigure(1, weight=1)
        self.dob_gender_frame.rowconfigure(2, weight=1)
        self.dob_label.grid(row=0, column=0, sticky='w', pady=5)
        self.dob_entry.grid(row=1, column=0, sticky='w')
        self.dob_info_label.grid(row=2, column=0, sticky='w')
        self.gender_label.grid(row=0, column=1, sticky='w', pady=5)
        self.gender_combo.grid(row=1, column=1, sticky='w')
        self.dob_gender_frame.pack(pady=15, fill='x')

        # Address and Phone Number frame
        self.adrs_phone_frame = tb.Frame(self.form_frame)
        self.adrs_label = tb.Label(self.adrs_phone_frame, text='Residental Address', font='Ubuntu 12')
        self.adrs = tb.StringVar()
        self.adrs_entry = tb.Entry(self.adrs_phone_frame, textvariable=self.adrs)
        self.phone_label = tb.Label(self.adrs_phone_frame, text='Phone Number', font='Ubuntu 12')
        self.phone = tb.StringVar()
        self.phone_entry = tb.Entry(self.adrs_phone_frame, textvariable=self.phone)
        # Layout
        self.adrs_phone_frame.columnconfigure(0, weight=1)
        self.adrs_phone_frame.columnconfigure(1, weight=1)
        self.adrs_phone_frame.rowconfigure(0, weight=1)
        self.adrs_phone_frame.rowconfigure(1, weight=1)
        self.adrs_label.grid(row=0, column=0, sticky='w', pady=5)
        self.adrs_entry.grid(row=1, column=0, sticky='ew')
        self.phone_label.grid(row=0, column=1, sticky='w', pady=5, padx=20)
        self.phone_entry.grid(row=1, column=1, sticky='w', padx=20)
        self.adrs_phone_frame.pack(pady=15, fill='x')

        # Email and Password frame
        self.email_pass_frame = tb.Frame(self.form_frame)
        self.email_label = tb.Label(self.email_pass_frame, text='Email', font='Ubuntu 12')
        self.email = tb.StringVar()
        self.email_entry = tb.Entry(self.email_pass_frame, textvariable=self.email)
        self.pass_label = tb.Label(self.email_pass_frame, text='Password', font='Ubuntu 12')
        self.password = tb.StringVar()
        self.pass_entry = tb.Entry(self.email_pass_frame, show='*', textvariable=self.password)
        # Layout
        self.email_pass_frame.columnconfigure(0, weight=1)
        self.email_pass_frame.columnconfigure(1, weight=1)
        self.email_pass_frame.rowconfigure(0, weight=1)
        self.email_pass_frame.rowconfigure(1, weight=1)
        self.email_label.grid(row=0, column=0, sticky='w', pady=5)
        self.email_entry.grid(row=1, column=0, sticky='w')
        self.pass_label.grid(row=0, column=1, sticky='w', pady=5)
        self.pass_entry.grid(row=1, column=1, sticky='w')
        self.email_pass_frame.pack(pady=15, fill='x')

        # Buttons
        self.register_btn = tb.Button(self.form_frame, text='Register User',
                                      command=self.__user_controller.on_register_clicked)
        self.register_btn.pack(pady=10)
