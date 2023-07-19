from fastapi import APIRouter, HTTPException

router = APIRouter( prefix="/user", tags=["user"] )


@router.get("/{user_id}")
def read_user(user_id: int):
    """
        @brief This function returns a user.
        @param user_id The ID of the user.
        @return The user.
    """
    if user_id == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": "Bob", "age": 42, "is_active": True, "items": ["foo", "bar", "baz"]}
