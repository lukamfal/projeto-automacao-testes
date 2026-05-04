import pytest


class TestStore:
    """Cobertura completa dos endpoints de Store (pedidos)."""

    @pytest.fixture(scope="class")
    def order_payload(self):
        """Payload padrão para criar um pedido."""
        return {
            "id": 999991,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2025-05-01T10:00:00.000Z",
            "status": "placed",
            "complete": False
        }

    def test_consultar_inventario(self, client):
        """Deve retornar o inventário com contagem por status."""
        response = client.get("/store/inventory")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0

    def test_criar_pedido(self, client, order_payload):
        """Deve criar um pedido com sucesso."""
        response = client.post("/store/order", order_payload)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == order_payload["id"]
        assert data["petId"] == order_payload["petId"]
        assert data["status"] == "placed"

    def test_buscar_pedido_por_id(self, client, order_payload):
        """Deve retornar o pedido correto dado um ID válido."""
        order_id = order_payload["id"]
        response = client.get(f"/store/order/{order_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == order_id

    def test_buscar_pedido_id_inexistente(self, client):
        """Deve retornar 404 para um pedido que não existe."""
        response = client.get("/store/order/999999999")

        assert response.status_code == 404

    def test_deletar_pedido(self, client, order_payload):
        """Deve deletar o pedido e confirmar remoção."""
        order_id = order_payload["id"]
        response = client.delete(f"/store/order/{order_id}")

        assert response.status_code == 200

        response_apos = client.get(f"/store/order/{order_id}")
        assert response_apos.status_code == 404
