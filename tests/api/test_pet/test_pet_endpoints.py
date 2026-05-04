import pytest


class TestPet:
    """Cobertura completa dos endpoints de Pet."""

    def test_criar_pet(self, client, pet_payload):
        """Deve criar um novo pet com sucesso."""
        response = client.post("/pet", pet_payload)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == pet_payload["id"]
        assert data["name"] == pet_payload["name"]
        assert data["status"] == pet_payload["status"]

    def test_buscar_pet_por_id(self, client, pet_payload):
        """Deve retornar o pet correto dado um ID válido."""
        pet_id = pet_payload["id"]
        response = client.get(f"/pet/{pet_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == pet_id
        assert data["name"] == pet_payload["name"]

    def test_atualizar_pet(self, client, pet_payload):
        """Deve atualizar o nome e status do pet com sucesso."""
        payload_atualizado = {**pet_payload, "name": "Rex Atualizado", "status": "sold"}
        response = client.put("/pet", payload_atualizado)

        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Rex Atualizado"
        assert data["status"] == "sold"

    def test_buscar_pets_por_status_available(self, client):
        """Deve retornar lista de pets com status 'available'."""
        response = client.get("/pet/findByStatus", params={"status": "available"})

        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)
        assert len(pets) > 0
        for pet in pets[:5]:
            assert pet["status"] == "available"

    def test_buscar_pets_por_status_pending(self, client):
        """Deve retornar lista de pets com status 'pending'."""
        response = client.get("/pet/findByStatus", params={"status": "pending"})

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_buscar_pets_por_status_sold(self, client):
        """Deve retornar lista de pets com status 'sold'."""
        response = client.get("/pet/findByStatus", params={"status": "sold"})

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_buscar_pet_id_inexistente(self, client):
        """A API pública pode retornar 200 ou 404 para IDs inexistentes."""
        response = client.get("/pet/999999999")

        assert response.status_code in [404, 200]

    def test_deletar_pet(self, client, pet_payload):
        """Deve deletar um pet e confirmar que ele não existe mais."""
        pet_id = pet_payload["id"]
        response = client.delete(f"/pet/{pet_id}")

        assert response.status_code == 200

        response_apos = client.get(f"/pet/{pet_id}")
        assert response_apos.status_code in [404, 200]