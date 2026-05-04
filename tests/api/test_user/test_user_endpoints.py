import pytest


class TestUser:
    """Cobertura completa dos endpoints de User."""

    def test_criar_usuario(self, client, user_payload):
        """Deve criar um novo usuário com sucesso."""
        response = client.post("/user", user_payload)

        assert response.status_code == 200

    def test_buscar_usuario_por_username(self, client, user_payload):
        """Deve retornar o usuário correto pelo username."""
        username = user_payload["username"]
        response = client.get(f"/user/{username}")

        assert response.status_code == 200
        data = response.json()
        assert data["username"] == username
        assert data["email"] == user_payload["email"]

    def test_atualizar_usuario(self, client, user_payload):
        """Deve atualizar os dados do usuário com sucesso."""
        username = user_payload["username"]
        payload_atualizado = {**user_payload, "firstName": "Atualizado", "email": "novo@example.com"}
        response = client.put(f"/user/{username}", payload_atualizado)

        assert response.status_code == 200

    def test_login_usuario(self, client, user_payload):
        """Deve realizar login e retornar token de sessão."""
        response = client.get("/user/login", params={
            "username": user_payload["username"],
            "password": user_payload["password"]
        })

        assert response.status_code == 200
        data = response.json()
        assert "logged in" in data.get("message", "").lower()

    def test_logout_usuario(self, client):
        """Deve realizar logout com sucesso."""
        response = client.get("/user/logout")

        assert response.status_code == 200

    def test_buscar_usuario_inexistente(self, client):
        """Deve retornar 404 para um usuário que não existe."""
        response = client.get("/user/usuario_que_nao_existe_xyz999")

        assert response.status_code == 404

    def test_criar_usuarios_em_lista(self, client):
        """Deve criar múltiplos usuários de uma vez."""
        lista = [
            {"id": 999992, "username": "user_lista_1", "firstName": "User", "lastName": "A",
             "email": "a@example.com", "password": "pass1", "phone": "11111111111", "userStatus": 1},
            {"id": 999993, "username": "user_lista_2", "firstName": "User", "lastName": "B",
             "email": "b@example.com", "password": "pass2", "phone": "22222222222", "userStatus": 1},
        ]
        response = client.post("/user/createWithList", lista)

        assert response.status_code == 200

    def test_deletar_usuario(self, client, user_payload):
        """Deve deletar o usuário e confirmar remoção."""
        username = user_payload["username"]
        response = client.delete(f"/user/{username}")

        assert response.status_code == 200

        response_apos = client.get(f"/user/{username}")
        assert response_apos.status_code == 404
