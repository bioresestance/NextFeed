import threading
import logging
from time import sleep
import mongoengine
import schedule
from .tasks.user_feeds import init_user_scheduling

logger = logging.getLogger("Nextfeed App")

def app_main(stop_event: threading.Event):
    """ This is the main function of the Nextfeed backend application.
    
        It is responsible for various backend tasks, such as parsing feeds.
        
        This method is designed to be ran in a separate thread.
    """
    
    logger.info("Starting Nextfeed backend application. Waiting for database connection.")
    mongoengine.connect( db="NextFeed", Username="admin", Password="admin" )
    logger.info("Database connection established. Starting backend tasks.")
    
    
    user_feed_scheduler = schedule.Scheduler()
    
    init_user_scheduling(user_feed_scheduler)
    
    # Infinite loop to keep the thread alive.
    while not stop_event.is_set():
        
        user_feed_scheduler.run_pending()
        
        next_run_time = user_feed_scheduler.idle_seconds
        
        # Negative time means the sheduler has a job to run.
        if next_run_time is float and next_run_time < 0:
            continue
        # Wait the specified time before running the next job.
        if next_run_time is float:
            sleep(next_run_time)
        # No jobs to run, so wait 1 second.
        else:
            sleep(1)