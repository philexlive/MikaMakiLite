from typing import Optional

from pydantic import Field

from pydantic_ai.providers.huggingface import HuggingFaceProvider
from pydantic_ai.models.huggingface import HuggingFaceModel

from src.core.ai_source import AISource


class HuggingFaceSource(AISource):
    api_key: Optional[str] = Field(alias='hf_api_key')
    provider_name: Optional[str]

    def build(self) -> HuggingFaceModel:
        provider = HuggingFaceProvider(
            api_key=self.api_key,
            provider_name=self.provider_name
        )
        model = HuggingFaceModel(
            self.model_name,
            provider=provider
        )

        return model

