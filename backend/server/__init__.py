"""
@package backend.server
@brief This package contains the web server and all related code.
"""

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from server.routes import feed_route, user_route
from logging import getLogger
from collections.abc import Callable

logger = getLogger("Server Main")
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

start_event: Callable | None = None
end_event: Callable | None = None


@app.on_event("startup")
def startup_event():
    """ Runs the startup event for the web server.
    """
    # If there is a startup event registered, run it.
    logger.info("Starting up server")
    if start_event is not None:
        try:
            start_event()
        except Exception as e:
            logger.error("Error in startup event: " + str(e))


@app.on_event("shutdown")
def shutdown_event():
    """ Runs the shutdown event for the web server.
    """
    # If there is a stop event registered, run it.
    logger.info("Shutting down server")
    if end_event is not None:
        try:
            end_event()
        except Exception as e:
            logger.error("Error in shutdown event: " + str(e))



def get_web_server(starting_event: Callable | None = None, stopping_event: Callable | None = None) -> FastAPI:
    """
        @brief This function creates the web server and configures it.
        @return The web server.
    """    
    global start_event
    global end_event
    v1_router = APIRouter( prefix="/api/v1", tags=["v1"] )
    
    v1_router.include_router(feed_route.router)
    v1_router.include_router(user_route.router)
    
    app.include_router(v1_router)
    
    start_event = starting_event
    end_event = stopping_event
    

    return app
