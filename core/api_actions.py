class ApiActions:
    def __init__(self, client):
        self.client = client

    def get_products(self):
        response = self.client.get("/products")
        assert response.status_code == 200
        return response.json()