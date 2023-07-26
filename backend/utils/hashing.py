from passlib.context import CryptContext


class Hasher():
    __pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return Hasher.__pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return Hasher.__pwd_context.hash(password)