import os

from telethon import TelegramClient, events
from huggingface_hub import InferenceClient
from dotenv import load_dotenv


load_dotenv()


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session = os.getenv("SESSION")
model = os.getenv("AI_MODEL")
ai_provider = os.getenv("AI_PROVIDER")
ai_api_key = os.getenv("AI_API_KEY")


client = TelegramClient(session, api_id, api_hash)


PROMPT = """
Respond:
{}
"""


inference = InferenceClient(
    provider=ai_provider,
    api_key=ai_api_key
)


def get_messages(response):
    return PROMPT.format(response)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'MikaMakiLite' in event.raw_text:
        completion = inference.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": get_messages(event.raw_text)
                }
            ]
        )
        await event.reply(completion.choices[0].message.content + "\n\n🍭 MikaMakiLite")


def main():
    client.start()
    client.run_until_disconnected()


with client:
    main()