import datetime
from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField, EmbeddedDocumentListField
from backend.utils.hashing import Hasher
from .subscriptions import Subscription

class User(Document):
    """
    User model for storing user related details in MongoDB
    """
    email = EmailField(required=True, unique=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    first_name = StringField()
    last_name = StringField()
    phone = StringField()
    address = StringField()
    city = StringField()
    state = StringField()
    zip_code = StringField()
    country = StringField()
    profile_picture = StringField()
    subscriptions = EmbeddedDocumentListField(Subscription)
    meta = {'collection': 'users', 
            "allow_inheritance": True,
            "indexes": [
                "email",
                "username",
            ],
            "auto_create_index ": True
            }
    

    def hash_password(self, password: str)-> None:
        """
        Hashes the user password.
        """
        self.password = Hasher.get_password_hash(password)


    def check_password(self, password: str) -> bool:
        """
        Checks the user password.
        """
        return Hasher.verify_password(password, self.password)


class AdminUser(User):
    """
    AdminUser model for storing admin user related details in MongoDB.
    Inherits from User, so stored in the same collection.
    """