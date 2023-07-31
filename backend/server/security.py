from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from backend.database.models.users import User
from backend.database.models.subscriptions import Subscription

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def get_current_user(user_token: Annotated[str, Depends(oauth2_scheme)]) -> User | None:
    """Dependency to get the current user from the database based on the token.
    
       If the token is invalid (stale or incorrect), this will return None.

    Args:
        user_token (Annotated[str, Depends): Token to get the user from.

    Returns:
        User | None: Either a logged in user or None.
    """
    
    return User.objects(username=user_token).first()


def get_user_subs(user: Annotated[User, Depends(get_current_user)]) -> list[Subscription]:
    """Dependency to get the current user's subs from the database based on the token.
    
       If the token is invalid (stale or incorrect), this will return None.

    Args:
        user_token (Annotated[str, Depends): Token to get the user from.

    Returns:
        User | None: Either a logged in user or None.
    """
    return user.subscriptions