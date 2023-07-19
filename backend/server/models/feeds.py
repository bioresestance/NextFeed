from pydantic import BaseModel




class Feed(BaseModel):
    """
        @brief This class represents a feed.
    """
    title: str
    link: str
    description: str
    
    
class FeedItemSummary(BaseModel):
    title: str
    link: str
    description: str
    published: str
    
class FeedItem(FeedItemSummary):
    article: str
    
class FeedItemInDB(FeedItem):
    feed_id: int
    feed_item_id: int
    