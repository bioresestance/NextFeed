from flask import Blueprint
from flask_restx import Resource, Api
from feed_parser import feed

feeds_route = Blueprint("feeds_route", __name__)

api = Api(feeds_route)


@api.route("/test")
class TestRoute(Resource):
    def get(self):
        return feed