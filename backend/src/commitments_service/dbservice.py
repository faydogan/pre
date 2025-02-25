"""Database service module for the commitments service."""

import os
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from commitments_service.models import AssetClass, Commitment
from commitments_service.sample_data import asset_classes, commitments


sqlite_file_name = os.path.join(os.path.dirname(__file__), "database.db")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_sqlite_db():
    """Create a database with the tables defined in the models using the engine defined."""

    SQLModel.metadata.create_all(engine)


def get_session():
    """Get a session from the engine and yield it for further use."""

    with Session(engine) as session:
        yield session


# Type alias for the Session dependency
SessionDep = Annotated[Session, Depends(get_session)]


def fill_db_with_sample_data():
    """Fill the database with the sample data."""

    with Session(engine) as session:
        for asset_class in asset_classes:
            db_asset_class = AssetClass(**asset_class)
            session.add(db_asset_class)
        session.commit()

        for commitment in commitments:
            db_commitment = Commitment(**commitment)
            session.add(db_commitment)
        session.commit()


def clean_db():
    """Clean the database by removing all the data."""

    if os.path.exists(sqlite_file_name):
        os.remove(sqlite_file_name)


if __name__ == "__main__":
    clean_db()
    create_sqlite_db()
    fill_db_with_sample_data()
