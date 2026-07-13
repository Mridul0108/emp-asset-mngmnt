from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.asset import Asset


def get_dashboard(db: Session):
    total_employees = db.query(Employee).count()

    total_assets = db.query(Asset).count()

    assigned_assets = (
        db.query(Asset)
        .filter(Asset.status == "assigned")
        .count()
    )

    available_assets = (
        db.query(Asset)
        .filter(Asset.status == "available")
        .count()
    )

    department_asset_count = (
        db.query(
            Employee.department,
            func.count(Asset.asset_id).label("count"),
        )
        .join(
            Asset,
            Employee.employee_id == Asset.employee_id,
        )
        .group_by(Employee.department)
        .all()
    )

    department_asset_list = []

    for department, count in department_asset_count:
        department_asset_list.append(
            {
                "department": department,
                "count": count,
            }
        )

    return {
        "total_employees": total_employees,
        "total_assets": total_assets,
        "assigned_assets": assigned_assets,
        "available_assets": available_assets,
        "department_asset_count": department_asset_list,
    }