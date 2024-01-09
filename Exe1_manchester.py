import csv
import os

def player_review(player, con=True):
    print("-------------------------------------------")
    print(f"Nombre: {player['name']}\n"
          f"Número de goles: {player['goals']}\n"
          f"Puntos en velocidad: {player['speed']}\n"
          f"Puntos en asistencia: {player['assists']}\n"
          f"Puntos en pases: {player['passing']}\n"
          f"Puntos en defensa: {player['defensive']}")
    print("-------------------------------------------")
    if con == True:
        input("Pulsa enter para continuar.")

def select_player(type_skill, number):

    with open("data/manchester_players.csv") as File:
        reader = csv.DictReader(File)
        points = 0
        if number == None:
            for row in reader:
                if int(row[type_skill]) > points:
                    points = int(row[type_skill])
                    player_info = row
            return player_info
        else:
            for row in reader:
                if int(row[type_skill]) == number:
                    return row

            print("Ese número no coincide con ningun jugador registrado.")


start = """###### Manchester United FC APP ######"""
ask_jersey = """Numero de camiseta: """

menu = """\
+---+----------------------------+
| 1 | Información de un jugardor |
+---+----------------------------+
| 2 | Comparar dos jugaodres     |
+---+----------------------------+
| 3 | Jugador por caracteristica |
+---+----------------------------+
| S | Cerrar                     |
+---+----------------------------+\
"""
menu_skills = """\
+---+---------------------+
| 1 | Mejor goleador      |
+---+---------------------+
| 2 | Mejor en velocidad  |
+---+---------------------+
| 3 | Mejor en asistencia |
+---+---------------------+
| 4 | Mejor en pases      |
+---+---------------------+
| 5 | Mejor en defensa    |
+---+---------------------+
| S | Volver al menú      |
+---+---------------------+\
"""

on = True

while on == True:
    os.system("cls")
    print(start)
    print(menu)
    selector = input("Seleciona una opción: ").lower()

    if selector == '1':
        os.system("cls")
        print(start)
        number = int(input(ask_jersey))
        player = select_player('number_jersey', number)
        os.system("cls")
        player_review(player)
    elif selector == '2':
        os.system("cls")
        print(start)
        print("Jugagor 1")
        number = int(input(ask_jersey))
        player1 = select_player('number_jersey', number)
        print("Jugagor 2")
        number = int(input(ask_jersey))
        player2 = select_player('number_jersey', number)
        os.system("cls")
        player_review(player1, con=False)
        player_review(player2)
    elif selector == '3':
        while True:
            os.system("cls")
            print(menu_skills)
            selector = input("Seleciona una opción:").lower()

            if selector == '1':
                os.system("cls")
                player = select_player('goals', None)
                player_review(player)
            elif selector == '2':
                os.system("cls")
                player = select_player('speed', None)
                player_review(player)
            elif selector == '3':
                os.system("cls")
                player = select_player('assists', None)
                player_review(player)
            elif selector == '4':
                os.system("cls")
                player = select_player('passing', None)
                player_review(player)
            elif selector == '5':
                os.system("cls")
                player = select_player('defensive', None)
                player_review(player)
            elif selector == 's':
                break
            else:
                os.system("cls")
                print("No he entidido tu respuesta")
                input("Pulsa intro para continuar.")
    elif selector == 's':
        exit()
    else:
        os.system("cls")
        print("No he entidido tu respuesta")
        input("Pulsa intro para continuar.")
