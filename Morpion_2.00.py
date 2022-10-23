#  Copyright (c) 2022. Code by Dimitri AIGLE
import random
from time import sleep

print(f"""
        ****************************************
        N O U V E L L E   P A R T I E  Morpion

                By Dimitri AIGLE
        ****************************************
        """)
game = {
    "current player": "player",
    "player 1": {
                            "name": "P1",
                            "win": 0
        },
    "player 2": {
                            "name": "P2",
                            "win": 0
        },

}
game["player 1"]['name'] = input("Entrez le nom du joueur 1 : ")
valide = input(f"Le nom du joueur 1 est : {game['player 1']['name']} ? (y/n) ")
while "n" in valide:
    game["player 1"]['name'] = input("Entrez le nom du joueur 1 : ")
    valide = input(f"Le nom du joueur 1 est : {game['player 1']['name']} ? (y/n) ")

game["player 2"]['name'] = input("Entrez le nom du joueur 2 : ")
valide2 = input(f"Le nom du joueur 2 est : {game['player 2']['name']} ? (y/n) ")
while "n" in valide2:
    game["player 2"]['name'] = input("Entrez le nom du joueur 2 : ")
    valide = input(f"Le nom du joueur 2 est : {game['player 2']['name']} ? (y/n) ")

joueur = random.randint(0, 2)
if joueur == 0:
    game["current player"] = game["player 1"]['name']
else:
    game["current player"] = game["player 2"]['name']
in_game = True
while in_game:

    map_game = [
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
    ]

    def draw():
        # clear()
        for i in range(3):
            print("-------------------")
            for j in range(3):
                print("|", end="")
                print(f" {map_game[i][j]} ", end="")
            print("|", end="")
            print("")
        print("-" * len("| ⭕ | ⭕ | ⭕ |"))
        if game["current player"] == game["player 1"]['name']:
            print(f"Tour du joueur : {game['current player']} (⭕)")
        else:
            print(f"Tour du joueur : {game['current player']} (❌)")

    def check_win():
        for i in range(3):
            if map_game[i][0] == map_game[i][1] == map_game[i][2] != '   ' or map_game[0][i] == map_game[1][i] == map_game[2][i] != '   ' or map_game[0][0] == map_game[1][1] == map_game[2][2] != '   ' or map_game[0][2] == map_game[1][1] == map_game[2][0] != '   ':
                return True


    def check_draw():
        check = True
        for i in range(3):
            for j in range(3):
                if map_game[i][j] == '   ':
                    check = False
        return check

    def replay():
        texte = " " + game["player 1"]['name'] + " | " + game["player 2"]['name']
        print("-" * (len(texte) + 1))
        print(texte)
        print("-" * (len(texte) + 1))
        print(" " * (len(" " + game["player 1"]['name'] + " ") // 2) + str(game["player 1"]['win'])
              + " " * (len(" " + game["player 1"]['name'] + " ") // 2) + "|"
              + " " * (len(" " + game["player 2"]['name'] + " ") // 2) + str(game["player 2"]['win']))
        print("-" * (len(texte) + 1))
        re = input("Voulez vous rejouez ? (Yes/No)")
        if re in ["No", "no", "n"]:
            global in_game
            in_game = False
        else:
            print(f"""
                    ****************************************
                    N O U V E L L E   P A R T I E  Morpion

                            By Dimitri AIGLE
                    {game['player 1']['name']} win : {game['player 1']['win']} | {game['player 2']['name']} win : {game['player 2']['win']}
                    ****************************************
                    """)

    while True:
        draw()
        a = int(input('Quel case voulez vous cochez ? [1-9] : '))
        if a in {'exit', 'quit', 'q', 'quitter'}:
            break
        if str(a).isdigit() and 0 < int(a) < 10:
            a = int(a)
            row, col = divmod(a - 1, 3)

            if a in {'exit', 'quit', 'q', 'quitter'}:
                break
            if map_game[row][col] == '   ':
                map_game[row][col] = "⭕" if game["current player"] == game["player 1"]["name"] else "❌"
                draw()
                if check_win():
                    print(f" {game['current player']} a gagné 🏆")
                    if game['current player'] == game["player 2"]["name"]:
                        game["player 2"]["win"] += 1
                    else:
                        game["player 1"]["win"] += 1
                    break
                if check_draw():
                    print("⛔ égalité !")
                    break
                if game["current player"] == game["player 2"]["name"]:
                    game["current player"] = game["player 1"]["name"]
                else :
                    game["current player"] = game["player 2"]["name"]
            else:
                print("⛔ Case déja rempli! rejouez ! ⛔")
                sleep(3)

    replay()