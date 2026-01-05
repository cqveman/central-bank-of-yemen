from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Transaction:
    transaction_id: int
    account_id: int
    amount: Decimal
    currency: str
    transaction_type: str
    timestamp: datetime
    to_account_id: int | None = None