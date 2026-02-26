from dataclasses import dataclass
from datetime import datetime

from central_bank_of_yemen.models.account import Account


@dataclass(frozen=True)
class User:
    user_id: str
    username: str
    legal_name: str
    date_of_birth: datetime
    gender: str
    address: str
    phone_number: str
    email: str
    password_hash: str
    accounts: list[Account]
    is_active: bool = True
