from services.account_service import AccountService
from services.user_service import UserService
from utilities.user_repo import UserRepo
from views.app import App

if __name__ == '__main__':
    user_repo = UserRepo()
    account_service = AccountService(user_repo)
    user_service = UserService(user_repo, account_service)

    app = App(user_service)
    app.mainloop()
