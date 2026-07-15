from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.asset import (
    CreateAsset,
    UpdateAsset
)

from app.crud.asset import (
    create_asset,
    get_asset,
    get_all_assets,
    update_asset,
    patch_asset,
    delete_asset,
)






def create_asset_service(
    db: Session, 
    asset: CreateAsset
    
):
    return create_asset(db, asset)





def get_all_assets_service(
    db: Session 
):
    return get_all_assets(db)




def get_asset_service(
    db: Session,
    asset_code: str
   
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






def update_asset_service(
    db: Session,
    asset_code: str,
    asset: CreateAsset
    
):
    return update_asset(
        db,
        asset_code,
        asset,
    )





def patch_asset_service(
    db: Session ,
    asset_code: str,
    asset: UpdateAsset
    
):
    return patch_asset(
        db,
        asset_code,
        asset,
    )





def delete_asset_service(
    db: Session,
    asset_code: str
    
):
    return delete_asset(
        db,
        asset_code,
    )