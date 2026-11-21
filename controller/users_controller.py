from dao.database import db_dependency, User
from form.form import UserBasePost, UserBaseGet
from main import app
from fastapi import HTTPException, status

@app.post('/users',status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBasePost, db: db_dependency):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user.id

@app.put('/users', status_code=status.HTTP_200_OK)
async def update_user(updated_user:UserBaseGet, db: db_dependency):
    user = db.query(User).filter(
        User.id == updated_user.id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.username = updated_user.username

    db.commit()
    db.refresh(user)

    return user

@app.get('/users', status_code=status.HTTP_200_OK)
async def read_users(db: db_dependency):
    users = db.query(User).all()
    return users

@app.get('/users/{user_id}', status_code=status.HTTP_200_OK)
async def read_user(user_id:int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@app.delete('/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id:int, db: db_dependency):
    user = db.query(User).filter(
        User.id == user_id
    ).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()
    return None