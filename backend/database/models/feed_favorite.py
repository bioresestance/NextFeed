import datetime
from mongoengine import StringField, DateTimeField, EmbeddedDocument, ReferenceField

class Favorite(EmbeddedDocument):
    """Database model to describe a feed item that a user has favorited.
    """
    feed_item = ReferenceField('FeedItem', required=True)
    added_date = DateTimeField(required=True, default=datetime.datetime.utcnow)
    user_notes = StringField()