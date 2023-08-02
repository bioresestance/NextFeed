import pytest
import mongomock
from mongoengine import connect, disconnect



@pytest.fixture(scope="function")
def mock_database_fixture():
    connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
    yield "db_connection"
    disconnect()

