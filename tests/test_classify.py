from tests.conftest import HEADERS
from app.api.v1.classify import MAX_TEXT_LENGTH, MIN_TEXT_LENGTH, MAX_WORDS

class TestClassifierText:

    def test_classify_text_productive(self, client):
        response = client.post(
            "/api/v1/text",
            json={"text": "Preciso de atualização do meu pedido"},
            headers=HEADERS,
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "classification" in data["data"]
        assert data["data"]["classification"]["category"] == "produtivo"
        assert 0.0 <= data["data"]["classification"]["confidence"] <= 1.0
        assert "analysis" in data["data"]
        assert "processingTime" in data["data"]["analysis"]
        assert "wordCount" in data["data"]["analysis"]
        assert "response" in data["data"]

    def test_classify_text_unproductive(self, client):
        response = client.post(
            "/api/v1/text",
            json={"text": "Feliz Natal a todos!"},
            headers=HEADERS,
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["data"]["classification"]["category"] == "improdutivo"
        assert "response" in data["data"]

    def test_classify_text_special_chars(self, client):
        response = client.post(
            "/api/v1/text",
            json={"text": "@cliente #pedido 123!!!"},
            headers=HEADERS,
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "classification" in data["data"]
        assert "analysis" in data["data"]
        assert "response" in data["data"]

    def test_classify_text_missing_field(self, client):
        response = client.post(
            "/api/v1/text",
            json={},
            headers=HEADERS,
        )

        assert response.status_code == 422  # erro de validação Pydantic

    def test_classify_text_max_text_length(self, client):
        long_text = "a" * (MAX_TEXT_LENGTH + 1)

        response = client.post(
            "/api/v1/text",
            json={"text": long_text},
            headers=HEADERS,
        )

        assert response.status_code == 400  # erro de validação
        data = response.json()
        assert data["detail"] == "Texto muito grande"

    def test_classify_text_min_text_length(self, client):
        small_text = "a" * (MIN_TEXT_LENGTH - 1)

        response = client.post(
            "/api/v1/text",
            json={"text": small_text},
            headers=HEADERS,
        )

        assert response.status_code == 400  # erro de validação
        data = response.json()
        assert data["detail"] == "Texto muito pequeno"

    def test_classify_text_max_word(self, client):
        max_words = "a " * (MAX_WORDS + 1)

        response = client.post(
            "/api/v1/text",
            json={"text": max_words},
            headers=HEADERS,
        )

        assert response.status_code == 400  # erro de validação
        data = response.json()
        assert data["detail"] == "Texto com muitas palavras"
