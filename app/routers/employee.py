from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud.employee import (
    create_employee,
    get_all_employees,
    get_employee,
    update_employee,
    patch_employee,
    delete_employee,
)
from app.schemas.employee import (
    CreateEmployee,
    UpdateEmployee,
    EmployeeResponse,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee_route(
    employee: CreateEmployee,
    db: Session = Depends(get_db),
):
    return create_employee(db, employee)


@router.get(
    "/",
    response_model=list[EmployeeResponse],
)
def get_all_employees_route(
    db: Session = Depends(get_db),
):
    return get_all_employees(db)


@router.get(
    "/{employee_email}",
    response_model=EmployeeResponse,
)
def get_employee_route(
    employee_email: str,
    db: Session = Depends(get_db),
):
    return get_employee(db, employee_email)


@router.put(
    "/{employee_email}",
    response_model=EmployeeResponse,
)
def update_employee_route(
    employee_email: str,
    employee: UpdateEmployee,
    db: Session = Depends(get_db),
):
    return update_employee(db, employee_email, employee)


@router.patch(
    "/{employee_email}",
    response_model=EmployeeResponse,
)
def patch_employee_route(
    employee_email: str,
    employee: UpdateEmployee,
    db: Session = Depends(get_db),
):
    return patch_employee(db, employee_email, employee)


@router.delete(
    "/{employee_email}",
)
def delete_employee_route(
    employee_email: str,
    db: Session = Depends(get_db),
):
    return delete_employee(db, employee_email)