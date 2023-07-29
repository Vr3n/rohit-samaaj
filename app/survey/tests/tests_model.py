from collections.abc import Generator
from fastapi.testclient import TestClient
import pytest
from sqlalchemy.orm import Session

from app.survey.models import SamaajMemberMaster


@pytest.fixture()
def create_samaajmember(db: Session) -> Generator[SamaajMemberMaster,
                                                  None, None]:
    member = SamaajMemberMaster(
        first_name="John",
        last_name="Doe",
        father_name="Jae",
        mother_name="Halsey",
    )
    db.add(member)
    db.flush()
    yield member
    db.rollback()


def test_get(
        app_client: TestClient,
        create_samaajmember: SamaajMemberMaster) -> None:
    pass
