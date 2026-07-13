from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import CreateEmployee, UpdateEmployee


def handle_integrity_error(db: Session, error: IntegrityError):
    db.rollback()

    raise HTTPException(
        status_code=400,
        detail="Invalid or missing data. Please check the required fields.",
    )


def create_employee(db: Session, employee: CreateEmployee):
    try:
        new_employee = Employee(**employee.model_dump())

        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)

        return new_employee

    except IntegrityError as e:
        handle_integrity_error(db, e)


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee(db: Session, employee_email: str):
    employee = (
        db.query(Employee)
        .filter(Employee.employee_email == employee_email)
        .first()
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found.",
        )

    return employee


def update_employee(
    db: Session,
    employee_email: str,
    employee: UpdateEmployee,
):
    db_employee = get_employee(db, employee_email)

    try:
        update_data = employee.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_employee, key, value)

        db.commit()
        db.refresh(db_employee)

        return db_employee

    except IntegrityError as e:
        handle_integrity_error(db, e)


def patch_employee(
    db: Session,
    employee_email: str,
    employee: UpdateEmployee,
):
    db_employee = get_employee(db, employee_email)

    try:
        update_data = employee.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_employee, key, value)

        db.commit()
        db.refresh(db_employee)

        return db_employee

    except IntegrityError as e:
        handle_integrity_error(db, e)


def delete_employee(
    db: Session,
    employee_email: str,
):
    employee = get_employee(db, employee_email)

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully."
    }