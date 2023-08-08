import threading
import types
from datetime import datetime
from schedule import Scheduler
from backend.database.models.users import User
from backend.database.models.feed_source import FeedSource
from backend.database.models.feed_item import FeedItem
from ..feed_parser import FeedParser




def feed_parser_runner(job: types.FunctionType, user:User):
    """Wrapper function to run the feed parser in a separate thread.
    """
    thread = threading.Thread(target=job, args=(user,))
    thread.start()



def parse_user_feeds(user: User):
    """Parses all the feeds of a user and stores the results in the database.
    """
    user_subscriptions: list[FeedSource] = user.subscriptions
    for sub in user_subscriptions:
        
        try:
            parser = FeedParser(sub.source_url)
        except Exception:
            continue
        feed = parser.get_feed()
            
        for item in feed.items:
            # If the feed item already exists, skip it.    
            if FeedItem.objects(title=item.title, feed_source=sub).first() is not None:
                continue
            
            # Item doesnt exist, create it.
            feed_item = FeedItem(title=item.title, 
                                 link=item.link, 
                                 feed_source=sub, 
                                 contents=item.content,
                                 description=item.description,
                                 published_at= datetime.strptime(str(item.published_at), "%a, %d %b %Y %H:%M:%S %z"),
                                 published_by=item.published_by,
                                 thumbnail_url=item.thumbnail_url or "https://via.placeholder.com/150",
                                )
            feed_item.save()
            








def init_user_scheduling(scheduler: Scheduler):
    
    for user in User.objects(is_active=True):
        # scheduler.every(user.feed_update_interval).seconds.do(feed_parser_runner, job=parse_user_feeds, user=user)
        scheduler.every(10).seconds.do(feed_parser_runner, job=parse_user_feeds, user=user)