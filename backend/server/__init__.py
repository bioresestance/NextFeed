"""
@package backend.server
@brief This package contains the web server and all related code.
"""


from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_pymongo import PyMongo



app = Flask(__name__)
cors = CORS(app)
restApi = Api(app)
# pymongo = PyMongo(app)


def get_web_server() -> Flask:
    """
        @brief This function creates the web server and configures it.
        @return The web server.
    """
    # pylint: disable=import-outside-toplevel
    from server.routes.feed_route import feeds_route

    # Register the different blueprints.

    # Appends API routes with /api/v1
    app.register_blueprint(feeds_route, url_prefix="/api/v1/feeds/")

    # restApi.init_app(app)
    # cors.init_app(app)
    # # pymongo.init_app(app)

    return app
