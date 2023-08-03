import threading
import types
from datetime import datetime
from schedule import Scheduler
from backend.database.models.users import User
from backend.database.models.subscriptions import Subscription
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
    user_subscriptions: list[Subscription] = user.subscriptions
    for sub in user_subscriptions:
        parser = FeedParser(sub.url)
        feed = parser.get_feed()
        
        feed_source = FeedSource.objects(url=sub.url, subscribed_user=user).first()
    
        # If the feed source doesn't exist yet, create it.
        if feed_source is None:
            feed_source = FeedSource(title=feed.title, url=sub.url, subscribed_user=user )
            feed_source.save()
            
        for item in feed.items:
            # If the feed item already exists, skip it.    
            if FeedItem.objects(title=item.title, feed_source=feed_source).first() is not None:
                continue
            
            # Item doesnt exist, create it.
            feed_item = FeedItem(title=item.title, 
                                 link=item.link, 
                                 feed_source=feed_source, 
                                 contents=item.content,
                                 description=item.description,
                                 published_at= datetime.strptime(str(item.published_at), "%a, %d %b %Y %H:%M:%S %z"),
                                 published_by=item.published_by,
                                )
            feed_item.save()
            # print(item)
            








def init_user_scheduling(scheduler: Scheduler):
    
    for user in User.objects(is_active=True):
        # scheduler.every(user.feed_update_interval).seconds.do(feed_parser_runner, job=parse_user_feeds, user=user)
        scheduler.every(10).seconds.do(feed_parser_runner, job=parse_user_feeds, user=user)