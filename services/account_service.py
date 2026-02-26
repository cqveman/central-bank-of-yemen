import uuid
from datetime import datetime
from decimal import Decimal

from models.account import Account
from utilities.user_repo import UserRepo
from utilities.utils import AccountType


class AccountService:
    def __init__(self, user_repo: UserRepo):
        self._user_repo = user_repo
        # self.accounts = []

    def open_account(self, user_id, account_type, currency):
        # Checking account's type
        if account_type not in AccountType:
            # return False
            print('Error with accounts')

        account_id = str(uuid.uuid4())

        account = Account(
            account_id,
            user_id,
            account_type,
            Decimal('0.00'),
            currency,
            datetime.fromisoformat(datetime.now().isoformat(timespec='seconds')),
            []
        )

        # self.accounts.append(account)
        return account
