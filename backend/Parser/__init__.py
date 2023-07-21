"""
Module to parse RSS feeds and return the data in a format that can be used by the frontend.
"""

import feedparser

FEED = None

with open("backend/feeds.txt", mode="r", encoding= "utf8") as f:
    FEED = f.read()

for line in FEED.split("\n"):
    print("-" * 80)
    print(f"Checking '{line}'")
    d = feedparser.parse(line)
    print(f"There are {len(d.entries)} entries in '{d.feed.title}'")

    for entry in d.entries:
        print(f"\tTitle: {entry.title}")
        print(f"\tSummary: {entry.summary}")
        print("\n")


print("-" * 80)
