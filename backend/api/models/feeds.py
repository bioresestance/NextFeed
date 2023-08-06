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
    
    @staticmethod
    def from_database_feed_source(feed_source) -> 'Feed':
        """
            @brief This function converts a database feed source into a Feed object.
            @param feed_source The database feed source.
            @return The Feed.
        """
        return Feed(
            title=feed_source.title,
            link=feed_source.url,
            description="",
            thumbnail_url="",
            tags=[]
        )
    
    
class FeedItemSummary(BaseModel):
    title: str
    link: str
    description: str
    published: str
    
class FeedItem(FeedItemSummary):
    article: str
    
    