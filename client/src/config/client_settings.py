from typing import Optional, Self

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ClientSettings(BaseSettings):
    api_id: str
    api_hash: str
    session_name: str
    watermark: str

    model_config = SettingsConfigDict(env_prefix="TELEGRAM_", extra="ignore")
    
client_settings = ClientSettings()
