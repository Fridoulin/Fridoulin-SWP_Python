import random

while True:
    choice = ["schere", "stein", "papier"]
    pc = random.choice(choice)
    player = None
    player = input("schere, stein, papier: ").lower()
    if player == pc:
        print("Computer: ", pc, "   Spieler: ", player)
        print("Unentschieden!")
    elif player == "schere":
        if pc == "papier":
            print("Computer: ", pc, "   Spieler: ", player)
            print("Gewonnen!")
        if pc == "stein":
            print("Computer: ", pc, "   Spieler: ", player)
            print("Verloren!")
    elif player == "stein":
        if pc == "schere":
            print("Computer: ", pc, "   Spieler: ", player)
            print("Gewonnen!")
        if pc == "papier":
            print("Computer: ", pc, "   Spieler: ", player)
            print("Verloren!")
    elif player == "papier":
        if pc == "stein":
            print("Computer: ", pc, "   Spieler: ", player)
            print("Gewonnen!")
        if pc == "schere":
            print("Computer: ", pc, "   Spieler: ", player)
            print("Verloren!")
    again = input("Nochmal [j/n]? ")
    if again != "j":
        break

