from pydantic import BaseModel
from typing import List

class PolygonCreate(BaseModel):
    name: str
    density: float
    coordinates: List[List[List[float]]]

class PolygonRead(BaseModel):
    id: int
    name: str
    density: float
    coordinates: List[List[List[float]]]

    class Config:
        orm_mode = True
