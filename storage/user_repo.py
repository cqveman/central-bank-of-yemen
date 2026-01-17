import json
import os
from dataclasses import asdict


class UserRepo:
    USERS_PATH = '../data/users.json'

    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        # if os.path.exists(UserRepo.USERS_PATH) and os.path.getsize(UserRepo.USERS_PATH) > 2:
        with open(UserRepo.USERS_PATH, 'r') as f:
            return json.load(f)

    def save_users(self):
        with open(UserRepo.USERS_PATH, 'w') as f:
            json.dump(self.users.users, f, indent=4)

    def add_user(self, user):
        self.users.append(user)
        self.save_users()
