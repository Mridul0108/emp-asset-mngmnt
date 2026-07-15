from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.db.database import get_db
from app.models.user import User

from app.schemas.employee import (
    CreateEmployee,
    UpdateEmployee,
    EmployeeResponse,
)

from app.service .employee import (
    create_employee_service,
    get_employee_service,
    get_all_employee_service,
    update_employee_service,
    patch_employee_service,
    delete_employee_service,
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
    return create_employee_service(
        db,
        employee,
    )


@router.get(
    "/",
    response_model=list[EmployeeResponse],
)
def get_all_employee_route(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_employee_service(db)


@router.get(
    "/{email}",
    response_model=EmployeeResponse,
)
def get_employee_route(
    email: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_employee_service(
        db,
        email,
    )


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
    return update_employee_service(
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
    return patch_employee_service(
        db,
        email,
        employee,
    )


@router.delete(
    "/{email}",
)
def delete_employee_route(
    email: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_employee_service(
        db,
        email,
    )