import datetime
from mongoengine import Document, StringField, BooleanField, DateTimeField, URLField, ReferenceField


class FeedSource(Document):
    """
    Database model to describe a feed source document in mongoDB.
    A feed source is a source of FeedItems, such as a blog or news site.
    Each entry is a parsed feed from a URL.
    """
    title = StringField(required=True)
    url = URLField(required=True)
    subscribed_user = ReferenceField('User', required=True)
    created = DateTimeField(required=True, default=datetime.datetime.utcnow)
    enabled = BooleanField(required=True, default=True)
    
   