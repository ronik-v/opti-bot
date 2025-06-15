from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """App env params"""

    model_config = SettingsConfigDict(env_file=".env")

    API_TOKEN: str
    CLIENT_TG_ID: str


config = AppConfig()
