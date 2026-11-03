from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm.session import Session

from app.Model.User import UserModel, UserLoginModel
from app.Config.ConnectDB import get_db

from app.Service.User import createUser, loginUser

router = APIRouter(
    prefix="/api/v1/user",
)

@router.post("/signup")
async def signUpUser(
    user: UserModel,
    db: Session = Depends(get_db)
):
    return await createUser(db, user)


@router.post("/login")
async def loginUserRoute(
    user: UserLoginModel,
    db: Session = Depends(get_db)
):
    return await loginUser(db, user, res=Response())