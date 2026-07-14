from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.auth import get_current_user
from app.models.user import User

from app.schemas.asset import (
    CreateAsset,
    UpdateAsset,
    AssetResponse,
)

from app.crud.asset import (
    create_asset,
    get_asset,
    get_all_assets,
    update_asset,
    patch_asset,
    delete_asset,
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
    return create_asset(db, asset)


@router.get(
    "/",
    response_model=list[AssetResponse],
)
def get_all_asset_route(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_assets(db)


@router.get(
    "/{asset_code}",
    response_model=AssetResponse,
)
def get_asset_route(
    asset_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    asset = get_asset(
        db,
        asset_code,
    )

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found.",
        )

    return asset


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
    return update_asset(
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
    return patch_asset(
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
    return delete_asset(
        db,
        asset_code,
    )