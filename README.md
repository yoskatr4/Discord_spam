This is the README.md file for the main2.py file.

This file contains the code for a Discord bot that can be used to send messages to a channel. The bot can be used to send text messages, as well as messages that are read aloud using text-to-speech (TTS).

The bot is controlled by a user who provides input via the command line. The user can specify the content of the message, whether or not to use TTS, and the number of times to send the message.

The bot uses the Discord API to send messages to the channel. The API is a RESTful API that allows developers to create bots that interact with Discord.

To use the bot, you will need to create a Discord application and obtain a token. You can find instructions on how to do this on the Discord developer website.

Once you have a token, you can run the bot by executing the following command:

```
python main2.py <token> <channel_id>
```

Where <token> is your Discord token and <channel_id> is the ID of the channel you want to send messages to.

Here is an example of how to use the bot:

```
python main2.py <token> <channel_id>

Enter message content: Hello world!

Enable TTS? (True/False): True

Enter number of times to send: 5

Message sent successfully.
```

The bot will then send the message "Hello world!" to the channel five times, using TTS.
