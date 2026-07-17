from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AgentSettings(BaseSettings):
    api_key: str
    model_name: str = Field(default="mistral-medium-latest",)
    
    model_config = SettingsConfigDict(env_prefix="AI_", extra="ignore")


agent_settings = AgentSettings()