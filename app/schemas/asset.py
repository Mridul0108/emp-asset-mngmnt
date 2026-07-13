from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class AssetBase(BaseModel):
    asset_code: str
    asset_name: str
    category: str
    brand: str
    status: str
    employee_id: Optional[UUID] = None
    assigned_at: Optional[datetime] = None
    returned_at: Optional[datetime] = None


class CreateAsset(AssetBase):
    pass


class UpdateAsset(BaseModel):
    asset_code: Optional[str] = None
    asset_name: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    status: Optional[str] = None
    employee_id: Optional[UUID] = None
    assigned_at: Optional[datetime] = None
    returned_at: Optional[datetime] = None


class AssetResponse(AssetBase):
    asset_id: UUID
    created_at: datetime
  

    class Config:
        from_attributes = True