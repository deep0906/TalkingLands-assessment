from sqlalchemy import Column, Integer, String, Float
from geoalchemy2 import Geometry
from .database import Base

class Polygon(Base):
    __tablename__ = "polygons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    density = Column(Float)
    geometry = Column(Geometry("POLYGON", srid=4326))
