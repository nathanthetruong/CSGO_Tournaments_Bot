import discord
import os
from hltvCommands import fazeEvents, fazeRoster, topTeams, teamEvents, teamRoster, upcomingEvents
from funResponse import broky_respond, bait_respond, command_list, tense1983_respond, faze_respond

client = discord.Client()

rageWords = [
    "green", "rage", "mad", "mald", "ratio", "ratio'd", "fatherless", "smash",
    "cope", "copium", "monitor", "keyboard", "desk", "gaming", "gamer"
]


@client.event
# Prints "What's up!" to console on startup
async def on_ready():
    print("What\'s up!")


# "/" is the command symbol
@client.event
async def on_message(message):
    #FaZe's team page
    fazeURL = "https://www.hltv.org/team/6667/faze"

    # Doesn't respond if the bot is the one who messages
    if message.author == client.user:
        return

    # Shortcut for message.content
    msg = message.content
    print(msg)
    msg = msg.lower()

    # "/help" outputs all the commands
    if msg == ("/help"):
        await command_list(message)

    # "/bait" outputs a random number divided by 8
    elif msg == ("/bait"):
        await bait_respond(message)

    # "/top teams" outputs list of top 30 teams
    elif msg == ("/top teams"):
        input = msg
        await topTeams(message)

    # "/events" outputs all the commands
    if msg == ("/events"):
        await upcomingEvents(message)

    # "/events [Team Name]" outputs events for team
    elif msg.startswith("/events"):
        input = msg
        await teamEvents(message, input)

    # "/roster [Team Name]" outputs events for team
    elif msg.startswith("/roster"):
        input = msg
        await teamRoster(message, input)

    # "/faze events" outputs list of ongoing and upcoming events
    elif msg == ("/faze events"):
        await fazeEvents(message, fazeURL)

    # Checks for any mention of FaZe Roster and outputs the roster
    elif msg == ("/faze roster"):
        await fazeRoster(message, fazeURL)

    # Checks for any mention of broky and outputs the TRUTH
    elif msg.find("broky") > -1:
        await broky_respond(message)

    # Checks for any mention of rage and outputs LIFE
    elif msg in rageWords:
        await tense1983_respond(message)

    # Checks for any mention of faze and outputs HARD FACTS
    elif msg.find("faze") > -1:
        await faze_respond(message)


# Runs the bot
my_secret = os.environ["DISCORD TOKEN"]
client.run(my_secret)
