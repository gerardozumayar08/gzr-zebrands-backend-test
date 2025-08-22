from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    ### Project ###
    environment: str = Field("dev")
    title: str = Field("gzr-zebrands-backend-test")
    name: str = Field("catalog-products")
    description: str = Field(
        """
        """
    )
    description_openapi: str = Field("")
    version: str = Field("0.1.0")

    ### API ###
    api_v1_str: str = Field("/api/v1")
    http_client_timeout: int = Field(20)
    base_path: str = Path(__file__).resolve().parent.parent.parent.parent.__str__()
    language: str = Field("es")

    ### DB Connections
    db_name: str = Field("postgres")
    db_user: str = Field("postgres")
    db_password: str = Field("postgres")
    db_host: str = Field("localhost")
    db_port: int = Field(5432)
    db_ssl: bool = Field(True)

    ### Logging ###
    ### AWS ###
    cloud_watch_log_group: str = Field("api-catalog-products-logs")

    ### CLoud Provider ###
    ### AWS ###
    aws_region: str = Field("us-east-1")
    notications_email: str = Field("")

    ### Login ###
    secret_key: str = Field("secret_key")
    algorithm: str = Field("HS256")
    access_token_expire_minutes: int = Field(60)

    @property
    def sql_uri_connection(self):
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()
