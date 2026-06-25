from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI API Test Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "AI API Test Platform is running"}


@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)