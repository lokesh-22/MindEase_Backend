from fastapi import FastAPI
from . import models, database
from .routes import users

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import users

app = FastAPI()

# Create all tables
models.Base.metadata.create_all(bind=database.engine)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔓 Allow all domains — use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Authorization, Content-Type, etc.
)

# Routers
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API is running"}


app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API is running"}
