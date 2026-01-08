from pydantic import field_validator

from pydantic_settings import (
    BaseSettings,
    YamlConfigSettingsSource
)

from pydantic_ai.models import Model
from pydantic_ai.models.huggingface import HuggingFaceModel
from pydantic_ai.providers.huggingface import HuggingFaceProvider
from pydantic_ai.models.mistral import MistralModel
from pydantic_ai.providers.mistral import MistralProvider


class AgentSettings(BaseSettings):
    models: dict[str, Model]

    @field_validator('models', mode='before')
    @classmethod
    def model_factory(cls, value: dict) -> dict[str, Model]:
        def get_clean_field(field):
            if not isinstance(field, dict):
                return field
            return {k.replace('-', '_'): get_clean_field(v) for k, v in field.items()}
                
        cleaned_dict = get_clean_field(value)
        models = {}

        for name, fields in cleaned_dict.items():
            provider_data = fields.pop('provider', {})
            model_name = fields.get('model_name')

            match name:
                case 'mistral': 
                    provider = MistralProvider(**provider_data)
                    models[name] = MistralModel(
                        model_name,
                        provider=provider
                    )
                case _:
                    provider = HuggingFaceProvider(**provider_data)
                    models[name] = HuggingFaceModel(
                        model_name,
                        provider=provider
                    )
        return models
    
    @classmethod
    def settings_customise_sources(
        cls, 
        settings_cls, 
        init_settings, 
        env_settings, 
        dotenv_settings, 
        file_secret_settings
    ):
        yaml_config_settings_source = YamlConfigSettingsSource(
            settings_cls,
            yaml_file='config/models.yaml',
            yaml_file_encoding='utf-8'
        )
        return (
            init_settings, 
            env_settings, 
            dotenv_settings, 
            yaml_config_settings_source,
            file_secret_settings
        )
    

agent_settings = AgentSettings()