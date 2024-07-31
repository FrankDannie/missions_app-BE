import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app
from app.db.session import get_db, SessionLocal
from app.models.robot import Robot as RobotModel
from app.schemas.robot import RobotCreate, RobotUpdate

# Create a new database session for testing
@pytest.fixture(scope="module")
def test_db():
    """
    Fixture for setting up and tearing down a test database session.

    Overrides the `get_db` dependency to use a test database session.
    Yields the test database session for use in tests and closes the
    session after tests are completed.
    """
    app.dependency_overrides[get_db] = lambda: SessionLocal()
    yield SessionLocal()
    SessionLocal().close()

@pytest.fixture(scope="module")
def client():
    """
    Fixture for setting up the FastAPI test client.

    Creates a new `TestClient` instance for making HTTP requests to
    the FastAPI application.
    """
    return TestClient(app)

def test_create_robot(client, test_db):
    """
    Test case for creating a new robot.

    Sends a POST request to the `/api/v1/robots/` endpoint with
    the robot data and verifies that the response contains the
    correct details and a valid ID.
    """
    robot_data = {"name": "Test Robot", "model_name": "Model X"}
    response = client.post("/api/v1/robots/", json=robot_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == robot_data["name"]
    assert response_data["model_name"] == robot_data["model_name"]
    assert "id" in response_data

def test_read_robot(client, test_db):
    """
    Test case for retrieving a specific robot by ID.

    Creates a new robot and then sends a GET request to the `/api/v1/robots/{robot_id}` 
    endpoint to retrieve the robot details. Verifies that the returned data
    matches the created robot data.
    """
    robot_data = {"name": "Test Robot", "model_name": "Model X"}
    create_response = client.post("/api/v1/robots/", json=robot_data)
    robot_id = create_response.json()["id"]

    response = client.get(f"/api/v1/robots/{robot_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == robot_id
    assert response_data["name"] == robot_data["name"]

def test_update_robot(client, test_db):
    """
    Test case for updating an existing robot.

    Creates a new robot, then sends a PUT request to the `/api/v1/robots/{robot_id}` 
    endpoint with updated robot data. Verifies that the response contains
    the updated details.
    """
    robot_data = {"name": "Test Robot", "model_name": "Model X"}
    create_response = client.post("/api/v1/robots/", json=robot_data)
    robot_id = create_response.json()["id"]

    update_data = {"name": "Updated Robot", "model_name": "Model Y"}
    response = client.put(f"/api/v1/robots/{robot_id}", json=update_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == update_data["name"]
    assert response_data["model_name"] == update_data["model_name"]

def test_read_robots(client, test_db):
    """
    Test case for listing all robots.

    Creates multiple robots and sends a GET request to the `/api/v1/robots/` 
    endpoint to list all robots. Verifies that the response contains
    at least the number of robots created.
    """
    robot_data1 = {"name": "Robot 1", "model_name": "Model A"}
    robot_data2 = {"name": "Robot 2", "model_name": "Model B"}
    client.post("/api/v1/robots/", json=robot_data1)
    client.post("/api/v1/robots/", json=robot_data2)

    response = client.get("/api/v1/robots/")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) >= 2

def test_read_robot_not_found(client):
    """
    Test case for handling retrieval of a non-existent robot.

    Sends a GET request to the `/api/v1/robots/999` endpoint with a
    non-existent robot ID. Verifies that the response status code
    is 404 and the error message indicates that the robot was not found.
    """
    response = client.get("/api/v1/robots/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Robot not found"}
