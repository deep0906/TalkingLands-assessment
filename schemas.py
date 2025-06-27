from pydantic import BaseModel

class PointCreate(BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float

class PointRead(BaseModel):
    id: int
    name: str
    description: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True
