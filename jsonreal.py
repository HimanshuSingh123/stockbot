import json
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

# from responses import getResponse

# load the token here
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
# $print(TOKEN)

# bot set up
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)

data_store = {}


@client.event
async def data_store(json_data):
    data_store = json.loads(json_data)
    print(data_store)
    # await send_message(message, usrMsg)


@client.event
async def show_data(ctx):
    await ctx.send(data_store)
    # await send_message(message, usrMsg)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
    # update?
