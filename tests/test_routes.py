"""Route-level tests for the Mergington API."""

from fastapi import status


def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
    assert response.headers["location"] == expected_location


def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    payload = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(payload, dict)
    assert expected_activity in payload
    assert "participants" in payload[expected_activity]
