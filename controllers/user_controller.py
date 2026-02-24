from services.user_service import UserService


class UserController:
    def __init__(self, app, user_service: UserService):
        self.app = app
        self.user_service = user_service

    def on_register_clicked(self):
        username = self.app.username.get()
        legal_name = f'{self.app.first_name.get()} {self.app.middle_name.get()} {self.app.last_name.get()}'
        date_of_birth = self.app.dob.get()
        gender = self.app.gender.get()
        address = self.app.adrs.get()
        phone_number = self.app.phone.get()
        email = self.app.email.get()
        password = self.app.password.get()

        self.user_service.create_user(username, legal_name, date_of_birth,
                                      gender, address, phone_number,
                                      email, password)
