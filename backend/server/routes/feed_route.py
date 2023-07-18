from flask import Blueprint
from flask_restx import Resource, Api


feeds_route = Blueprint("feeds_route", __name__)

api = Api(feeds_route)


@api.route("/")
class TestRoute(Resource):
    def get(self):
        return {"Hello": "world"}