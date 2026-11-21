
from dao.database import db_dependency, Comment
from form.form import CommentBase
from main import app
from fastapi import status

@app.post('/comments', status_code=status.HTTP_201_CREATED)
async def create_comment(comment:CommentBase, db: db_dependency):
    db_comment = Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    return db_comment.id