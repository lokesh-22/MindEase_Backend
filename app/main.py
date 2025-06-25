import uvicorn
from fastapi import FastAPI

from app.api.routes import (
    auth as auth_routes,
    mood as mood_routes,
    journal as journal_routes,
    activity as activity_routes,
    completed_activity as completed_routes,
)
from app.db.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MindEase API")

# Include routers
app.include_router(auth_routes.router)
app.include_router(mood_routes.router)
app.include_router(journal_routes.router)
app.include_router(activity_routes.router)
app.include_router(completed_routes.router)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
