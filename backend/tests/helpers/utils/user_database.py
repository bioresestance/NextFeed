from backend.database.models.users import User
from backend.database.models.subscriptions import Subscription


def create_new_test_user(username="test_user", 
                         email="test@test.ca", 
                         first_name="test", 
                         last_name="user", 
                         phone="1234567890",
                         address="123 test street", 
                         city="test city", 
                         state="test state", 
                         zip_code="12345", 
                         country="test country", 
                         profile_picture="test_picture",
                         password="test_password") -> User:
    
    """Create a new user for testing.
    The user is created, saved in the database, and returned.
    """
    
    new_user = User(username=username, email=email, 
                    first_name=first_name, 
                    last_name=last_name, 
                    phone=phone, 
                    address=address, 
                    city=city, 
                    state=state, 
                    zip_code=zip_code, 
                    country=country, 
                    profile_picture=profile_picture)
    
    User.hash_password(new_user, password)
    new_user.save()
    return new_user


def add_test_subscription_to_user(user: User, 
                                  url="http://lorem-rss.herokuapp.com/feed", 
                                  user_title="test_title", 
                                  user_tags=None) -> User:
    # Safer default for user_tags
    if user_tags is None:
        user_tags = ["test_tag"]
    
    sub = Subscription(url=url, user_title=user_title, user_tags=user_tags)
    user.subscriptions.append(sub)
    user.save()
