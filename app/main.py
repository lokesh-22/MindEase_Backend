from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models, database
from .routes import users, journals  # adjust if these are named differently

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(journals.router)

# Root test route
@app.get("/")
def root():
    return {"message": "API is running"}
