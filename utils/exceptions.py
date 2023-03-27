class TokenNotFoundException(Exception):
    def __init__(self, message: str = "Token not found in environment variables!"):
        super().__init__(message)
