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

game["player 2"]['name'] = input("Entrez le nom du joueur 2 : ")
valide2 = input(f"Le nom du joueur 2 est : {game['player 2']['name']} ? (y/n) ")
while "n" in valide2:
    game["player 2"]['name'] = input("Entrez le nom du joueur 2 : ")

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


    # def clear():
    #     # for windows
    #     system('cls' if name == 'nt' else 'clear')
    #     print("\n")

    def draw():
        # clear()
        for i in range(3):
            print("-------------------")
            for j in range(3):
                print("|", end="")
                print(f" {map_game[i][j]} ", end="")
            print("|", end="")
            print("")
        print("-------------------")
        if game["current player"] == game["player 1"]['name']:
            print(f"Tour du joueur : {game['current player']} (⭕)")
        else:
            print(f"Tour du joueur : {game['current player']} (❌)")

    def replay():
        texte = " "+ game["player 1"]['name'] + " | " + game["player 2"]['name']
        print("-"*(len(texte)+1))
        print(texte)
        print("-" * (len(texte)+1))
        print(" "* (len(" "+ game["player 1"]['name'] + " ")//2)+ str(game["player 1"]['win']) +" "* (len(" "+ game["player 1"]['name'] + " ")//2) + "|"+" "* (len(" "+ game["player 2"]['name'] + " ")//2) + str(game["player 2"]['win']))
        print("-" * (len(texte)+1))
        re = input("Voulez vous rejouez ? (Yes/No)")
        if re in ["No","no","n"] :
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


    def gagne():
        for i in range(3):
            if map_game[i][0] == map_game[i][1] == map_game[i][2] != '   ':
                if map_game[i][0] == "⭕":
                    print(f"{game['player 1']['name']} vous avez Gagné ! 🏆")
                    game['player 1']['win'] = game['player 1']['win'] + 1
                else:
                    print(f"{game['player 2']['name']} vous avez Gagné ! 🏆")
                    game['player 2']['win'] = game['player 2']['win'] + 1
                return True

            elif map_game[0][i] == map_game[1][i] == map_game[2][i] != '   ':
                if map_game[0][i] == "⭕":
                    print(f"{game['player 1']['name']} vous avez Gagné ! 🏆")
                    game['player 1']['win'] = game['player 1']['win'] + 1
                else:
                    print(f"{game['player 2']['name']} vous avez Gagné ! 🏆")
                    game['player 2']['win'] = game['player 2']['win'] + 1
                return True
            if map_game[0][0] == map_game[1][1] == map_game[2][2] != '   ':
                if map_game[0][0] == "⭕":
                    print(f"{game['player 1']['name']} vous avez Gagné ! 🏆")
                    game['player 1']['win'] = game['player 1']['win'] + 1
                else:
                    print(f"{game['player 2']['name']} vous avez Gagné ! 🏆")
                    game['player 2']['win'] = game['player 2']['win'] + 1
                return True
            elif map_game[0][2] == map_game[1][1] == map_game[2][0] != '   ':
                if map_game[0][2] == "⭕":
                    print(f"{game['player 1']['name']} vous avez Gagné ! 🏆")
                    game['player 1']['win'] = game['player 1']['win'] + 1
                else:
                    print(f"{game['player 2']['name']} vous avez Gagné ! 🏆")
                    game['player 2']['win'] = game['player 2']['win'] + 1
                return True
    while True:
        a = 0
        draw()
        while a == 0 or a < 0 or a > 9:
            a = int(input('Quel case voulez vous cochez ? [1-9] : '))

        if a < 4:
            a -= 1
            if game["current player"] == game["player 1"]['name'] and map_game[0][a] != "❌" and map_game[0][a] != "⭕":
                map_game[0][a] = "⭕"
                if gagne() :
                    break
                game["current player"] = game["player 2"]['name']
            elif map_game[0][a] != "❌" and map_game[0][a] != "⭕":
                map_game[0][a] = "❌"
                if gagne() :
                    break
                game["current player"] = game["player 1"]['name']
            else:
                print("⛔ Case déja rempli! rejouez ! ⛔")
                sleep(5)
        elif a < 7:
            a -= 4
            if game["current player"] == game["player 1"]['name'] and map_game[1][a] != "❌" and map_game[1][a] != "⭕":
                map_game[1][a] = "⭕"
                if gagne() :
                    break
                game["current player"] = game["player 2"]['name']
            elif map_game[1][a] != "❌" and map_game[1][a] != "⭕":
                map_game[1][a] = "❌"
                if gagne() :
                    break
                game["current player"] = game["player 1"]['name']
            else:
                print("⛔ Case déja rempli! rejouez ! ⛔")
                sleep(5)
        elif a < 10:
            a -= 7
            if game["current player"] == game["player 1"]['name'] and map_game[2][a] != "❌" and map_game[2][a] != "⭕":
                map_game[2][a] = "⭕"
                if gagne() :
                    break
                game["current player"] = game["player 2"]['name']
            elif map_game[2][a] != "❌" and map_game[2][a] != "⭕":
                map_game[2][a] = "❌"
                if gagne():
                    break

                game["current player"] = game["player 1"]['name']
            else:
                print("⛔ Case déja rempli! rejouez ! ⛔")
                sleep(3)

    replay()