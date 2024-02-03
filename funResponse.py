import random

brokyResponse = [
    "GODKY", "GOATKY", "#1 AWPer For Sure", "broky GOD", "Latvian Laser"
]

fazeResponse = [
    "The best team!", "#1 in the World", "eZaF", "rain GOD", "broky GOD",
    "Twistzz GOD", "ropz GOD", "karrigan GOD",
    "rain, broky, Twistzz, ropz, karrigan GODS"
]


async def command_list(message):
    output = "List of Commands (Capitalization Doesn't Matter):\n"
    output += "\"/FaZe Events\"                              Lists all the events of FaZe\n"
    output += "\"/FaZe Roster\"                                     Lists the roster of FaZe\n"
    output += "\"/Bait\"                                                       Randomly rate a bait\n"
    output += "\"/Events\"                    Lists all the Upcoming Events"
    output += "\"/Events [TeamName]\"      Lists all the events of the Team\n"
    output += "\"/Roster [TeamName]\"             Lists the roster of the Team\n"
    output += "\"/Top Teams\"                     Lists the top 30 Teams Currently\n"
    await message.channel.send(output)


async def broky_respond(message):
    await message.channel.send(random.choice(brokyResponse))


async def bait_respond(message):
    await message.channel.send(str(random.randint(0, 8)) + "/8")


async def tense1983_respond(message):
    await message.channel.send(
        "https://tenor.com/view/csgo-banging-table-angry-mad-rage-quit-gif-17478101"
    )


async def faze_respond(message):
    await message.channel.send(random.choice(fazeResponse))
