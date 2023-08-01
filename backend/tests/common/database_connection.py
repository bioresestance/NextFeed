import pytest
import mongomock
from mongoengine import connect, disconnect



@pytest.fixture(scope="function")
def db_connection():
    connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
    yield "db_connection"
    disconnect()

