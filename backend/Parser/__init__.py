import feedparser

feed = None

with open("backend/feeds.txt", mode="r") as f:
    feed = f.read()

for line in feed.split("\n"):
    print("-" * 80)
    print(f"Checking '{line}'")
    d = feedparser.parse(line)
    print(f"There are {len(d.entries)} entries in '{d.feed.title}'")

    for entry in d.entries:
        print(f"\tTitle: {entry.title}")
        print(f"\tSummary: {entry.summary}")
        print("\n")


print("-" * 80)