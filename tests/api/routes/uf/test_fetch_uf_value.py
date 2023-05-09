from fastapi import status
from fastapi.testclient import TestClient
from datetime import date

from schemas import UF


def test_fetch_uf_value(client: TestClient):
    """
    GIVEN   a `target_date`
    WHEN    the GET /uf/ endpoint is called
    THEN    the response should be `HTTP_200_OK`
    """
    # GIVEN
    query_parameters = {"target_date": date(2023, 1, 1).strftime("%Y-%m-%d")}

    # WHEN
    response = client.get(f"/uf/", params=query_parameters)
    content = response.json()
    # THEN

    assert response.status_code == status.HTTP_200_OK, content
    UF(**content)


def test_invalid_target_date(client: TestClient):
    """
    GIVEN   an invalid `target_date`
    WHEN    the GET /uf/ endpoint is called
    THEN    the response should be `HTTP_400_BAD_REQUEST`
    """
    # GIVEN
    query_parameters = {"target_date": date(2025, 1, 1).strftime("%Y-%m-%d")}

    # WHEN
    response = client.get(f"/uf/", params=query_parameters)
    content = response.json()
    # THEN

    assert response.status_code == status.HTTP_400_BAD_REQUEST, content
    assert content["detail"] == "There was an error with SII API"
