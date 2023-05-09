from collections.abc import Generator
from fastapi.testclient import TestClient

import pytest
from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    # Setup

    with TestClient(app) as test_client:
        # Testing
        yield test_client

    # Teardown
