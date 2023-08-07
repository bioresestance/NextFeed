import logging
from mongoengine import connect, disconnect

from .models.users import User, AdminUser
from .models.feed_source import FeedSource


logger = logging.getLogger("Database")



def initialize():
    """ Initializes the database connection.
    """
    connect( db="NextFeed", Username="admin", Password="admin" )
    logger.info("Connected to the MongoDB database!")


# The following is just for testing purposes, and should be removed later.
    # Create the admin user if it doesn't exist
    admin = User.objects(username="admin").first()
    
    if admin is None:
        admin = AdminUser(
            username="admin",
            email="admin@ajb-tech.ca",
            first_name="Admin",
            last_name="User",
            zip_code="N/A",
            country="N/A",
            profile_picture=""
        )
        AdminUser.hash_password(admin, password="admin1234")
        admin.save()
        
        
        sub1 = FeedSource(source_title="Hackaday", source_url="https://hackaday.com/blog/feed/", user_tags=["news", "tech"], user_title="Hackaday", subscribed_user = admin)
        sub1.save()
        sub2 = FeedSource(source_title="The Monster Under the Bed", source_url="https://themonsterunderthebed.net/feed/", user_tags=["comics"], user_title="The Monster Under the Bed", subscribed_user = admin)
        sub2.save()
        sub3 = FeedSource(source_title="The Daily", source_url="https://feeds.simplecast.com/54nAGcIl", user_tags=["news"], user_title="The Daily", subscribed_user = admin)
        sub3.save()
        admin.subscriptions = [sub1, sub2, sub3]
        admin.save()
        
        

def uninitialize():
    """ Closes the database connection.
    """
    logger.info("Closing the MongoDB database connection.")
    disconnect()