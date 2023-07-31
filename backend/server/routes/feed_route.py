from typing import Annotated
from fastapi import APIRouter, HTTPException, Request, Depends
from backend.database.models.users import User
from backend.server.models.feeds import Feed

router = APIRouter( prefix="/feeds", tags=["feeds"] )


@router.get("/", response_description="Returns all feeds")
def read_feeds():
    """
        @brief This function returns all feeds.
        @return A list of all feeds.
    """


@router.get("/{feed_id}", response_description="Returns a single feed")
def read_feed(feed_id: int, request: Request):
    """
        @brief This function returns a feed.
        @param feed_id The ID of the feed.
        @return The feed.
    """
    if feed_id >= len(request.app.data):
        raise HTTPException(status_code=404, detail="Feed not found")
    return request.app.data[feed_id]