from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import getResponse

# load the token here
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
# $print(TOKEN)

# bot set up
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# message functionality
async def send_message(
    message: Message, usrMsg: str
) -> None:  # only meant to execute code
    if (
        not usrMsg
    ):  # if there is no user message... usually because intents were not enabled
        print("message was empty because intents were not enabled probably")
        return

    if (
        is_private := usrMsg[0] == "?"
    ):  # so := (walrus) used when you want to exectue if statement and store that val in a variable
        # basically we are doing private dms here, the "?" is there to command that
        usrMsg = usrMsg[1:]

    try:
        response: str = getResponse(usrMsg)
        (
            await message.author.send(response)
            if is_private
            else await message.channel.send(response)
        )  # basically if is_private is true, then we send response to user, otherwise we send to the channel where it was sent from
    except Exception as e:
        print(e)


# handling start up
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")


# handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if (
        message.author == client.user
    ):  # this makes sure that the bot doesn't constantly reply to itself
        return

    username: str = str(message.author)
    usrMsg: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{usrMsg}"')
    await send_message(message, usrMsg)

    # main entry point


def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
