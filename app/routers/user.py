from fastapi import (
    APIRouter,
    Depends,
    Form,
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import RegisterUser, LoginUser, Token
from app.crud.user import register_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = RegisterUser(
        username=username,
        email=email,
        password=password,
    )

    return register_user(
        db=db,
        user=user,
    )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    login_data = LoginUser(
        email=email,
        password=password,
    )

    return login_user(
        db=db,
        user=login_data,
    )