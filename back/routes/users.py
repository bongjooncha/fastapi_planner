from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)
users = {}

@user_router.post("/signup", responses={
        409: {"description": "User with supplied username exists"}
    })
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= "User with supplied username exists"
        )
    users[data.email] = data
    return {
        "message": "User seccesfully registered"
    }


@user_router.post("/signin", 
    responses={
        403: {"description": "Wrong credential passed"},
        404: {"description": "User does not exist"}
    })
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return {
        "message": "User signed in successfully."
    }
