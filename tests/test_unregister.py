"""Unregister endpoint tests using AAA structure."""

from urllib.parse import quote

from fastapi import status

import src.app as app_module


def test_unregister_success_removes_participant(client):
    # Arrange
    activity_name = "Programming Class"
    email = "temporary.student@mergington.edu"
    encoded_activity = quote(activity_name)
    app_module.activities[activity_name]["participants"].append(email)

    # Act
    response = client.delete(
        f"/activities/{encoded_activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in app_module.activities[activity_name]["participants"]


def test_unregister_student_not_signed_up_returns_404(client):
    # Arrange
    activity_name = "Programming Class"
    email = "not.registered@mergington.edu"
    encoded_activity = quote(activity_name)

    # Act
    response = client.delete(
        f"/activities/{encoded_activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Student not signed up for this activity"
