from typing import Optional, Self

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ClientSettings(BaseSettings):
    api_id: str = Field(validation_alias="TG_API_ID")
    api_hash: str = Field(validation_alias="TG_API_HASH")
    session: str = Field(validation_alias="TG_SESSION")
    wt: str = Field(validation_alias="WATERMARK")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


client_settings = ClientSettings()
