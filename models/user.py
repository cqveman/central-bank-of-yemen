from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    user_id: int
    username: str
    legal_name: str
    date_of_birth: datetime
    gender: str
    address: str
    phone_number: str
    email: str
    password_hash: str
    accounts: list
    is_active: bool = True