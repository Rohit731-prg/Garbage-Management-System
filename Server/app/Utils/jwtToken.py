from jose import jwt
from app.Config.Config import setting

def jwt_token(data):
    return jwt.encode(data, setting.SECRET_KEY, algorithm=setting.ALGORITHM)