from central_bank_of_yemen.controllers.auth_controller import AuthController
from central_bank_of_yemen.services.account_service import AccountService
from central_bank_of_yemen.services.user_service import UserService
from central_bank_of_yemen.utilities.user_repo import UserRepo


class AppController:
    def __init__(self, app):
        user_repo = UserRepo()
        account_service = AccountService(user_repo)
        user_service = UserService(user_repo, account_service)

        self.auth = AuthController(app, user_service)