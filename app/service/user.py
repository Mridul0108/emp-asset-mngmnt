from sqlalchemy.orm import Session
from app.schemas.user import (
    RegisterUser,
    LoginUser
)
from app.crud.user import (
    register_user,
    login_user,
)

def register_service(
    db: Session,
    user: RegisterUser,
    
):
    return register_user(
        db=db,
        user=user,
    )







def login_service(
    db: Session, 
    user: LoginUser,
   
):
    return login_user(
        db=db,
        user=user,
    )