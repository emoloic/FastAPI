from fastapi import HTTPException
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog import models, schemas

def create(request: schemas.User, db: Session):
    hashedPassword = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with the id {id} is not available")
    
    return user