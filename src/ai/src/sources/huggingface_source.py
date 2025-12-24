from pydantic_ai.providers.huggingface import HuggingFaceProvider
from pydantic_ai.models.huggingface import HuggingFaceModel

from src.core.ai_source import AISource


class HuggingFaceSource(AISource):
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

