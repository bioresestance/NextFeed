from pydantic import BaseModel




class Feed(BaseModel):
    """
        @brief This class represents a feed.
    """
    title: str
    link: str
    description: str
    thumbnail_url: str
    tags: list[str]
    
    
class FeedItemSummary(BaseModel):
    title: str
    link: str
    description: str
    published: str
    
class FeedItem(FeedItemSummary):
    article: str
    
    