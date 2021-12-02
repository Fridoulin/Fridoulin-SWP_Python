import random
import DB



def inputUser(valuableList):
    global userChoice
    userChoice = input("Rock, Paper, Scissors, Lizard, Spock: ").lower()
    if userChoice in valuableList:
        print("Your Choice: ", userChoice)
        return userChoice
    else:
        print("Try again")
        print(userChoice)
        return inputUser(valuableList)


def inputComputer(valuableList):
    choice = random.choice(valuableList)
    print("Computers choice: ", choice)
    return choice


def check(choiceUser, choiceComputer):
    guessToIndex = {"rock": 0, "spock": 1, "paper": 2, "lizard": 3, "scissors": 4}
    user = guessToIndex.get(choiceUser)
    pc = guessToIndex.get(choiceComputer)
    index = (user - pc) % 5
    return index


def winner(result):
    global score
    if result == 0:
        score = "Draw"
        print("Draw")
    elif result == 1 or result == 2:
        score = "Won"
        print("Won")
    elif result > 2:
        score = "Lost"
        print("Lost")
    print("\n")


def main():
    valuableList = ["rock", "spock", "paper", "lizard", "scissors"]
    choiceUser = inputUser(valuableList)
    choiceComputer = inputComputer(valuableList)
    result = check(choiceUser, choiceComputer)
    winner(result)
    db()


def again():
    again = input("Try again[y,n]: ").lower()
    if (again == "y"):
        return True
    elif (again == "n"):
        return False
    else:
        again()

def db():
    DB.database(userChoice, score)
    DB.select()

while True:
    if __name__ == "__main__":
        main()
    if again() == False:
        break
