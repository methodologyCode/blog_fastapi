from fastapi import FastAPI

from db import models
from db.database import engine
from routers import user, post, comment

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)

models.Base.metadata.create_all(engine)
