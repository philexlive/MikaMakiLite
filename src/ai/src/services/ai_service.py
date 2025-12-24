from pydantic import BaseModel, Field

from pydantic_ai import Agent

from src.config.persona import persona
from src.config.ai_settings import ai_settings

from src.core.ai_source import AISource

from src.sources.huggingface_source import HuggingFaceSource
from src.sources.mistral_source import MistralSource


# Text response of model
class ClientResponse(BaseModel):
    text: str = Field(description="Client responded.")


class AIService:
    async def run(self):
        source: AISource
        
        settings = ai_settings.model_dump(
            exclude_none=True,
            include=[
                Field(alias="api_key", validation_alias='hf_api_key')
            ]
        )
        source = HuggingFaceSource(**settings)

        model = source.build()

        ai_client = Agent(
            model,
            output_type=ClientResponse,
            instructions=(
                'Your identity.'
                'Name: {name}'
                'Bio:'
                '{bio}'
            ).format(
                name=persona.name,
                bio=persona.bio
            ),
            end_strategy='exhaustive'
        )

        result = await ai_client.run("Hello, what is your name?")
        print(result)