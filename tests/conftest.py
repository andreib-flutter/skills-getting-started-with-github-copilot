"""Shared pytest fixtures for backend API tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

ORIGINAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities so tests are isolated and deterministic."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(ORIGINAL_ACTIVITIES))
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    """Provide a FastAPI test client bound to the main app instance."""
    return TestClient(app_module.app)
