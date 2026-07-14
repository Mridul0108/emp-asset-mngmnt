from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.auth import get_current_user
from app.models.user import User

from app.schemas.employee import (
    CreateEmployee,
    UpdateEmployee,
    EmployeeResponse,
)

from app.crud.employee import (
    create_employee,
    get_employee,
    get_all_employees,
    update_employee,
    patch_employee,
    delete_employee,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


@router.post(
    "/",
    response_model=EmployeeResponse,
)
def create_employee_route(
    employee: CreateEmployee,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_employee(db, employee)


@router.get(
    "/",
    response_model=list[EmployeeResponse],
)
def get_all_employee_route(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_employees(db)


@router.get(
    "/{email}",
    response_model=EmployeeResponse,
)
def get_employee_route(
    email: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    employee = get_employee(db, email)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found.",
        )

    return employee


@router.put(
    "/{email}",
    response_model=EmployeeResponse,
)
def update_employee_route(
    email: str,
    employee: CreateEmployee,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_employee(
        db,
        email,
        employee,
    )


@router.patch(
    "/{email}",
    response_model=EmployeeResponse,
)
def patch_employee_route(
    email: str,
    employee: UpdateEmployee,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return patch_employee(
        db,
        email,
        employee,
    )


@router.delete("/{email}")
def delete_employee_route(
    email: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_employee(
        db,
        email,
    )