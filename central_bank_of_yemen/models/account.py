from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from central_bank_of_yemen.models.transaction import Transaction
from central_bank_of_yemen.utilities.utils import AccountType


@dataclass
class Account:
    account_id: str
    user_id: str
    account_type: AccountType
    balance: Decimal
    currency: str
    created_at: datetime
    transactions: list[Transaction]
