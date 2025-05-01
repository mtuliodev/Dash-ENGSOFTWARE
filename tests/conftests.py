# tests/conftest.py
import pytest
from database import engine, metadata, SessionLocal

@pytest.fixture(scope="function", autouse=True)
def db():
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)
