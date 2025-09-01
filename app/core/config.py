import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env


class Settings:
    PROJECT_NAME: str = "Email Classifier API"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    API_KEY: str = os.getenv("API_KEY", "default_key")


settings = Settings()
