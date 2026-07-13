from pydantic import BaseModel


class DepartmentAssetCount(BaseModel):
    department: str
    count: int


class DashboardResponse(BaseModel):
    total_employees: int
    total_assets: int
    assigned_assets: int
    available_assets: int
    department_asset_count: list[DepartmentAssetCount]