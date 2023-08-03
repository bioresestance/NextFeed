import logging
from mongoengine import connect, disconnect

from .models.users import User, AdminUser
from .models.subscriptions import Subscription


logger = logging.getLogger("Database")

data_base_connection = None


def initialize():
    """ Initializes the database connection.
    """
    global data_base_connection
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
        
        sub1 = Subscription(url="https://hackaday.com/blog/feed/", user_tags=["news", "tech"], user_title="Hackaday")
        sub2 = Subscription(url="https://themonsterunderthebed.net/feed/", user_tags=["comics"], user_title="The Monster Under the Bed")
        sub3 = Subscription(url="https://feeds.simplecast.com/54nAGcIl", user_tags=["news"], user_title="The Daily")
        admin.subscriptions = [sub1, sub2, sub3]     
        admin.save()
        

def uninitialize():
    """ Closes the database connection.
    """
    logger.info("Closing the MongoDB database connection.")
    disconnect()