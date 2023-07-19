from fastapi import APIRouter, HTTPException

router = APIRouter( prefix="/feeds", tags=["feeds"] )


@router.get("/")
def read_feeds():
    """
        @brief This function returns all feeds.
        @return A list of all feeds.
    """
    return {"message": "Hello World"}

@router.get("/{feed_id}")
def read_feed(feed_id: int):
    """
        @brief This function returns a feed.
        @param feed_id The ID of the feed.
        @return The feed.
    """
    if feed_id == 0:
        raise HTTPException(status_code=404, detail="Feed not found")
    return {"message": "Hello World"}