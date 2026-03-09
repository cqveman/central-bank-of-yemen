from central_bank_of_yemen.services.user_service import UserService


class AuthController:
    def __init__(self, app, user_service: UserService):
        self.app = app
        self.user_service = user_service
        self.__logged_user = None

    def on_register_clicked(self):
        data = self.app.views['RegisterView'].get_form_data()

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
        self.app.show_view('LoginView')

    def on_login_clicked(self):
        data = self.app.views['LoginView'].get_form_data()

        is_logged = self.user_service.login(data['username'], data['password'])
        current_user = self.user_service.get_current_user()

        if is_logged is True and current_user is not None:
            self.__logged_user = current_user
            self.app.show_view('UserDashboardView')
            return

        print('ERROR OCCURRED')

    def get_logged_user(self):
        return self.__logged_user
