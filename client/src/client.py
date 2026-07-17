import sys
import logging
import httpx

from pydantic_ai.models.mistral import MistralModel
from pydantic_ai.providers.mistral import MistralProvider
from telethon import TelegramClient, events

from src.config.client_settings import client_settings
from src.config.persona_settings import persona_settings
from src.config.agent_settings import agent_settings
from src.core.text_request import TextRequest
from src.agent import agent


client = TelegramClient(
    session=f"../.secrets/{client_settings.session_name}.session", 
    api_id=client_settings.api_id, 
    api_hash=client_settings.api_hash,
    proxy={
        'proxy_type': 'socks5',
        'addr': '127.0.0.1',
        'port': 10808,
    }
)


logger = logging.getLogger(__name__)
logging.basicConfig(stream=logging.StreamHandler(sys.stdout), level=logging.INFO)


model = MistralModel(
    agent_settings.model_name,
    provider=MistralProvider(
        api_key=agent_settings.api_key
    )
)

async def get_response(
    request: TextRequest,
) -> str:
    async with httpx.AsyncClient() as http_client:
        try:
            result = await agent.run(
                request.text,
                model=model,
                instructions=persona_settings.persona.bio,
                deps=request,
            )

            response = result.output.text
        except httpx.RequestError as e:
            logger.error(e)
            response = "Sry, bad request to AI..."
        
        return f"{response}\n{client_settings.watermark}"


async def user_handler(event):
    chat_id = event.chat_id
    
    logger.info("Responding")

    sender = await event.get_sender()
    
    request = TextRequest(
        first_name=sender.first_name or "",
        second_name=sender.last_name or "",
        username=sender.username,
        text=event.message.text
    )

    response = await get_response(request)
    
    await event.reply(response)


@client.on(events.NewMessage)
async def handler(event):
    if not 'mika' in event.message.text:
        logger.info('Conversation has no keyword.')
        return
    
    logger.info('Conversation starting...')
    
    await user_handler(event)