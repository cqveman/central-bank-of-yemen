import hashlib
import re
import uuid
from datetime import datetime

from models.user import User
from services.account_service import AccountService
from utilities.user_repo import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo, account_service: AccountService):
        self._user_repo = user_repo
        self._account_service = account_service

    def create_user(self, username, legal_name, date_of_birth,
                    gender, address, phone_number,
                    email, password):

        # Checking username uniqueness
        if any(user.username == username for user in self._user_repo.users):
            return False

        # Checking email uniqueness
        if any(user.email == email for user in self._user_repo.users):
            return False

        # Checking user's age
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        today = datetime.today()
        age = (today.year - date_of_birth.year -
               ((today.month, today.day) < (date_of_birth.month, date_of_birth.day,)))  # If True -> 1, False -> 0
        if age < 18:
            return False

        # Checking user's gender
        if gender.capitalize() not in ('Male', 'Female'):
            return False

        # Validate user's email format
        email_regex = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        if not re.match(email_regex, email):
            return False

        # Hashing user's password
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        user_id = str(uuid.uuid4())

        user = User(
            user_id,
            username,
            legal_name,
            date_of_birth,
            gender,
            address,
            phone_number,
            email,
            password_hash,
            self._account_service.open_account(user_id, 'checking', 'YER')
        )

        self._user_repo.add_user(user)
        return True
