import asyncio
import aiohttp

async def send_message(session, url, headers, message_data):
    async with session.post(url, headers=headers, json=message_data) as response:
        if response.status == 200:
            print('Message sent successfully.')
        else:
            print('An error occurred. Message could not be sent.')

async def bump_channel(token, channel_id):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    # Ask for user input regarding message content, TTS option, and number of times to send
    message_content = input("Enter message content: ")
    tts_option = input("Enable TTS? (True/False): ")
    num_times_to_send = int(input("Enter number of times to send: "))

    message_data = {
        'content': message_content,
        'tts': bool(tts_option)
    }

    urls = [f'https://discord.com/api/v9/channels/{channel_id}/messages'] * num_times_to_send

    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for url in urls:
            task = asyncio.ensure_future(send_message(session=session, url=url,
                                                      headers=headers,
                                                      message_data=message_data))
            tasks.append(task)

        await asyncio.gather(*tasks)

# Usage example
token = "token"
channel_id = "channel_id"

loop=asyncio.get_event_loop()
loop.run_until_complete(bump_channel(token=token, channel_id=channel_id))