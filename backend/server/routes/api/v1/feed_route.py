from flask import Blueprint
from flask_restx import Resource, Api


feeds_route = Blueprint("Feeds", __name__)

api = Api(feeds_route)


@api.route("/")
class InvoiceRoute(Resource):
    def get(self):
        return "Hello World"