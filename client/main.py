from src.client import client


def main():
    client.start()
    client.run_until_disconnected()


if __name__ == "__main__":
    main()