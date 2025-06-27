from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from geoalchemy2.shape import to_shape

from . import models, schemas
from .database import engine, SessionLocal, Base

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/points", response_model=schemas.PointRead)
async def create_point(point: schemas.PointCreate, db: AsyncSession = Depends(get_db)):
    geom = f'POINT({point.longitude} {point.latitude})'
    db_point = models.Point(
        name=point.name,
        description=point.description,
        location=geom
    )
    db.add(db_point)
    await db.commit()
    await db.refresh(db_point)

    shape = to_shape(db_point.location)
    return schemas.PointRead(
        id=db_point.id,
        name=db_point.name,
        description=db_point.description,
        latitude=shape.y,
        longitude=shape.x
    )

@app.get("/points", response_model=list[schemas.PointRead])
async def get_points(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Point))
    points = result.scalars().all()

    return [
        schemas.PointRead(
            id=p.id,
            name=p.name,
            description=p.description,
            latitude=to_shape(p.location).y,
            longitude=to_shape(p.location).x
        ) for p in points
    ]
