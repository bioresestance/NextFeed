"""
@package backend.server
@brief This package contains the web server and all related code.
"""

from fastapi import FastAPI, APIRouter
from pymongo import MongoClient
from dotenv import dotenv_values
from fastapi.middleware.cors import CORSMiddleware
from server.routes import feed_route, user_route

app = FastAPI()
config = dotenv_values(".env")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    app.mongodb_client = MongoClient(config["MONGO_URI"])
    app.database = app.mongodb_client["NextFeed"]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_event():
    app.mongodb_client.close()
    print("Disconnected from the MongoDB database!")


def get_web_server() -> FastAPI:
    """
        @brief This function creates the web server and configures it.
        @return The web server.
    """
    # pylint: disable=import-outside-toplevel
    
    
    v1_router = APIRouter( prefix="/api/v1", tags=["v1"] )
    
    v1_router.include_router(feed_route.router)
    v1_router.include_router(user_route.router)
    
    app.include_router(v1_router)
    

    return app
