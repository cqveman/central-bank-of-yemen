import re
from datetime import datetime


class User:
    def __init__(
            self, username, fullName,
            dob, gender, job,
            address, phNum, email, password
    ):
        self._username = username
        self._fullName = fullName
        self._dob = dob
        self._gender = gender
        self._job = job
        self._address = address
        self._phNum = phNum
        self._email = email
        self._password = password
        self.balance = 0.0

    # USERNAME
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        value = value.strip()
        for user in self.users:
            if user.get('username') == value:
                raise ValueError('Username is unavailable. Please try again.')
        self._username = value

    # NAME
    @property
    def fullName(self):
        return self._fullName

    @fullName.setter
    def fullName(self, value):
        value = value.strip().title()
        if value.replace(' ', '').replace('-', '').isalpha():
            self._fullName = value
        else:
            raise ValueError('Invalid Full Name. Only letters, spaces, and hyphens are allowed.')

    # DATE OF BRITH
    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        value = value.strip()
        try:
            datetime.strptime(value, '%d-%m-%Y')
            self._dob = value
        except ValueError:
            raise ValueError('Invalid Date of Birth. Use format DD-MM-YYYY.')

    # GENDER
    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, value):
        value = value.strip().capitalize()
        if value == 'Male' or value == 'Female':
            self.gender = value
        else:
            raise ValueError('Invalid Gender. Enter either male or female.')

    # JOB
    @property
    def job(self):
        return self.job

    @job.setter
    def job(self, value):
        value = value.strip().title()
        if value.replace(' ', '').isalpha():
            self.job = value
        else:
            raise ValueError('Invalid Job. Only letters are allowed.')

    # ADDRESS
    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, value):
        value = value.strip()
        pattern = r'^\d+, [A-Za-z .]+, [A-Za-z ]+, [A-Za-z]+-\d+$'
        if bool(re.fullmatch(pattern, value)):
            self.address = value
        else:
            raise ValueError('Invalid Address. Use format (building #, Street Name, Neighbourhood, City-Postal Code).')

    # PHONE NUMBER
    @property
    def phNum(self):
        return self.phNum

    @phNum.setter
    def phNum(self, value):
        value = value.strip()
        pattern = r'^(?:\+967)?7\d{8}$'
        if bool(re.fullmatch(pattern, value)):
            self.phNum = value
        else:
            raise ValueError('Invalid Phone Number. Use format 7********.')

    # EMAIL
    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        value = value.strip()
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if bool(re.fullmatch(pattern, value)):
            self.email = value
        else:
            raise ValueError('Invalid Email. Use format example@gmail.com')

    # PASSWORD
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        value = value.strip()
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])[^\s]{8,}$'
        if bool(re.fullmatch(pattern, value)):
            self.password = value
        else:
            raise ValueError('Invalid Password. Must have:\n'
                             'At least 8 characters\n'
                             'Contain at least one uppercase letter\n'
                             'Contain at least one digit\n'
                             'Contain at least one special character')
