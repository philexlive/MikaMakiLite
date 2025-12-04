import pandas as pd
import asyncio


async def msg_to_dict(msg, client):
    reply_to = msg.reply_to.reply_to_msg_id if msg.reply_to else None
    user_id = msg.from_id.user_id
    user = await client.get_entity(user_id)

    return {
        "user_id": user_id,
        "username": user.username,
        "peer_id": msg.peer_id.channel_id,
        "msg_id": msg.id,
        "message": msg.message,
        "date": msg.date,
        "reply_to": reply_to
    }


async def get_table_from_chat(chat, topic, client):
    tasks = []
    async for msg in client.iter_messages(chat, reply_to=topic, limit=100):
        if msg.sender_id:
            task = msg_to_dict(msg, client)
            tasks.append(task)
    
    messages = await asyncio.gather(*tasks)
    print(pd.DataFrame(messages))