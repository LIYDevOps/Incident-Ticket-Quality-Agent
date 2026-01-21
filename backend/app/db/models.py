from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


class AssignmentGroup(Base):
    __tablename__ = "assignment_groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String, nullable=False)


class ConfigurationItem(Base):
    __tablename__ = "configuration_items"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    ci_type = Column(String, nullable=False)
