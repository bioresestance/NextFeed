"""
Module to parse RSS feeds and return the data in a format that can be used by the frontend.
"""


from .feed_parser import FeedParser, Feed, FeedItem
import dataclasses
import pymongo


feed = []
feed_items = None
with open("feeds.txt", mode="r", encoding= "utf8") as f:
    feed_items = f.read()

for feed_item in feed_items.split("\n"):

    parser = FeedParser(feed_item)
    feed.append(dataclasses.asdict(parser._feed))
