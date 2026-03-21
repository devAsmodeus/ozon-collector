from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["TEST", "LOCAL", "DEV", "PROD"] = "LOCAL"

    # Ozon Seller API
    OZON_CLIENT_ID: str = ""
    OZON_API_KEY: str = ""
    OZON_API_BASE_URL: str = "https://api-seller.ozon.ru"

    # Ozon Performance API (реклама)
    OZON_PERFORMANCE_CLIENT_ID: str = ""
    OZON_PERFORMANCE_CLIENT_SECRET: str = ""
    OZON_PERFORMANCE_API_URL: str = "https://api-performance.ozon.ru"

    # PostgreSQL
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "ozon_user"
    DB_PASS: str = "ozon_pass"
    DB_NAME: str = "ozon_collector"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}"
            f"/{self.DB_NAME}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        extra="ignore",
    )


settings = Settings()
