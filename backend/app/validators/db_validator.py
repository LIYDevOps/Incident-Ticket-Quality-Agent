from app.db.database import SessionLocal
from app.db.models import Category, AssignmentGroup, ConfigurationItem


def validate_against_reference(incident: dict):
    db = SessionLocal()
    errors = []

    if not db.query(Category).filter_by(name=incident["category"]).first():
        errors.append("Invalid category")

    if not db.query(AssignmentGroup).filter_by(
        name=incident["assignment_group"],
        category=incident["category"]
    ).first():
        errors.append("Assignment group does not match category")

    if not db.query(ConfigurationItem).filter_by(
        name=incident["cmdb_ci"]
    ).first():
        errors.append("Invalid configuration item")

    db.close()
    return errors
