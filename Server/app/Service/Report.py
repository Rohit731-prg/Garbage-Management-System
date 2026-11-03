from sqlalchemy.orm.session import Session
from fastapi import HTTPException

from app.DB.Report import Report
from app.Model.Report import ReportModel

async def submitReport(db: Session, data: ReportModel):
    try:
        new_report = Report(
            user_id=data.user_id,
            report_image=data.report_image,
            report_description=data.report_description,
            latitude=data.latitude,
            longitude=data.longitude,
            country=data.country,
            state=data.state,
            district=data.district,
            city=data.city,
            street=data.street
        )
        db.add(new_report)
        db.commit()
        db.refresh(new_report)
        return new_report
    except HTTPException as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


async def getReportsByUserID(db: Session, user_id: int):
    try:
        reports = db.query(Report).filter(Report.user_id == user_id).all()
        return reports
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def getAllReportsByState(db: Session, state: str):
    try:
        reports = db.query(Report).filter(Report.state == state).all()
        return reports
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
