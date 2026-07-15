from fastapi import (
    APIRouter,
    Depends,
    Form,
    status,
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import (
    RegisterUser,
    LoginUser,
    UserResponse,
    Token,
)
from app.service.user import (
    register_service,
    login_service,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
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

    return register_service(
        db=db,
        user=user,
    )


@router.post(
    "/login",
    response_model=Token,
    status_code=status.HTTP_200_OK,
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
    return login_service(
        db=db,
        user=login_data,
    )