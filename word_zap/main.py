from player import Player
import sys
import itertools


def getUserInt(userInput):
    while True:
        num = input(userInput).strip()
        try:
            num = int(num)
            if num <= 0:
                pass
            else:
                break
        except:
            print("You can't convert that string to an int")
    return num


def getUserString(userInput):
    string = input(userInput).strip()
    return string


def getUserName(userInput):
    while True:
        string = input(userInput).strip()
        if len(string) > 0:
            break
        else:
            pass
    return string


def getPlayers():
    players = []

    numPlayers = getUserInt("How many players are there? ")

    for i in range(numPlayers):
        name = getUserName("What is player {0}'s name? ".format(i + 1))
        player = Player(name)
        players.append(player)

    return players


def checkWin(player):
    if len(player.getLetters()) == 0:
        print("{0} just won the game!".format(player.getName()))
        sys.exit()


def takeTurn(playersList):
    i = 0
    while True:

        player = playersList[i % len(playersList)]
        print("It is now {0}'s turn".format(player.getName()))
        print("Your letters are: {0}".format(player.printLetters()))
        word = getUserString("Enter a word to play or press enter to pass ")
        player.checkWord(word)
        checkWin(player)
        player.drawLetter()
        print("Your letters are now: {0}".format(player.printLetters()))
        print("")

        i += 1


def main():
    players = getPlayers()
    print("")
    print("Now we can play")
    print("")
    takeTurn(players)


if __name__ == '__main__':
    main()