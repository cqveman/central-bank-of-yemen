import json
from datetime import datetime
from decimal import Decimal
from json import JSONDecodeError

from central_bank_of_yemen.models.account import Account
from central_bank_of_yemen.models.transaction import Transaction
from central_bank_of_yemen.models.user import User


class UserRepo:
    USERS_PATH = './data/users.json'

    def __init__(self):
        self.users = self.load_users()

    def get_user_by(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def add_user(self, user):
        self.users.append(user)
        self.save_users()

    def load_users(self):
        try:
            with open(UserRepo.USERS_PATH, 'r') as f:
                raw = json.load(f)
            return [self._dict_to_user(user) for user in raw]
        except (FileNotFoundError, JSONDecodeError):
            print('Users file missing or corrupted, starting fresh.')
            return []

    def save_users(self):
        data = [self._user_to_dict(user) for user in self.users]
        with open(UserRepo.USERS_PATH, 'w') as f:
            json.dump(data, f, indent=4)

    def _user_to_dict(self, user: User):
        return {
            'user_id': user.user_id,
            'username': user.username,
            'legal_name': user.legal_name,
            'date_of_birth': user.date_of_birth.isoformat(timespec='seconds'),
            'gender': user.gender,
            'address': user.address,
            'phone_number': user.phone_number,
            'email': user.email,
            'password_hash': user.password_hash,
            'is_active': user.is_active,
            'accounts': [self._account_to_dict(a) for a in user.accounts],
        }
    def _account_to_dict(self, account: Account):
        return {
            'account_id': account.account_id,
            'user_id': account.user_id,
            'account_type': account.account_type,
            'balance': str(account.balance),
            'currency': account.currency,
            'created_at': account.created_at.isoformat(timespec='seconds'),
            'transactions': [self._transaction_to_dict(t) for t in account.transactions],
        }
    def _transaction_to_dict(self, transaction: Transaction):
        return {
            'transaction_id': transaction.transaction_id,
            'account_id': transaction.account_id,
            'amount': str(transaction.amount),
            'currency': transaction.currency,
            'transaction_type': transaction.transaction_type,
            'timestamp': transaction.timestamp.isoformat(timespec='seconds'),
            'to_account_id': transaction.to_account_id,
        }

    def _dict_to_user(self, data: dict):
        return User(
            user_id=data["user_id"],
            username=data["username"],
            legal_name=data["legal_name"],
            date_of_birth=datetime.fromisoformat(data["date_of_birth"]),
            gender=data["gender"],
            address=data["address"],
            phone_number=data["phone_number"],
            email=data["email"],
            password_hash=data["password_hash"],
            is_active=data["is_active"],
            accounts=[self._dict_to_account(a) for a in data.get("accounts", [])],
        )
    def _dict_to_account(self, a: dict):
        return Account(
            account_id=a["account_id"],
            user_id=a["user_id"],
            account_type=a["account_type"],
            balance=Decimal(a["balance"]),
            currency=a["currency"],
            created_at=datetime.fromisoformat(a["created_at"]),
            transactions=[self._dict_to_transaction(t) for t in a.get("transactions", [])],
        )
    def _dict_to_transaction(self, t: dict):
        return Transaction(
            transaction_id=t["transaction_id"],
            account_id=t["account_id"],
            amount=Decimal(t["amount"]),
            currency=t["currency"],
            transaction_type=t["transaction_type"],
            timestamp=datetime.fromisoformat(t["timestamp"]),
            to_account_id=t["to_account_id"],
        )
