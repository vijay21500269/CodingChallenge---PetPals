class AdoptionException(Exception):
    def __init__(self, message="Adoption failed due to invalid pet details or availability."):
        super().__init__(message)
