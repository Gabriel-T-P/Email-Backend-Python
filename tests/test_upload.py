import io
from tests.conftest import HEADERS
from tests.utils import make_pdf_bytes, make_txt_bytes
from app.api.v1.upload import MAX_FILE_SIZE

class TestUploadFile:

    def test_classify_file_txt(self, client):
        txt_bytes = make_txt_bytes("Este é um email de teste em TXT")

        response = client.post(
            "/api/v1/file",
            files={"file": ("email.txt", io.BytesIO(txt_bytes), "text/plain")},
            headers=HEADERS,
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "classification" in data["data"]
        assert "response" in data["data"]
        assert "analysis" in data["data"]

    def test_classify_file_pdf(self, client):
        pdf_bytes = make_pdf_bytes("Conteúdo de teste em PDF")

        response = client.post(
            "/api/v1/file",
            files={"file": ("email.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
            headers=HEADERS,
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "classification" in data["data"]
        assert "response" in data["data"]
        assert "analysis" in data["data"]

    def test_classify_file_invalid_format(self, client):
        file_content = b"Sou uma imagem, nao um email"

        response = client.post(
            "/api/v1/file",
            files={"file": ("foto.jpg", io.BytesIO(file_content), "image/jpeg")},
            headers=HEADERS,
        )

        assert response.status_code == 400
        data = response.json()
        assert data["detail"] == "Formato de arquivo não suportado"

    def test_classify_file_too_large(self, client):
        large_file_bytes = b"a" * (MAX_FILE_SIZE + 1)

        response = client.post(
            "/api/v1/file",
            files={"file": ("large_file.txt", io.BytesIO(large_file_bytes), "text/plain")},
            headers=HEADERS,
        )

        assert response.status_code == 400
        data = response.json()
        assert data["detail"] == "Arquivo muito grande"
