from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    employee_name: str
    employee_age: str
    employee_gender: str
    employee_email: EmailStr
    employee_post: str
    department: str
    years_of_experience: Optional[str] = None
    joining_date: date


class CreateEmployee(EmployeeBase):
    pass


class UpdateEmployee(BaseModel):
    employee_name: Optional[str] = None
    employee_age: Optional[str] = None
    employee_gender: Optional[str] = None
    employee_email: Optional[EmailStr] = None
    employee_post: Optional[str] = None
    department: Optional[str] = None
    years_of_experience: Optional[str] = None
    joining_date: Optional[date] = None


class EmployeeResponse(EmployeeBase):
    employee_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True