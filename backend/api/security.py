from datetime import timedelta, datetime
from typing import Annotated

from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from backend.database.models.users import User
from backend.database.models.subscriptions import Subscription
from backend.api.models.security import AccessToken, AccessTokenContents

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

# TODO: Use another storage method, this is only for dev uses for now.
JWT_SECRET = "7a622820781eff8983daebd5552995d510c674d870b5e02a332360e0e68ed985"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_current_user(user_token: Annotated[str, Depends(oauth2_scheme)]) -> User | None:
    """Dependency to get the current user from the database based on the token.
    
       If the token is invalid (stale or incorrect), this will return None.

    Args:
        user_token (Annotated[str, Depends): Token to get the user from.

    Returns:
        User | None: Either a logged in user or None.
    """
    
    return verify_json_web_token(user_token)


def get_user_subs(user: Annotated[User, Depends(get_current_user)]) -> list[Subscription]:
    """Dependency to get the current user's subs from the database based on the token.
    
       If the token is invalid (stale or incorrect), this will return None.

    Args:
        user_token (Annotated[str, Depends): Token to get the user from.

    Returns:
        User | None: Either a logged in user or None.
    """
    return user.subscriptions


def create_json_web_token(username:str, expires_time: timedelta | None = None) -> AccessToken:
    
    """Generates a JSON Web Token thats been encoded with needed data to verify authentication.

    Returns:
        AccessToken: Model containing the generated bearer token.
    """
    
    if expires_time:
        expire = datetime.utcnow() + expires_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        
    # Attempt to encode the contents into the token.
    encoded_jwt = jwt.encode(dict(AccessTokenContents(sub=username, exp=expire)), JWT_SECRET, algorithm=ALGORITHM)
    
    # Return the Access Token model, ready to be returned as is.
    return AccessToken(access_token=encoded_jwt)


def verify_json_web_token(token) -> User | None:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Decode the token.
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        token_contents:AccessTokenContents = AccessTokenContents(**payload)
    except JWTError as e:
        raise credentials_exception from e
    
    # Validate the username and check if the token has expired
    if (token_contents.username is None) or (token_contents.exp is None):
        raise credentials_exception
    
    if datetime.utcnow() > token_contents.exp:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token is expired, please log in again",
        headers={"WWW-Authenticate": "Bearer"},
        )
    
    # It has passed all checks, return the user from the database.
    user = User.objects(username=token_contents.username).first()
    if user is None:
        raise credentials_exception
    return user