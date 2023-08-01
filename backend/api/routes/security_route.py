from typing import Annotated
from logging import getLogger
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import  OAuth2PasswordRequestForm
from backend.database.models.users import User
from backend.api.security import get_current_user as current_user, create_json_web_token
from backend.api.models.security import AccessToken

router = APIRouter( prefix="", tags=["security"] )
logger = getLogger("SecurityRoute")


@router.post("/login")        
async def login_user(login_form: Annotated[OAuth2PasswordRequestForm, Depends()]) -> AccessToken:
    
    try:
        user:User = User.objects(username=login_form.username).first()     
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while trying to log in.") from e
    
    # Ensure the user exists
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password.")
    
    # Validate the password
    if user.check_password(login_form.password) is False:
        logger.warning(f"User {user.username} attempted to log in with an incorrect password.")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password.")
    
    token = create_json_web_token(user.username)
    
    return token




@router.post("/logout")
def logout_user(user: Annotated[User, Depends(current_user)]):
    return "Hello"