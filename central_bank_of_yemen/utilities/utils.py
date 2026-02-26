from enum import StrEnum

from pwdlib import PasswordHash


class AccountType(StrEnum):
    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT = "credit"
    LOAN = "loan"
    BUSINESS = "business"


def hash_password(password):
    password_hash = PasswordHash.recommended().hash(password)
    return password_hash

def verify_password(password, password_hash):
    return PasswordHash.recommended().verify(password,password_hash)