from telethon import TelegramClient
import asyncio
import time
from telethon import events, functions
from telethon.tl.functions.contacts import ResolveUsernameRequest
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
chanel_hash = os.getenv('SECRET_CHAT_HASH')
owner_id = os.getenv('OWNER_ID')

client = TelegramClient('Username', api_id, api_hash)

message = '1'


def main():

    client.start()

    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        if event.is_private:
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            print(event.message.message)
            channel = await client(functions.messages.CheckChatInviteRequest(chanel_hash))
            # print(channel.chat)
            client_list = await client.get_participants(channel.chat)
            print(client_list)

            msg = event.message.message
            sender = await event.get_sender()

            if (sender.id == owner_id):
                await client.send_message(sender, "Good day my boss")
                for user in client_list:
                    time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                    await client.send_message(user, msg )
                await client.send_message(sender, f'Message "{msg}" was sent to all participants')
            else:
                await client.send_message(sender, f'You are not my boss')

            
            
            # print(event)
            # user = await client.get_entity(event.from_id)
            # print(event.original_update.user_id)
            # print(sender)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
