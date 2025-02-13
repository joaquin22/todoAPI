import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:  # type: ignore
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient
