from sqlalchemy import Column, Integer, String
from app.Config.ConnectDB import base

class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    creadit_point = Column(Integer, index=True)