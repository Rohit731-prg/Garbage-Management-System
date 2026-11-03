import cloudinary.uploader
import app.Config.Cloudinary

from fastapi import UploadFile, HTTPException


def upload_report_image(file: UploadFile) -> str:
    try:
        result = cloudinary.uploader.upload(
            file.file,
            folder="garbage_reports",
            resource_type="image"
        )

        return result["secure_url"]

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail="Failed to upload report image"
        ) from e