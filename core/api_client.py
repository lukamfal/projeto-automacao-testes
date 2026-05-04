import requests


BASE_URL = "https://petstore.swagger.io/v2"


class ApiClient:
    """Cliente HTTP reutilizável para todos os endpoints da API Petstore."""

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint, params=None):
        return self.session.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint, payload=None):
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)

    def put(self, endpoint, payload=None):
        return self.session.put(f"{self.base_url}{endpoint}", json=payload)

    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}{endpoint}")
