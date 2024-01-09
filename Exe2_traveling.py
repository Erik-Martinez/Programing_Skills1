import csv
import os
import sys

with open("data/opc_activities.csv") as File:
    reader = csv.DictReader(File, delimiter=';')

    while True:

        print("Soy su sistema de ayuda para viajes.")
        money = input("Seleciona tu presupuesto maximo: ")

        money = int(money)

        if money < 100:
            os.system("cls")
            print("Con ese presupuesto no podemos ofrecerte ningún viaje.")

        elif  money >= 100:
            os.system("cls")
            print("Con este presupuesto te puedes permitir viajar en:")
            ava_season = []

            # Options avaliable for bugedt
            while True:
                File.seek(0)
                for row in reader:
                    if int(row['money']) <= money:
                        if row['season'] not in ava_season:
                            ava_season.append(row['season'])
                            print(row['season'])

                File.seek(0)

                #options avaliable for activities

                print("-----------------------------------------------------")
                select_season = input("En que estación de las disponibles te gustaria viajar: ")
                select_season = select_season.lower()

                os.system("cls")

                if select_season in ava_season:
                    while True:
                        ava_activities = []
                        ava_places = []
                        num_act = 0
                        print("-------------------------------------------------------------")
                        for row in reader:
                            if row['season'] == select_season:
                                num_act += 1
                                print(f"{num_act}.{row['activity']}")
                                ava_activities.append(row['activity'])
                                ava_places.append(row['place'])

                                if row['activity2'] != 'None':
                                    num_act += 1
                                    print(f"{num_act}.{row['activity2']}")
                                    ava_activities.append(row['activity2'])
                                    ava_places.append(row['place'])

                        print("-------------------------------------------------------------")
                        print("Cual de las anteriores actividades es la que mas te interesa?")
                        select_act = input("Seleciona el número correspondiente: ")

                        if int(select_act) in range(1, num_act):
                            select_act = int(select_act) - 1
                            os.system("cls")
                            print(f"Nuestro super-ordenador recomienda para ti:\n"
                                  f"{ava_places[select_act]}")
                            exit()
                        else:
                            os.system("cls")
                            print("No entendi tu respuesta.")
                            input("Pulsa enter para continuar")


                elif select_season in ["primavera", 'otoño', 'invierno', 'verano'] and select_season not in ava_season:
                    print("No puedes viajar en esa estación con un presupuesto tan bajo.")
                    input("Pulsa enter para continuar")

                else:
                    print("No entendi tu respuesta.")
                    input("Pulsa enter para continuar")

        print("No entendi tu respuesta.")
        input("Pulsa enter para continuar")




def options_season(money_destination):

    with open('data/opc_activities.csv') as File:
        reader = csv.DictReader(File, delimiter=';')



money_destination = options_money(300)
