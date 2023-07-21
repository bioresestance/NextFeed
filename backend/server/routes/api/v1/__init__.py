"""
 This module is the entry point for the backend server API routes.
"""

from flask import Blueprint

from .feed_route import feeds_route


# Top Level route for Rest Api
api_routes = Blueprint("api_v1_routes", __name__)

# Nest all individual routes under the api_route.
api_routes.register_blueprint(feeds_route, url_prefix="/feeds")
