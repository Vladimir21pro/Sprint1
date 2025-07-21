from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import SessionLocal
from models import Base, engine, User, Coords, Level, Pereval, Image
from sqlalchemy.orm import Session
import base64

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ImageData(BaseModel):
    title: str
    img_base64: str

class CoordsData(BaseModel):
    latitude: float
    longitude: float
    height: int

class LevelData(BaseModel):
    winter: str = ""
    summer: str = ""
    autumn: str = ""
    spring: str = ""

class UserData(BaseModel):
    email: str
    phone: str
    fam: str
    name: str
    otc: str

class PerevalData(BaseModel):
    beauty_title: str
    title: str
    other_titles: str
    connect: str
    user: UserData
    coords: CoordsData
    level: LevelData
    images: list[ImageData]

@app.post("/submitData")
def submit_data(data: PerevalData, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.user.email).first()
    if not user:
        user = User(**data.user.dict())
        db.add(user)
        db.flush()

    coords = Coords(**data.coords.dict())
    level = Level(**data.level.dict())
    db.add(coords)
    db.add(level)
    db.flush()

    pereval = Pereval(
        beauty_title=data.beauty_title,
        title=data.title,
        other_titles=data.other_titles,
        connect=data.connect,
        user_id=user.id,
        coords_id=coords.id,
        level_id=level.id,
        status="new"
    )
    db.add(pereval)
    db.flush()

    for img in data.images:
        image = Image(
            title=img.title,
            img=base64.b64decode(img.img_base64),
            pereval_id=pereval.id
        )
        db.add(image)

    db.commit()
    return {"status": "ok", "id": pereval.id}
