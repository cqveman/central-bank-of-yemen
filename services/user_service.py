from models.user import User
from storage.user_repo import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def create_user(self, username, legal_name, date_of_birth,
                    gender, address, phone_number,
                    email, password_hash, accounts):
        user = User(
            len(self.user_repo.users) + 1,
            username,
            legal_name,
            date_of_birth,
            gender,
            address,
            phone_number,
            email,
            password_hash,
            accounts
        )

        self.user_repo.add_user(user)
        return True
