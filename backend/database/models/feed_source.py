import datetime
from mongoengine import Document, StringField, BooleanField, DateTimeField, URLField, ReferenceField, ListField


class FeedSource(Document):
    """
    Database model to describe a feed source document in mongoDB.
    A feed source is a source of FeedItems, such as a blog or news site.
    Each entry is a parsed feed from a URL.
    """
    source_title = StringField(required=True)
    source_url = URLField(required=True)
    source_description = StringField()
    thumbnail_url = URLField()
    subscribed_user = ReferenceField('User', required=True)
    created = DateTimeField(required=True, default=datetime.datetime.utcnow)
    enabled = BooleanField(required=True, default=True)
    favorite = BooleanField(required=True, default=False)
    source_tags = ListField(StringField())
    user_title = StringField(default="")
    user_tags = ListField(StringField())
    
    meta = {'collection': 'feed_sources', 
            "indexes": [
            "subscribed_user",
            "source_url",
            ]
            }
    
   