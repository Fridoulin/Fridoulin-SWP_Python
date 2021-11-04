import random

while True:
    player = input("schere, stein, papier: ").lower()
    choice = ["schere", "stein", "papier"]
    computer = random.choice(choice)
    print("Spieler:", player)
    print("Computer:", computer)
    guess_index = {'schere': 0, 'stein': 1, 'papier': 2}
    guess_player = guess_index.get(player, 3)
    guess_computer = guess_index.get(computer)
    possible_results = [[0, 2, 1], [1, 0, 2], [2, 1, 0], [3, 3, 3]]
    result_compare = possible_results[guess_player][guess_computer]
    result_messages = ["Unentschieden", "Gewonnen", 'Verloren', 'Ungültige Eingabe']
    print(result_messages[result_compare])
    again = input("Nochmal [j/n]? ")
    if again != "j":
        break
