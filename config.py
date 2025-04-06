
import os

class Settings:
    PROJECT_NAME: str = "LegalMind V2 - Investigador"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend do LegalMind V2 com endpoints para investigações de mercado e web crawling controlado."
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

settings = Settings()
