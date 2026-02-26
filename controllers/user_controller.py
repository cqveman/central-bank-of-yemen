from services.user_service import UserService


class UserController:
    def __init__(self, app, user_service: UserService):
        self.app = app
        self.user_service = user_service

    def on_register_clicked(self):
        data = self.app.frames['RegisterView'].get_form_data()

        user = self.user_service.create_user(
            username=data['username'],
            legal_name=data['legal_name'],
            date_of_birth=data['date_of_birth'],
            gender=data['gender'],
            address=data['address'],
            phone_number=data['phone_number'],
            email=data['email'],
            password=data['password']
        )

        print('Created user successfully!' if user is True
              else "Error when creating user.")

    def on_login_clicked(self):
        data = self.app.frames['LoginView'].get_form_data()

        is_he_logged, user = self.user_service.login(data['username'], data['password'])

        print(f'Welcome back {user.legal_name}!' if is_he_logged
              else "Username or password is incorrect.")
