from pydantic import BaseModel, Field

class ReportModel(BaseModel):
    user_id: int = Field(..., description="The ID of the user who submitted the report")
    report_image: str | None = None
    report_description: str = Field(..., description="A description of the report")
    latitude: float = Field(..., description="The latitude of the report location")
    longitude: float = Field(..., description="The longitude of the report location")
    country: str = Field(..., description="The country of the report location")
    state: str = Field(..., description="The state of the report location")
    district: str = Field(..., description="The district of the report location")
    city: str = Field(..., description="The city of the report location")
    street: str = Field(..., description="The street of the report location")