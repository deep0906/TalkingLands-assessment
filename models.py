from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from .database import Base

class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    location = Column(Geometry("POINT", srid=4326))  # WGS84
