class NullReferenceException(Exception):
    def __init__(self, message="Pet information is missing."):
        super().__init__(message)
