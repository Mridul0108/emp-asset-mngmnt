from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud.asset import (
    create_asset,
    get_all_assets,
    get_asset,
    update_asset,
    patch_asset,
    delete_asset,
)
from app.schemas.asset import (
    CreateAsset,
    UpdateAsset,
    AssetResponse,
)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)


@router.post(
    "/",
    response_model=AssetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_asset_route(
    asset: CreateAsset,
    db: Session = Depends(get_db),
):
    return create_asset(db, asset)


@router.get(
    "/",
    response_model=list[AssetResponse],
)
def get_all_assets_route(
    db: Session = Depends(get_db),
):
    return get_all_assets(db)


@router.get(
    "/{asset_code}",
    response_model=AssetResponse,
)
def get_asset_route(
    asset_code: str,
    db: Session = Depends(get_db),
):
    return get_asset(db, asset_code)


@router.put(
    "/{asset_code}",
    response_model=AssetResponse,
)
def update_asset_route(
    asset_code: str,
    asset: UpdateAsset,
    db: Session = Depends(get_db),
):
    return update_asset(db, asset_code, asset)


@router.patch(
    "/{asset_code}",
    response_model=AssetResponse,
)
def patch_asset_route(
    asset_code: str,
    asset: UpdateAsset,
    db: Session = Depends(get_db),
):
    return patch_asset(db, asset_code, asset)


@router.delete(
    "/{asset_code}",
)
def delete_asset_route(
    asset_code: str,
    db: Session = Depends(get_db),
):
    return delete_asset(db, asset_code)