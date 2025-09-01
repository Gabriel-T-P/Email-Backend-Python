import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
HEADERS = {"X-API-Key": API_KEY}


@pytest.fixture
def client():
    return TestClient(app)
