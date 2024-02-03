import requests
from bs4 import BeautifulSoup

baseURL = "https://www.hltv.org"
rankingURL = "https://www.hltv.org/ranking/teams"
eventsURL = "https://www.hltv.org/events"


# Extracts from FaZe HLTV page and outputs events
async def fazeEvents(message, fazeURL):
    output = "_**Ongoing and Upcoming Events:**_\n"
    await message.channel.send(output)
    response = requests.get(fazeURL)
    soup = BeautifulSoup(response.text, "html.parser")
    event = soup.find("div", class_="upcoming-events-holder")
    links = event.findAll("a")
    # Puts all the event names in a list
    outputEvents = []
    counter = 0
    for div in event:
        outputEvent = div.text
        outputEvent = outputEvent.strip()
        outputEvents.append(outputEvent)
        counter = counter + 1
    # Puts all the event URLs in a list
    outputURLs = []
    counter = 0
    for link in links:
        href = link.get("href")
        if href.startswith("/events"):
            outputURL = baseURL + href
            outputURLs.append(outputURL)
        counter = counter + 1
    # Puts both the event names and URLs together into output
    length = len(outputEvents)
    for x in range(0, length - 1):
        eventName = outputEvents[x]
        eventURL = outputURLs[x]
        output = "=========================================================\n**" + eventName + "**\n" + eventURL
        await message.channel.send(output)


# Extracts from FaZe HLTV page and outputs roster
async def fazeRoster(message, fazeURL):
    output = "_**Current FaZe Roster:**_"
    response = requests.get(fazeURL)
    soup = BeautifulSoup(response.text, "html.parser")
    players = soup.findAll("a", class_="col-custom")
    for a in players:
        player = a.text
        player = player.strip()
        output = output + "\n" + player
    await message.channel.send(output)


# Extracts from HLTV Rankings page and outputs Top 30 Teams and takes input string for date
async def topTeams(message):
    output = "_**Current Top 30 Teams:**_\n"
    response = requests.get(rankingURL)
    soup = BeautifulSoup(response.text, "html.parser")
    teams = soup.findAll("div", class_="ranking-header")
    counter = 0
    for div in teams:
        teamName = teams[counter].find("span", class_="name")
        teamName = str(teamName)
        teamName = teamName.replace("<span class=\"name\">", "")
        teamName = teamName.replace("</span>", "")
        counter += 1
        if counter <= 5:
            teamName = "**" + teamName + "**"
        output = output + str(counter) + ". " + teamName + "\n"
    await message.channel.send(output)


# Extracts from HLTV Events page and outputs Events in this month
async def upcomingEvents(message):
    output = "_**Ongoing and Upcoming Events:**_\n"
    await message.channel.send(output)
    response = requests.get(eventsURL)
    soup = BeautifulSoup(response.text, "html.parser")
    event = soup.find("div", class_="events-month")
    links = event.findAll("")
    outputEvents = []
    for div in links:
        outputEvent = div.text
        outputEvent = outputEvent.strip()
        outputEvents.append(outputEvent)
    outputURLs = []
    for link in links:
        outputURL = link.text
        outputURL = outputURL.strip()
        outputURLs.append(outputURL)
    length = len(outputEvents)
    for x in range(0, length - 1):
        eventName = outputEvents[x]
        eventURL = outputURL[x]
        output = "=========================================================\n**" + eventName + "**\n" + eventURL
        await message.channel.send(output)


# Extracts from given team HLTV page and outputs events
async def teamEvents(message, input):
    output = "_**Ongoing and Upcoming Events:**_\n"
    await message.channel.send(output)
    input = input.replace("/events ", "")
    input = spaceUniform(input)
    oldInput = input
    input = teamSearch(input)
    oldInput = spaceReplace(oldInput)
    if (not validLink(oldInput, input)):
        await message.channel.send("Invalid Team Name or Not Top 30")
    else:
        response = requests.get(input)
        soup = BeautifulSoup(response.text, "html.parser")
        event = soup.find("div", class_="upcoming-events-holder")
        links = event.findAll("a")
        # Puts all the event names in a list
        outputEvents = []
        for div in event:
            outputEvent = div.text
            outputEvent = outputEvent.strip()
            outputEvents.append(outputEvent)
        # Puts all the event URLs in a list
        outputURLs = []
        for link in links:
            href = link.get("href")
            if href.startswith("/events"):
                outputURL = baseURL + href
                outputURLs.append(outputURL)
        # Puts both the event names and URLs together into output
        length = len(outputEvents)
        for x in range(0, length - 1):
            eventName = outputEvents[x]
            eventURL = outputURLs[x]
            output = "=========================================================\n**" + eventName + "**\n" + eventURL
            await message.channel.send(output)


# Extracts from given team HLTV page and outputs roster
async def teamRoster(message, input):
    input = input.replace("/roster ", "")
    input = spaceUniform(input)
    oldInput = input
    oldInput = spaceUniform(oldInput)
    output = "_**Current " + input + " Roster:**_"
    input = teamSearch(input)
    oldInput = spaceReplace(oldInput)
    if (not validLink(oldInput, input)):
        await message.channel.send("Invalid Team Name or Not Top 30")
    else:
        response = requests.get(input)
        soup = BeautifulSoup(response.text, "html.parser")
        players = soup.findAll("a", class_="col-custom")
        for a in players:
            player = a.text
            player = player.strip()
            output = output + "\n" + player
        await message.channel.send(output)


# Extracts from HLTV Rankings page and returns link to team page
def teamSearch(input):
    output = ""
    input = input.replace(" ", "-")
    response = requests.get(rankingURL)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.findAll("a")
    for link in links:
        href = link.get("href")
        href = str(href)
        if (href.find("/team/") >= 0 and href.find(input) >= 0):
            output = baseURL + href
    return output


# Removes all the extra spaces
def spaceUniform(input):
    input = input.strip()
    length = len(input)
    copyInput = input
    output = ""
    currChar = 0
    while currChar < length:
        if (input[currChar] == " "):
            copyInput = input[0:currChar]
            input = input.replace(input[0:currChar], "")
            input = input.strip()
            output = output + copyInput + " "
            currChar = 0
        length = len(input)
        currChar += 1
    output = output + input
    return output


# Returns true or false if the link is valid
def validLink(oldInput, input):
    # Checks if the URL is empty
    if (input == ""):
        return False

    # Checks if the end name of the URL is same length as input
    location = input.rindex("/") + 1
    start = 0
    if (len(oldInput) != len(input) - location):
        return False

    # Checks if the end name of the URL's characters are same as input
    while (input[location + start] == oldInput[start]
           and start < len(oldInput) - 1):
        start += 1
    if (start != len(oldInput) - 1):
        return False

    return True


# Replaces all ' ' with '-'
def spaceReplace(input):
    input = input.replace(" ", "-")
    return input
