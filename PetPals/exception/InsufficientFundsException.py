class InsufficientFundsException(Exception):
    def __init__(self, message="Donation must be at least $10."):
        super().__init__(message)
