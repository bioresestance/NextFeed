from datetime import datetime
from pydantic import BaseModel




class AccessToken(BaseModel):
    """
        Model to describe the Access token JSON to return via API.
    """
    access_token: str
    token_type: str = "bearer"
    
    
class AccessTokenContents(BaseModel):
    """
        Model to describe the unencoded JWT token contents
    """
    sub: str | None = None
    exp: datetime