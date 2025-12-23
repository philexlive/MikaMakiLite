import telethon as tl
from src.tg.bot import client

def run_ai():
    with client:
        client.run_until_disconnected()


def main():
    client.start()
    run_ai()
    if client.is_connected:
        client.disconnect()


if __name__ == "__main__":
    main()