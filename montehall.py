from random import choice

def gameShow(initialChoice, stayOrSwitch, games):

    if games == 0: return 0

    carDoor = choice([1, 2, 3])

    goodChoice = initialChoice == carDoor
    winMessage = 'Winner'
    loseMessage = 'No Car!'

    if goodChoice and stayOrSwitch == 'stay':
        result = winMessage

    elif goodChoice and stayOrSwitch == 'switch':
        result = loseMessage

    elif not goodChoice and stayOrSwitch == 'switch':
        result = winMessage

    else:
        result = loseMessage

    print(result)

    if result == winMessage:
        return 1 + gameShow(initialChoice, stayOrSwitch, games-1)

    else:
        return 0 + gameShow(initialChoice, stayOrSwitch, games-1)


print(gameShow(2, 'switch', 10)/10)
