import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app
from app.db.session import get_db, SessionLocal
from app.models.mission import Mission as MissionModel
from app.schemas.mission import MissionCreate, MissionUpdate

# Create a new database session for testing
@pytest.fixture(scope="module")
def test_db():
    """Fixture to provide a database session for testing.

    This fixture overrides the `get_db` dependency to use a test database session
    and ensures the session is closed after the tests are complete.
    """
    app.dependency_overrides[get_db] = lambda: SessionLocal()
    yield SessionLocal()
    SessionLocal().close()

@pytest.fixture(scope="module")
def client():
    """Fixture to provide a TestClient instance for testing.

    This fixture initializes and returns a FastAPI TestClient for making API requests.
    """
    return TestClient(app)

BASE_URL = "/api/v1/missions"

def test_create_mission(client, test_db):
    """Test the creation of a new mission.

    Sends a POST request to create a new mission with sample data. Verifies that
    the response status is 200 and checks that the response data contains the
    correct mission details and an 'id' field.
    """
    mission_data = {"name": "Test Mission", "description": "Test Description", "robot_id": 1}
    response = client.post(BASE_URL, json=mission_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == mission_data["name"]
    assert response_data["description"] == mission_data["description"]
    assert response_data["robot_id"] == mission_data["robot_id"]
    assert "id" in response_data

def test_read_mission(client, test_db):
    """Test retrieving a specific mission by ID.

    First creates a mission and then sends a GET request to retrieve it by its ID.
    Verifies that the response status is 200 and checks that the retrieved data
    matches the created mission's details.
    """
    mission_data = {"name": "Test Mission", "description": "Test Description", "robot_id": 1}
    create_response = client.post(BASE_URL, json=mission_data)
    mission_id = create_response.json()["id"]

    response = client.get(f"{BASE_URL}/{mission_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == mission_id
    assert response_data["name"] == mission_data["name"]

def test_update_mission(client, test_db):
    """Test updating an existing mission.

    Creates a mission, then sends a PUT request to update it with new data. Verifies
    that the response status is 200 and checks that the updated data matches the
    provided update data.
    """
    mission_data = {"name": "Test Mission", "description": "Test Description", "robot_id": 1}
    create_response = client.post(BASE_URL, json=mission_data)
    mission_id = create_response.json()["id"]

    update_data = {"name": "Updated Mission", "description": "Updated Description", "robot_id": 2}
    response = client.put(f"{BASE_URL}/{mission_id}", json=update_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == update_data["name"]
    assert response_data["description"] == update_data["description"]
    assert response_data["robot_id"] == update_data["robot_id"]

def test_read_missions(client, test_db):
    """Test listing all missions.

    Creates two missions and sends a GET request to retrieve the list of missions.
    Verifies that the response status is 200 and checks that at least two missions
    are present in the response data.
    """
    mission_data1 = {"name": "Mission 1", "description": "Description 1", "robot_id": 1}
    mission_data2 = {"name": "Mission 2", "description": "Description 2", "robot_id": 2}
    client.post(BASE_URL, json=mission_data1)
    client.post(BASE_URL, json=mission_data2)

    response = client.get(BASE_URL)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) >= 2

def test_read_mission_not_found(client):
    """Test retrieving a non-existent mission by ID.

    Sends a GET request for a mission ID that does not exist. Verifies that the response
    status is 404 and checks that the response detail indicates the mission was not found.
    """
    response = client.get(f"{BASE_URL}/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Mission not found"}
