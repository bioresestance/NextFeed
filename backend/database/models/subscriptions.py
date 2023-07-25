import datetime

from mongoengine import StringField, BooleanField, DateTimeField, EmbeddedDocument, URLField, ListField

class Subscription(EmbeddedDocument):
    url = URLField(required=True, unique=True)
    added_at = DateTimeField(required=True, default=datetime.datetime.utcnow)
    user_tags = ListField(StringField())
    enabled = BooleanField(default=True)