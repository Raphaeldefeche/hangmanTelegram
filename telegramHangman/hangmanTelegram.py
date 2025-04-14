#!/usr/bin/python

from telethon import TelegramClient, events
import random

# import time
import sys
import os

api_id = "your api id"
api_hash = "your api hash"

client = TelegramClient("test", api_id, api_hash)

contact = os.getenv("CONTACT")

HANGMAN_PARTS = (
    """






  """,
    """







┗━━━━━━━ 
""",
    """

┃
┃
┃
┃
┃
┗━━━━━━━ 
""",
    """
┏━━━━━┓
┃
┃
┃
┃
┃
┗━━━━━━━ 
""",
    """
┏━━━━━┓
┃                   ┃
┃
┃
┃
┃
┗━━━━━━━ 
""",
    """
┏━━━━━┓
┃                   ┃
┃                    O
┃
┃
┃
┗━━━━━━━ 
""",
    """
┏━━━━━┓
┃                   ┃
┃                    O
┃                    /|\\
┃
┃
┗━━━━━━━ 
""",
    """
┏━━━━━┓
┃                   ┃
┃                    O
┃                    /|\\
┃                    / \\
┃
┗━━━━━━━ 
""",
)
MAX_ERROR = len(HANGMAN_PARTS) - 1

WORDS = (
    "algorithm",
    "application",
    "binary",
    "browser",
    "cache",
    "cloud",
    "coding",
    "compile",
    "database",
    "debugging",
    "encryption",
    "firewall",
    "framework",
    "hardware",
    "host",
    "hyperlink",
    "interface",
    "internet",
    "java",
    "keyboard",
    "logic",
    "malware",
    "memory",
    "network",
    "packet",
    "processor",
    "protocol",
    "query",
    "router",
    "script",
    "server",
    "software",
    "storage",
    "streaming",
    "syntax",
    "terminal",
    "token",
    "authentication",
    "backup",
    "bandwidth",
    "blockchain",
    "buffer",
    "checksum",
    "client",
    "cloud",
    "compiler",
    "console",
    "cryptography",
    "data",
    "debugger",
    "default",
    "digital",
    "disk",
    "document",
    "domain",
    "drive",
    "encryption",
    "extension",
    "file",
    "firewall",
    "folder",
    "function",
    "gateway",
    "graphic",
    "hash",
    "host",
    "hypertext",
    "index",
    "input",
    "integrate",
    "interface",
    "login",
    "macro",
    "memory",
    "module",
    "network",
    "offline",
    "online",
    "packet",
    "password",
    "platform",
    "protocol",
    "remote",
    "replica",
    "restore",
    "router",
    "runtime",
    "search",
    "server",
    "software",
    "static",
    "system",
    "transfer",
    "virus",
    "virtual",
    "widget",
    "wireless",
    "zoom",
)


word = random.choice(WORDS)

wordguess = "-" * len(word)

error = 0

guess = ""

# success = None

tried = []

message = """  

|-| /-\\ |\\| [, |\\/| /-\\ |\\|                                          

guess with one letter
'exit' or 'quit' to quit
in the theme of the computers (list by chatGPT)
enjoy
"""

# ____________________________________
# import random


# def reset():


# while error < MAX_ERROR and wordguess != word:
async def hangman(guess, message):
    global word, wordguess, error, tried

    # print(word)
    tried.append(guess)

    if guess in word:
        message += f"the letter {guess} is in the word\n"
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += wordguess[i]

        wordguess = new

    else:
        message += f"sorry bro, {guess} is not in the word\n"
        error += 1
    message += HANGMAN_PARTS[error]
    # message += f"you used : " + " ".join(map(str, tried))
    message += f"you used : {tried}"
    message += f"\nthe word is : {wordguess}\n"

    await client.send_message(contact, message)
    # await client.send_message(contact, str(error))
    # await client.send_message(contact, str(tried))
    # await client.send_message(contact, str(guess))
    # await client.send_message(contact, str(wordguess))


# ____________________________________
# async def main():

print("here")
# time.sleep(1)


@client.on(events.NewMessage(contact))
async def my_event_handler(event):
    global word, wordguess, error, tried
    # print(event.raw_text)
    # client.send_message(contact, message)
    message = ""
    guess = event.raw_text
    guess = guess.lower()

    if guess == "exit" or guess == "quit":
        message += f"\nthe word was '{word}'\nSee you next time!"
        await client.send_message(contact, message)
        sys.exit()
    if guess in tried:
        await client.send_message(
            contact, "You already tried that letter, you dumbass.\nTry again."
        )
        return

    await hangman(guess, message)
    if error == MAX_ERROR:
        message += HANGMAN_PARTS[error]
        message += "\ntoo bad, you died, looser"
        message += f"\nthe word was '{word}'\n"
        await client.send_message(contact, message)
        sys.exit()
    elif wordguess == word:
        message += "you are very smart\n"
        message += f"\nthe word was '{word}'\n"
        message += "\nsee you next time!\n"
        await client.send_message(contact, message)
        sys.exit()


# await client.send_message(contact, "see you soon")


# @client.on(events.NewMessage("me"))
# async def my_event_handler(event):
#     # if "hello" in event.raw_text:
#     #     await event.reply("hi!")
#     print(event.raw_text)
# client.send_message(contact, "end")


async def main():
    await client.send_message(contact, message)


# while error < MAX_ERROR and wordguess != word:
with client:
    client.loop.run_until_complete(main())

client.start()
client.run_until_disconnected()
# client.start()
# client.run_until_disconnected()
# reset()
# hangman(word, wordguess, error, guess, tried, message)
# async def response(conv):
#     name = await conv.get_response().raw_text
#     await conv.send_message(f"You said {name}")


# async def conver():
#     await conv.send_message("quoicoubeh test")
#     await response(conv)


# with client:
#     client.loop.run_until_complete(main())
# client.start()
# with client.conversation(313227467) as conv:
#     conver()
# conv.send_message('Thanks {}!'.format(name))
