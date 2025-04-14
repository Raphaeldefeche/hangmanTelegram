import random

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
		┃     ┃
		┃
		┃
		┃
		┃
		┗━━━━━━━
""",
    """
		┏━━━━━┓
		┃     ┃
		┃     O
		┃
		┃
		┃
		┗━━━━━━━
""",
    """
		┏━━━━━┓
		┃     ┃
		┃     O
		┃    /|\\
		┃
		┃
		┗━━━━━━━
""",
    """
		┏━━━━━┓
		┃     ┃
		┃     O
		┃    /|\\
		┃    / \\
		┃
		┗━━━━━━━ """,
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
    "Java",
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

success = None

tried = []

while error < MAX_ERROR and wordguess != word:
    print(HANGMAN_PARTS[error])
    print(f"you used {tried}")
    print(f"the word is : {wordguess}")

    if success is None:
        print("in the theme of the computers (list by chatGPT)")
        print("enjoy")
    elif success:
        print(f"the letter {guess} is in the word")
    else:
        print(f"sorry bro, {guess} is not in the word")

    guess = input("guess: ").lower()

    if guess == "exit" or guess == "quit":
        break
    while guess in tried:
        print("you already tried this letter, you dumbass")
        guess = input("trie again ").lower()

    tried.append(guess)

    if guess in word:
        success = True
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += wordguess[i]

        wordguess = new

    else:
        success = False
        error += 1

if error == MAX_ERROR:
    print(HANGMAN_PARTS[error])
    print("too bad, you died, looser")

else:
    print("you are very smart")

print(f"the word was '{word}'")
print("\nsee you next time!")
