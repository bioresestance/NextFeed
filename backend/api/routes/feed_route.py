from typing import Annotated
from fastapi import APIRouter, HTTPException, Request, Depends
from backend.database.models.users import User
from backend.database.models.feed_source import FeedSource
from backend.api.models.feed_source import Feed
from backend.api.security import get_current_user as current_user

router = APIRouter( prefix="/feeds", tags=["feeds"] )


@router.get("/", response_description="Returns all feeds")
def read_feeds(user: Annotated[User, Depends(current_user)])-> list[Feed]:
    """
        @brief This function returns all feeds.
        @return A list of all feeds.
    """
    
    user_feeds = FeedSource.objects(subscribed_user=user, enabled=True)
    
    feeds = []
    if user_feeds is not None:
        for feed in user_feeds:
            feeds.append(Feed.from_database_feed_source(feed))
            
    return feeds
    
    


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