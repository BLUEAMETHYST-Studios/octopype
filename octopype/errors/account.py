class AccountError(Exception): ...
class InvalidToken(AccountError): ...
class AuthenticationError(AccountError): ...