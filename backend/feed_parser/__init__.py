"""
Module to parse RSS feeds and return the data in a format that can be used by the frontend.
"""


from backend.feed_parser.feed_parser import FeedParser, Feed, FeedItem


if __name__ == "__main__":
    
    feed_items = None
    with open("backend/feeds.txt", mode="r", encoding= "utf8") as f:
        feed_items = f.read()

    for feed_item in feed_items.split("\n"):

        parser = FeedParser(feed_item)
        print(parser)
