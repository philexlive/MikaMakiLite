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

        try:
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
        except:
            respond = "{}\n\n{}".format(
                "I have no tokens but can answer with this hardcoded text:(",
                character_config.watermark
            )

        rpl = message.reply_to

        if rpl:
            if len(tg_config.chat_id) < 2:
                log = get_chat_log(
                    sender=sender,
                    chat=event.chat_id,
                    rpl=event.message.id,
                    msg=event.text,
                    rsp=respond
                )
                print(log)
                
                await event.reply(respond)
            else:
                topic = rpl.reply_to_top_id or rpl.reply_to_msg_id

                if rpl and topic == tg_config.chat_id[1]:
                    await event.reply(respond)

                log = get_chat_log(
                    sender=sender,
                    chat=event.chat_id,
                    topic=topic,
                    rpl=event.message.id,
                    msg=event.text,
                    rsp=respond
                )
                print(log)


def get_chat_log(sender, chat, rpl, msg, rsp, topic=None):
    chat_info = (
        f"chat={chat}, topic={topic}" 
        if topic else 
        f"chat={chat}"
    )
    text = """
        Sender({sender})
        Chat({chat_info})
        Rpl({rpl})
        Msg({msg})
        Rsp({rsp})
    """
    return (
        textwrap
        .dedent(text)
        .format(
            sender=sender,
            chat_info=chat_info,
            rpl=rpl,
            msg=msg,
            rsp=rsp
        )
        .strip()
    )