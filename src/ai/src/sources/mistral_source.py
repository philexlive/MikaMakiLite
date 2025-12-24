from pydantic_ai.providers.mistral import MistralProvider
from pydantic_ai.models.mistral import MistralModel

from src.core.ai_source import AISource


class MistralSource(AISource):
    def build(self) -> MistralModel:
        provider = MistralProvider(
            api_key=self.api_key,
            base_url=self.api_key
        )
        model = MistralModel(
            api_key=self.api_key,
            provider=provider
        )

        return model