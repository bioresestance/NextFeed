"""
    @brief ...
"""
from dataclasses import dataclass
import feedparser


@dataclass
class FeedItem:
    """
        Dataclass to hold the data from a feed item.
    """    
    title: str = ""
    link: str = ""
    description: str = ""
    published_by: str = ""
    published_at: str = ""
    thumbnail_url: str = ""
    content:  str = ""

@dataclass
class Feed:
    """
    Dataclass to hold the data from a feed.
    """
    title: str = ""
    link: str = ""
    description: str = ""
    last_updated: str = ""
    thumbnail_url:str = ""
    tags = None
    items: list[FeedItem] = None



class FeedParser:

    def __init__(self, feed_url: str):
        self._feed_url = feed_url

        # 
        try:
            self._parser = feedparser.parse(self._feed_url)
        except Exception as e:
            print(f"Error parsing feed: {e}")
            raise e
        
        if self._parser.bozo:
            print(f"Feed '{self._feed_url}' is invalid.")
            raise ValueError(f"Feed '{self._feed_url}' is invalid.")

        self._load()


    def _load(self):
        """
            Loads in the feed to the local data structures.
        """

        new_feed = Feed()
        new_feed.title = self._parser.feed.get("title", "No Title Provided")
        new_feed.link = self._parser.feed.get("link", "No Link Provided")
        new_feed.description = self._parser.feed.get("description", "No Description Provided")
        new_feed.last_updated = self._parser.feed.get("published", "No Last Publish date Provided")
        new_feed.thumbnail_url = self._parser.feed.get("image", "No Thumbnail Provided")
        new_feed.tags = self._parser.feed.get("categories", "No Tags Provided")
        new_feed.items = []

        for entry in self._parser.entries:

            new_item = FeedItem()
            new_item.title = entry.get("title", "No Title Provided")
            new_item.link = entry.get("link", "No Link Provided")
            new_item.description = entry.get("description", "No Description Provided")
            new_item.published_by = entry.get("author", "No Author Provided")
            new_item.published_at = entry.get("published", "No Publish date Provided")
            thumbnail = entry.get("media_thumbnail", "")
            
            if isinstance(thumbnail, str):
                new_item.thumbnail_url = thumbnail
            elif isinstance(thumbnail, list):
                if ("url" in thumbnail[0]) and (thumbnail[0]["url"] is str):
                    new_item.thumbnail_url = thumbnail[0]["url"]
            else:
                new_item.thumbnail_url = ""
            content = entry.get("content", "No Content Provided")
            
            if isinstance(content, str):
                new_item.content = content
            elif isinstance(content, list):
                if len(content) > 0 and isinstance(content[0], dict):
                    if ("value" in content[0]) and isinstance(content[0]["value"], str):
                        new_item.content = content[0]["value"]               
            else:
                new_item.content = "No Content Provided"


            new_feed.items.append(new_item)

        self._feed = new_feed

    def get_feed(self) -> Feed:
        return self._feed


    def __str__(self) -> str:
        return str(self._feed)