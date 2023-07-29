from functools import lru_cache
from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session, create_session
from sqlalchemy_utils import create_database, database_exists
from app.database import Base

from app.main import app


@pytest.fixture(scope="session")
def db() -> Session:
    db_session = create_session()
    engine = db_session.bind
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.bind = engine
    Base.metadata.drop_all()
    Base.metadata.create_all()
    return db_session


@pytest.fixture()
def cleanup_db(db: Session) -> None:
    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())


@pytest.fixture()
def app_client(cleanup_db: Any) -> Generator[TestClient, None, None]:
    yield TestClient(app)
