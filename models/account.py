from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Account:
    account_id: int
    user_id: int
    account_type: str
    balance: Decimal
    currency: str
    created_at: datetime
    transactions: list