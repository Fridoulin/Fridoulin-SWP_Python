import random


def inputUser(valuableList):
    choice = input("Rock, Paper, Scissors, Lizard, Spock: ").lower()
    if choice in valuableList:
        print("Your Choice: ", choice)
        return choice
    else:
        print("Try again")
        main()


def inputComputer(valuableList):
    choice = random.choice(valuableList)
    print("Computers choice: ", choice)
    return choice


def check(choiceUser, choiceComputer):
    guessToIndex = {"rock": 0, "spock": 1, "paper": 2, "lizard": 3, "scissors": 4}
    user = guessToIndex.get(choiceUser)
    pc = guessToIndex.get(choiceComputer)
    return (user - pc) % 5


def winner(result):
    if result == 0:
        print("Draw")
    elif result == 1 or result == 2:
        print("Won")
    elif result > 2:
        print("Lost")
    print("\n")


def main():
    valuableList = ["rock", "spock", "paper", "lizard", "scissors"]
    choiceUser = inputUser(valuableList)
    choiceComputer = inputComputer(valuableList)
    result = check(choiceUser, choiceComputer)
    winner(result)


while True:
    if __name__ == "__main__":
        main()

    again = input("Try again [y,n]? ")
    if again == "n":
        break
