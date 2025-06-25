from fastapi import FastAPI
from . import models, database
from .routes import users

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API is running"}
