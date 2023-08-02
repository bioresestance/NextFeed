import pytest
from backend.database.models.users import User
from backend.database.models.subscriptions import Subscription
from backend.tests.helpers.fixtures.database_user import create_new_user_func_fixture
from backend.tests.helpers.fixtures.database_connection import mock_database_class_fixture
from backend.tests.helpers.utils.user_database import create_new_test_user, add_test_subscription_to_user



@pytest.mark.usefixtures("mock_database_class_fixture", "create_new_user_func_fixture")
class TestNewUser:
    
    def test_create_new_user(self):
        user = User.objects().first() 
        assert user is not None
            
    def test_user_has_username(self):
        user = User.objects().first()
        assert user.username == "test_user"
        
    def test_user_has_email(self):
        user = User.objects().first()
        assert user.email == "test@test.ca"

    def test_user_has_password(self):
        user = User.objects().first()
        assert user.password is not None
        
    def test_user_password_is_hashed(self):
        user = User.objects().first()
        assert User.check_password(user, "test_password") is True
        
    def test_user_password_is_not_plain_text(self):
        user = User.objects().first()
        assert user.password is not "test_password"
        
    def test_user_has_first_name(self):
        user = User.objects().first()
        assert user.first_name == "test"
        
    def test_user_has_last_name(self):
        user = User.objects().first()
        assert user.last_name == "user"
        
    def test_user_has_phone(self):
        user = User.objects().first()
        assert user.phone == "1234567890"
    
    def test_user_has_address(self):
        user = User.objects().first()
        assert user.address == "123 test street"
        
    def test_user_has_city(self):
        user = User.objects().first()
        assert user.city == "test city"
        
    
    def test_user_has_state(self):
        user = User.objects().first()
        assert user.state == "test state"
        
    def test_user_has_zip_code(self):
        user = User.objects().first()
        assert user.zip_code == "12345"
        
    def test_user_has_country(self):
        user = User.objects().first()
        assert user.country == "test country"
        
    def test_user_has_profile_picture(self):
        user = User.objects().first()
        assert user.profile_picture == "test_picture"
        
    def test_user_has_no_subscriptions(self):
        user = User.objects().first()
        assert len(user.subscriptions) == 0
        
    def test_duplicate_username_raises_error(self):
        with pytest.raises(Exception):
            create_new_test_user()
        

@pytest.mark.usefixtures("mock_database_class_fixture", "create_new_user_func_fixture")
class TestUserSubscriptions:
    
    def test_user_has_no_default_subscriptions(self):
        user = User.objects().first()
        assert len(user.subscriptions) == 0
    
    def test_user_can_add_subscription(self):
        user = User.objects().first()
        add_test_subscription_to_user(user)
        assert len(user.subscriptions) == 1
        
    def test_user_can_add_multiple_subscriptions(self):
        user = User.objects().first()
        add_test_subscription_to_user(user)
        add_test_subscription_to_user(user)
        assert len(user.subscriptions) == 2
    
