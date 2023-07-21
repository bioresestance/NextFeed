"""
@package backend.server
@brief This package contains the web server and all related code.
"""


from flask import Flask
from flask_restx import Api
from flask_cors import CORS


app = Flask(__name__)
cors = CORS()
restApi = Api()


def get_web_server() -> Flask:

    """
        @brief This function creates the web server and configures it.
        @return The web server.
    """

    # Register the different blueprints.
    # from server.routes import api_routes

    # # Appends API routes with /api/v1
    # app.register_blueprint(api_routes, url_prefix="/api/v1/")

    restApi.init_app(app, doc=True)
    cors.init_app(app)

    return app
