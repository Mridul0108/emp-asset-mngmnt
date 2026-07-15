from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.auth import get_current_user
from app.models.user import User

from app.schemas.asset import (
    CreateAsset,
    UpdateAsset,
    AssetResponse,
)
from app.service.asset import (
    create_asset_service,
    get_asset_service,
    get_all_assets_service,
    update_asset_service,
    patch_asset_service,
    delete_asset_service

)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)


@router.post(
    "/",
    response_model=AssetResponse,
)
def create_asset_route(
    asset: CreateAsset,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_asset_service(db, asset)


@router.get(
    "/",
    response_model=list[AssetResponse],
)
def get_all_asset_route(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_assets_service(db)


@router.get(
    "/{asset_code}",
    response_model=AssetResponse,
)
def get_asset_route(
    asset_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_asset_service(
        db,
        asset_code,
    )




@router.put(
    "/{asset_code}",
    response_model=AssetResponse,
)
def update_asset_route(
    asset_code: str,
    asset: CreateAsset,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_asset_service(
        db,
        asset_code,
        asset,
    )


@router.patch(
    "/{asset_code}",
    response_model=AssetResponse,
)
def patch_asset_route(
    asset_code: str,
    asset: UpdateAsset,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return patch_asset_service(
        db,
        asset_code,
        asset,
    )


@router.delete("/{asset_code}")
def delete_asset_route(
    asset_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_asset_service(
        db,
        asset_code,
    )