class AppError(Exception):
    pass


class AuthenticationError(AppError):
    pass


class AuthorizationError(AppError):
    pass


class UserAlreadyExistsError(AppError):
    pass


class InsufficientFundsError(AppError):
    pass


class AccountNotFoundError(AppError):
    pass
