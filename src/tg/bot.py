import textwrap
from telethon import TelegramClient, events
from src.config import tg_config, character_config
from src.ai.client import inference

client = TelegramClient(
    session=tg_config.session, 
    api_id=tg_config.api_id, 
    api_hash=tg_config.api_hash
)

@client.on(events.NewMessage)
async def replies(event):
    msg = event.raw_text
    if 'MikaMakiLite' in msg and event.chat_id == tg_config.chat_id[0]:
        
        sender = await event.get_sender()

        sender = "{} - {} {}".format(
            sender.username,
            sender.first_name,
            sender.last_name
        )
        message = event.message

        completion = inference.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": character_config.ai.who.format(
                        model=character_config.ai.model,
                        username=sender,
                        respond=msg)
                }
            ]
        )
        respond = "{}\n\n{}".format(
            completion.choices[0].message.content,
            character_config.watermark
        )

        rpl = message.reply_to
        
        if rpl:
            topic = rpl.reply_to_top_id or rpl.reply_to_msg_id

            if rpl and topic == tg_config.chat_id[1]:
                respond = "Hello World"
                
                log = textwrap.dedent("""
                Sender({sender})
                Topic({topic})
                Rpl({rpl})
                Msg({msg})
                Rsp({respond})
                """).strip().format(
                    sender=sender,
                    topic=topic,
                    rpl=event.message.id,
                    msg=event.text,
                    respond=respond
                )
                print(log)
                
                await event.reply(respond)
