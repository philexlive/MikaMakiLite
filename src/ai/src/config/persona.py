import yaml

from typing import Optional, Any

from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings, 
    SettingsConfigDict,
    PydanticBaseSettingsSource
)


class Persona(BaseModel):
    name: str
    bio: Optional[str]


class YamlConfigSettingsSource(PydanticBaseSettingsSource):
    def get_field_value(self, field, field_name):
        try:
            encoding = self.config.get('env_file_encoding')
            with open('config/persona.yaml', 'r', encoding=encoding) as f:
                return yaml.safe_load(f)[field_name], field_name, False
        except FileNotFoundError:
            return {}, field_name, False
    
    def prepare_field_value(self, field_name, field, value, value_is_complex):
        return value

    def __call__(self) -> dict[str, Any]:
        d: dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(
                field, field_name
            )
            field_value = self.prepare_field_value(
                field_name, field, field_value, value_is_complex
            )
            if field_value is not None:
                d[field_key] = field_value
            
        return d


class PersonaSettings(BaseSettings):
    name: str = Field()
    bio: Optional[str] = Field()
    
    model_config = SettingsConfigDict(env_file_encoding='utf-8')

    @classmethod
    def settings_customise_sources(
        cls, 
        settings_cls, 
        init_settings, 
        env_settings, 
        dotenv_settings, 
        file_secret_settings
    ):
        return (
            init_settings,
            YamlConfigSettingsSource(settings_cls),
            env_settings, 
            file_secret_settings
        )

persona = PersonaSettings()