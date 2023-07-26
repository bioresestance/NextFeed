from pydantic import BaseModel, EmailStr
from backend.database.models.users import User, AdminUser

class NewUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str # Raw password, will be hashed before storing in DB
    first_name: str
    last_name: str


class NewUserResponse(BaseModel):
    user_id: str | None = None # Used to return user ID if user creation succeeded
    message: str | None = None # Used to return error message if user creation failed


class GetUserResponse(BaseModel):
    id: str 
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    created_at: str
    zip_code: str
    country: str
    profile_picture: str = ""

    @classmethod
    def from_database_user(cls, user: User) -> "GetUserResponse":
        
        return cls( id=str(user.id),
                    username=user.username,
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    is_active=user.is_active,
                    created_at=str(user.created_at),
                    zip_code=user.zip_code,
                    country=user.country,
                    profile_picture=user.profile_picture )