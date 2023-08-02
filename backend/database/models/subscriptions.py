import datetime

from mongoengine import StringField, BooleanField, DateTimeField, EmbeddedDocument, URLField, ListField

class Subscription(EmbeddedDocument):
    url = URLField(required=True)
    added_at = DateTimeField(required=True, default=datetime.datetime.utcnow)
    enabled = BooleanField(required=True, default=True)
    user_tags = ListField(StringField())
    user_title = StringField(required=True)