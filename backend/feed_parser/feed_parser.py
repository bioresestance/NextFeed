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
    base_link: str = ""
    description: str = ""
    last_updated: str = ""
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
        new_feed.base_link = self._parser.feed.get("link", "No Link Provided")
        new_feed.description = self._parser.feed.get("description", "No Description Provided")
        new_feed.last_updated = self._parser.feed.get("published", "No Last Publish date Provided")
        new_feed.items = []

        for entry in self._parser.entries:

            new_item = FeedItem()
            new_item.title = entry.get("title", "No Title Provided")
            new_item.link = entry.get("link", "No Link Provided")
            new_item.description = entry.get("description", "No Description Provided")
            new_item.published_by = entry.get("author", "No Author Provided")
            new_item.published_at = entry.get("published", "No Publish date Provided")
            new_item.thumbnail_url = entry.get("image", "No Thumbnail Provided")
            new_item.content = entry.get("content", "No Content Provided")


            new_feed.items.append(new_item)

        self._feed = new_feed


    def __str__(self) -> str:
        return str(self._feed)