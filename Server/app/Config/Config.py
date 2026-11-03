from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    # Database settings
    DATABASE_PASSWORD: str = ""

    # Security settings
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    GEMINI_API_KEY: str = "your-gemini-key"
    DATABASE_URL: str = ""
    CLOUDINARY_CLOUD_NAME=""
    CLOUDINARY_API_KEY=""
    CLOUDINARY_API_SECRET=""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

setting = Setting()