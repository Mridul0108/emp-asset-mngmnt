from fastapi import FastAPI

from app.db.database import Base, engine
from app.routers.employee import router as employee_router
from app.routers.asset import router as asset_router



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Slack",
)

app.include_router(employee_router)
app.include_router(asset_router)

