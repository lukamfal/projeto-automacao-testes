import pytest
from core.api_client import ApiClient


@pytest.fixture(scope="session")
def client():
    """Fixture que fornece o cliente de API para todos os testes."""
    return ApiClient()


@pytest.fixture(scope="session")
def pet_payload():
    """Payload padrão para criação de um pet."""
    return {
        "id": 999991,
        "name": "Rex",
        "status": "available",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["https://example.com/rex.jpg"],
        "tags": [{"id": 1, "name": "friendly"}]
    }


@pytest.fixture(scope="session")
def user_payload():
    """Payload padrão para criação de um usuário."""
    return {
        "id": 999991,
        "username": "test_user_auto",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "senha123",
        "phone": "11999999999",
        "userStatus": 1
    }
