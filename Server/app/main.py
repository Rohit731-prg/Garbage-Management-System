from fastapi import FastAPI

from app.Router.User import router as user_router
from app.Router.Report import router as report_router

from app.Config.ConnectDB import engine, base
from fastapi.middleware.cors import CORSMiddleware
from app.Config.Config import setting

app = FastAPI()

base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "https://spentsmart-client.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(report_router)