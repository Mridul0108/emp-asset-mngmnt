from fastapi import FastAPI

from app.db.database import Base, engine
from app.routers.employee import router as employee_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Slack",
)

app.include_router(employee_router)


@app.get("/")
def root():
    return {
        "message": "Employee Asset Management API is running."
    }