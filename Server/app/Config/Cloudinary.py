import cloudinary
from app.Config.Config import setting

cloudinary.config(
    api_key=setting.CLOUDINARY_API_KEY,
    api_secret=setting.CLOUDINARY_API_SECRET,
    cloud_name=setting.CLOUDINARY_CLOUD_NAME,
    secure=True
)