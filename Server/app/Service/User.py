from sqlalchemy.orm.session import Session
from typing import cast

from fastapi import HTTPException, Response

from app.Model.User import UserModel, UserLoginModel
from app.DB.User import User
from app.Utils.hashedPassword import hash_Password, compare_Password
from app.Utils.jwtToken import jwt_token

async def createUser(db: Session, data: UserModel):
    try:
        is_exist = db.query(User).filter(User.email == data.email).first()
        if is_exist:
            raise HTTPException(status_code=400, detail="Email already registered")

        user_hashedPassword = hash_Password(data.password)
        new_user = User(
            username = data.username,
            email = data.email,
            password = user_hashedPassword,
            creadit_point = 0
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "message": "User sign up success"
        }
    except HTTPException as e:
        print(str(e ))
        raise
    except Exception as e:
        print(str(e ))
        raise HTTPException(status_code=500, detail=str(e))


async def loginUser(db: Session, data: UserLoginModel, res: Response):
    try:
        user = db.query(User).filter(User.email == data.email).first()
        if not user:
            return HTTPException(status_code=400, detail="Email not registered")

        is_password_match = compare_Password(data.password, cast(str, user.password))
        if not is_password_match:
            return HTTPException(status_code=400, detail="password not match")

        token = jwt_token({"user_id": user.id, "email": user.email})
        res.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=True,
            samesite="none"
        )

        return {
            "message": "User login success",
            "user": user
        }
    except HTTPException as e:
        print(str(e ))
        raise
    except Exception as e:
        print(str(e ))
        raise HTTPException(status_code=500, detail=str(e))