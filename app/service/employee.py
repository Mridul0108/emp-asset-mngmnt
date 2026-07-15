from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.employee import (
    CreateEmployee,
    UpdateEmployee,
)

from app.crud.employee import (
    create_employee,
    get_employee,
    get_all_employees,
    update_employee,
    patch_employee,
    delete_employee,
)


def create_employee_service(
    db: Session,
    employee: CreateEmployee,
):
    return create_employee(
        db,
        employee,
    )


def get_all_employee_service(
    db: Session,
):
    return get_all_employees(db)


def get_employee_service(
    db: Session,
    email: str,
):
    employee = get_employee(
        db,
        email,
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found.",
        )

    return employee


def update_employee_service(
    db: Session,
    email: str,
    employee: CreateEmployee,
):
    return update_employee(
        db,
        email,
        employee,
    )


def patch_employee_service(
    db: Session,
    email: str,
    employee: UpdateEmployee,
):
    return patch_employee(
        db,
        email,
        employee,
    )


def delete_employee_service(
    db: Session,
    email: str,
):
    return delete_employee(
        db,
        email,
    )