import uuid

from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.database import Base


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_name = Column(String, nullable=False)
    employee_age = Column(String, nullable=False)
    employee_gender = Column(String, nullable=False)
    employee_email = Column(String, unique=True, nullable=False)
    employee_post = Column(String, nullable=False)
    department = Column(String, nullable=False)
    years_of_experience = Column(String, nullable=True)
    joining_date = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)