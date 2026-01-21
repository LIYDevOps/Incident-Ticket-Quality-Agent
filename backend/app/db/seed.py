from app.db.database import SessionLocal, init_db
from app.db.models import Category, AssignmentGroup, ConfigurationItem


def seed_data():
    init_db()
    db = SessionLocal()

    if db.query(Category).first():
        return  # already seeded

    db.add_all([
        Category(name="Database"),
        Category(name="Network"),
        Category(name="Application")
    ])

    db.add_all([
        AssignmentGroup(name="DB Support", category="Database"),
        AssignmentGroup(name="Network Ops", category="Network"),
        AssignmentGroup(name="App Support", category="Application")
    ])

    db.add_all([
        ConfigurationItem(name="Postgres-Prod", ci_type="Database"),
        ConfigurationItem(name="Core-Switch-01", ci_type="Network"),
        ConfigurationItem(name="App-Server-01", ci_type="Application")
    ])

    db.commit()
    db.close()
