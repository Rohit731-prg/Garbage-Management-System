from jose import jwt
from fastapi import Request, Depends, HTTPException

from app.Config.Config import setting
from app.Config.ConnectDB import get_db
from app.DB.User import User

from sqlalchemy.orm.session import Session

SECRET_KEY = setting.SECRET_KEY

async def verify_jwt_token(
    req: Request,
    db: Session = Depends(get_db)
) -> dict:
    try:
        cookie = req.cookies.get("access_token")
        if not cookie:
            raise HTTPException(status_code=400, detail="No cookie found")
            
        payload = jwt.decode(cookie, setting.SECRET_KEY, algorithms=[setting.ALGORITHM])
        user_id, user_email = payload.get("user_id"), payload.get("email")

        user = db.query(User).filter(User.id == user_id, User.email == user_email).first()
        if not user:
            raise HTTPException(status_code=400, detail="User not found")

        return user
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    