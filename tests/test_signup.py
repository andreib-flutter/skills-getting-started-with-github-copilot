"""Signup endpoint tests using AAA structure."""

from urllib.parse import quote

from fastapi import status

import src.app as app_module


def test_signup_success_adds_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    encoded_activity = quote(activity_name)

    # Act
    response = client.post(
        f"/activities/{encoded_activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    assert email in app_module.activities[activity_name]["participants"]


def test_signup_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "someone@mergington.edu"
    encoded_activity = quote(activity_name)

    # Act
    response = client.post(
        f"/activities/{encoded_activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Activity not found"
