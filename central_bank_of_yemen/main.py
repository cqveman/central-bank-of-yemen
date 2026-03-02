from services.account_service import AccountService
from services.user_service import UserService
from utilities.user_repo import UserRepo
from views.app import App

if __name__ == '__main__':
    app = App()
    app.mainloop()
