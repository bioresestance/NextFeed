import datetime
from pydantic import BaseModel

from backend.database.models.feed_item import FeedItem as DatabaseFeedItem




class FeedItem(BaseModel):
    """Model for a Feed Item. Only contains the metadata.
    """
    
    feed_source: str
    title: str
    link: str
    description: str
    published_by: str
    published_at: datetime.datetime
    thumbnail_url: str
    
    def from_database_feed_item(self, feed_item: DatabaseFeedItem) -> 'FeedItem':
        
        return FeedItem(
            feed_source=feed_item.feed_source,
            title=feed_item.title,
            link=feed_item.link,
            description=feed_item.description,
            published_by=feed_item.published_by,
            published_at=feed_item.published_at,
            thumbnail_url=feed_item.thumbnail_url
        )
    
    
    
class FeedItemFull(FeedItem):
    """ A feed item with contents.
    """
    contents: str
    
    def from_database_feed_item(self, feed_item: DatabaseFeedItem) -> 'FeedItem':
        
        item = super().from_database_feed_item(feed_item)
        
        return FeedItemFull(
            **item,
            contents=feed_item.contents
        )
    