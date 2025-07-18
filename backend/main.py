from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import auth, posts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(posts.router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)