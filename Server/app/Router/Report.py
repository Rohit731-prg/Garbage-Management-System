from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.Config.ConnectDB import get_db
from app.Model.Report import ReportModel
from app.Service.CloudinaryService import upload_report_image
from app.Service.Report import submitReport, getReportsByUserID, getAllReportsByState
from app.Middleware.jwt import verify_jwt_token

router = APIRouter(
    prefix="/api/v1/reports",
)

@router.post("/create")
async def create_report(
    report_image: UploadFile = File(...),
    report_description: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    country: str = Form(...),
    state: str = Form(...),
    district: str = Form(...),
    city: str = Form(...),
    street: str = Form(...),

    db: Session = Depends(get_db),
    user = Depends(verify_jwt_token)
):
    # Upload image to Cloudinary
    image_url = upload_report_image(report_image)

    # Construct Pydantic model
    data = ReportModel(
        user_id=user.id,
        report_image=image_url,
        report_description=report_description,
        latitude=latitude,
        longitude=longitude,
        country=country,
        state=state,
        district=district,
        city=city,
        street=street
    )

    return await submitReport(db, data)