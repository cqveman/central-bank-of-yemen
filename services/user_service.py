import re
import uuid
from datetime import datetime

from models.user import User
from storage.user_repo import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def create_user(self, username, legal_name, date_of_birth,
                    gender, address, phone_number,
                    email, password_hash):

        # Checking username uniqueness
        if any(user.username == username for user in self.user_repo.users):
            return False

        # Checking email uniqueness
        if any(user.email == email for user in self.user_repo.users):
            return False

        # Checking user's age
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

        user_id = str(uuid.uuid4())

        user = User(
            user_id=user_id,
            username=username,
            legal_name=legal_name,
            date_of_birth=date_of_birth,
            gender=gender,
            address=address,
            phone_number=phone_number,
            email=email,
            password_hash=password_hash,
            accounts=[],
        )

        self.user_repo.add_user(user)
        return True
