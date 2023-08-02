import pytest
import mongomock
from mongoengine import connect, disconnect



@pytest.fixture(scope="function")
def mock_database_func_fixture():
    """Connect to a mock database for testing.
    This fixture is scoped to the function, so it will reset the connection for each test.
    
    """
    connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
    yield
    disconnect('mongoenginetest')
    
    
@pytest.fixture(scope="class")
def mock_database_class_fixture():
    """Connect to a mock database for testing.
    
    This fixture is scoped to the class, so it will only connect once for all tests in the class.

    """
    connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
    yield 
    disconnect('mongoenginetest')

