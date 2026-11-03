from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.Config.Config import setting

url = setting.DATABASE_URL

engine = create_engine(
    url,
    pool_pre_ping=True,
    pool_recycle=300
)

sessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()