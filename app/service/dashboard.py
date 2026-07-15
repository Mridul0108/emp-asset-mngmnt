
from sqlalchemy.orm import Session

from app.crud.dashboard import get_dashboard




def get_dashboard_service(
    db: Session
):
    return get_dashboard(db)