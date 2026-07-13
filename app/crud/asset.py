from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import CreateAsset, UpdateAsset


def handle_integrity_error(db: Session, error: IntegrityError):
    db.rollback()

    error_message = str(error.orig)

    if "assets_asset_code_key" in error_message:
        raise HTTPException(
            status_code=400,
            detail="Asset code already exists."
        )

    raise HTTPException(
        status_code=400,
        detail=error_message,
    )


def validate_asset(asset):
    status = asset.status.lower()

    if status == "available":
        if asset.employee_id is not None:
            raise HTTPException(
                status_code=400,
                detail="Available assets cannot have an employee assigned.",
            )

        if asset.assigned_at is not None:
            raise HTTPException(
                status_code=400,
                detail="Available assets cannot have an assigned date.",
            )

    elif status == "assigned":
        if asset.employee_id is None:
            raise HTTPException(
                status_code=400,
                detail="Assigned assets must have an employee.",
            )


def create_asset(db: Session, asset: CreateAsset):
    validate_asset(asset)

    try:
        new_asset = Asset(**asset.model_dump())

        db.add(new_asset)
        db.commit()
        db.refresh(new_asset)

        return new_asset

    except IntegrityError as e:
        handle_integrity_error(db, e)


def get_all_assets(db: Session):
    return db.query(Asset).all()


def get_asset(db: Session, asset_code: str):
    asset = (
        db.query(Asset)
        .filter(Asset.asset_code == asset_code)
        .first()
    )

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found.",
        )

    return asset


def update_asset(
    db: Session,
    asset_code: str,
    asset: UpdateAsset,
):
    db_asset = get_asset(db, asset_code)

    try:
        update_data = asset.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_asset, key, value)

        validate_asset(db_asset)

        db.commit()
        db.refresh(db_asset)

        return db_asset

    except IntegrityError as e:
        handle_integrity_error(db, e)


def patch_asset(
    db: Session,
    asset_code: str,
    asset: UpdateAsset,
):
    return update_asset(
        db=db,
        asset_code=asset_code,
        asset=asset,
    )


def delete_asset(
    db: Session,
    asset_code: str,
):
    asset = get_asset(db, asset_code)

    db.delete(asset)
    db.commit()

    return {
        "message": "Asset deleted successfully."
    }