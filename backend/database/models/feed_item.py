import datetime

from mongoengine import Document, StringField, DateTimeField, URLField, ReferenceField

class FeedItem(Document):
    feed_source = ReferenceField('FeedSource', required=True)
    title: str = StringField(required=True)
    link: str = URLField(required=True)
    description: str = StringField()
    published_by: str = StringField()
    published_at: datetime.datetime = DateTimeField()
    thumbnail_url: str = URLField()
    contents: str = StringField(required=True)