# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware configuration
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/missions/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    return crud.create_mission(db=db, mission=mission)

@app.get("/missions/", response_model=List[schemas.Mission])
def read_missions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    missions = crud.get_missions(db, skip=skip, limit=limit)
    return missions

@app.get("/mission/{mission_id}", response_model=schemas.Mission)
def read_mission(mission_id: int, db: Session = Depends(get_db)):
    db_mission = crud.get_mission(db, mission_id=mission_id)
    if db_mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return db_mission

@app.post("/robots/", response_model=schemas.Robot)
def create_robot(robot: schemas.RobotCreate, db: Session = Depends(get_db)):
    return crud.create_robot(db=db, robot=robot)

@app.get("/robots/", response_model=List[schemas.Robot])
def read_robots(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    robots = crud.get_robots(db, skip=skip, limit=limit)
    return robots

@app.get("/robot/{robot_id}", response_model=schemas.Robot)
def read_robot(robot_id: int, db: Session = Depends(get_db)):
    db_robot = crud.get_robot(db, robot_id=robot_id)
    if db_robot is None:
        raise HTTPException(status_code=404, detail="Robot not found")
    return db_robot
