import threading
import types
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
    user_subscriptions: list[Subscription] = user.subscriptions
    
    for sub in user_subscriptions:
        print(f"Updating feed: {sub.user_title}")
    
    


def init_user_scheduling(scheduler: Scheduler):
    
    for user in User.objects(is_active=True):
        scheduler.every(user.feed_update_interval).seconds.do(feed_parser_runner, job=parse_user_feeds, user=user)