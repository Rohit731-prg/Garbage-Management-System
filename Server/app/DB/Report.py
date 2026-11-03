from sqlalchemy import Column, Integer, Float, String, DateTime
from app.Config.ConnectDB import base

class Report(base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    report_image = Column(String, index=True)
    report_description = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    country = Column(String, index=True)
    district = Column(String, index=True)
    state = Column(String, index=True)
    city = Column(String, index=True)
    street = Column(String, index=True)
    report_status = Column(String, index=True)
    report_created_at = Column(DateTime, index=True)
    report_updated_at = Column(DateTime, index=True)