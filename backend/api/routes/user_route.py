from typing import Annotated
from logging import getLogger
from fastapi import APIRouter, HTTPException, status, Depends
from mongoengine.errors import NotUniqueError
from backend.api.models.users import GetUserResponse, NewUserRequest, NewUserResponse
from backend.database.models.users import User
from backend.api.security import get_current_user as current_user

router = APIRouter( prefix="/user", tags=["user"] )
logger = getLogger("UserRoute")


@router.get("/", description="Get the currently logged in user")
def get_current_user(user: Annotated[User, Depends(current_user)]) -> GetUserResponse:
    """ Gets the currently logged in user.

    Args:
        user : The current user.

    Raises:
        HTTPException: If the user is not found.

    Returns:
        GetUserResponse: The user.
    """
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not logged in.")
    
    return GetUserResponse.from_database_user(user)




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
        logger.warning(f"Exception occurred while trying to find user with ID {user_id}: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.") from e
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.")


    return GetUserResponse.from_database_user(user)

@router.get("/username/{username}")
def get_user_by_username(username: str) -> GetUserResponse:
    """ Get a user by their username.

    Args:
        username (str): The username of the user to get.

    Raises:
        HTTPException: If the username is invalid or the user is not found.

    Returns:
        GetUserResponse: The user.
    """
    if (username is None) or (username == ""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username, please check and try again.")
    
    try:
        user:User = User.objects(username=username).first()
    except Exception as e:
        logger.warning(f"Exception occurred while trying to find user with username {username}: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.") from e
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, please check spelling and try again.")


    return GetUserResponse.from_database_user(user)

@router.post("/new", response_model=NewUserResponse, status_code=status.HTTP_201_CREATED, response_description="User created successfully.", description="Creates a new user.")
def create_user(new_user_request: NewUserRequest) -> NewUserResponse:
    print(new_user_request)
    try:
        new_user = User( username=new_user_request.username,
                        email=new_user_request.email,
                        first_name=new_user_request.first_name,
                        last_name=new_user_request.last_name )
        new_user.hash_password(new_user_request.password)
        new_user.save()
    except NotUniqueError as e:
        logger.warning(f"Exception {type(e)} occurred while trying to create new user: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists, please change either username or email") from e
    except Exception as e:
        logger.warning(f"Exception {type(e)} occurred while trying to create new user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating user, please try again.") from e
    
    return NewUserResponse(user_id=str(new_user.id))
                        

