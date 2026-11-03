from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    username: str = Field(..., description="Name of the user")
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=8)


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=8)