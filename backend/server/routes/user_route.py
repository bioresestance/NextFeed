from logging import getLogger
from fastapi import APIRouter, HTTPException, status
from backend.database.models.users import User
from backend.server.models.users import GetUserResponse

router = APIRouter( prefix="/user", tags=["user"] )
logger = getLogger("UserRoute")


@router.get("/id/{user_id}")
def get_user_by_id(user_id: str) -> GetUserResponse:
    """
        @brief This function returns a user by ID.
        @param user_id The ID of the user.
        @return The user.
    """
    if (user_id is None) or (user_id == ""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username, please check and try again.")
    try:
        user:User = User.objects(id=user_id).first()
    except Exception as e:
        logger.warning(f"Exception occurred while trying to find user with ID {user_id}: {e}") #pylint: disable=logging-fstring-interpolation
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.") from e
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.")


    return GetUserResponse.from_database_user(user)

@router.get("/username/{username}")
def get_user_by_username(username: str) -> GetUserResponse:
    if (username is None) or (username == ""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username, please check and try again.")
    
    try:
        user:User = User.objects(username=username).first()
    except Exception as e:
        logger.warning(f"Exception occurred while trying to find user with username {username}: {e}") #pylint: disable=logging-fstring-interpolation
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.") from e
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.")


    return GetUserResponse.from_database_user(user)