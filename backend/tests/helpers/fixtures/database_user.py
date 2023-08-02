import pytest
from backend.database.models.users import User
from ..utils.user_database import create_new_test_user



@pytest.fixture(scope="function")
def create_new_user_func_fixture() -> User:
    user = create_new_test_user()
    yield user
    user.delete()
