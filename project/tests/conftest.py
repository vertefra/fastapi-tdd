import os

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app import main
from app.config import get_settings, Settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=1, database_url=os.getenv("DATABASE_TEST_URL"))


# Fixture are reusable objects for tests They have a scope associated with them
# which indicates how often the fixture is invoked
#
# 1-function - (default) once per test
# 2-class - once per test class
# 3-module - once per test module
# 4-session - once per test session


@pytest.fixture(scope="module")
def test_app():
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    # Set up definition
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
    with TestClient(app) as test_client:

        yield test_client
