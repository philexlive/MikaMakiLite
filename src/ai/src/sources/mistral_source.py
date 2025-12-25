from typing import Optional

from pydantic import Field

from pydantic_ai.providers.mistral import MistralProvider
from pydantic_ai.models.mistral import MistralModel

from src.core.ai_source import AISource


class MistralSource(AISource):
    api_key: Optional[str] = Field(alias='mistral_api_key')

    def build(self) -> MistralModel:
        provider = MistralProvider(api_key=self.api_key)
        model = MistralModel(
            self.model_name,
            provider=provider
        )

        return model