import pytest
from backend.database.models.users import User
from helpers.database_connection import mock_database_fixture



@pytest.fixture(scope="function")
def create_user_fixture(mock_database_fixture):
    new_user = User(username="test_user", email="test@test.ca")
    User.hash_password(new_user, "test_password")
    new_user.save()


@pytest.mark.usefixtures("create_user_fixture")
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