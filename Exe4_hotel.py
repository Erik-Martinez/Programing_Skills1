import os
import pandas as pd

#data
df = pd.read_csv('data/hotel.csv', sep=";", encoding='windows-1252')
dic_keys = {'user': 'gonzalo', 'password': '1234'}


dic_countries = {'1': 'España', '2': 'Alemania', '3': 'Italia', '4': 'Francia', '5': 'Portugal'}
dic_rooms_price = {'1': 450, '2': 100, '3': 200, '4': 350, '5': 550}
dic_rooms_name = {'1': 'vip_suites', '2': 'single', '3': 'double', '4': 'group', '5': 'luxury'}
dic_user = {'name': None, 'surname': None, 'id': None}


menu_rooms = """\
    Añadir habitaciones   
+---+-------------+-------+
| 1 | VIP Suites  | 450 $ |
+---+-------------+-------+
| 2 | Single Room | 100 $ |
+---+-------------+-------+
| 3 | Double Room | 200 $ |
+---+-------------+-------+
| 4 | Group Room  | 350 $ |
+---+-------------+-------+
| 5 | Luxury Room | 550 $ |
+---+-------------+-------+
| 6 | Continuar           |
+---+---------------------+\
"""
menu_countries = """\
+---+----------+
| 1 | España   |
+---+----------+
| 2 | Alemania |
+---+----------+
| 3 | Italia   |
+---+----------+
| 4 | Francia  |
+---+----------+
| 5 | Portugal |
+---+----------+\
"""


#funtions
def log_in():
    attemps = 0
    while attemps < 3:
        print("Modo test: gonzalo - 1234")
        print('-------------------------')
        user = input("Nombre de usuario: ")
        if dic_keys['user'] == user:
            password = input("Contraseña: ")
            if dic_keys['password'] == password:
                os.system("cls")
                print('Claves aceptadas.')
                input('Pulsa enter para continuar.')
                return
            else:
                os.system("cls")
                attemps += 1
                print(f"La contraseña no es correcta.\n"
                      f"Te quedan {3 - attemps} intentos.")
                input('Pulsa enter para continuar.')


        else:
            os.system("cls")
            attemps += 1
            print(f"{user} no esta registrado en nuestro sistema.\n"
                  f"Te quedan {3-attemps} intentos.")
            input('Pulsa enter para continuar.')

    print('Has superado el numero de intentos maximos.')
    exit()

def select_hotel():
    price = 0

    while True:
        os.system('cls')
        print(menu_countries)
        country = input('Número del país en el que quieres reservar: ')

        if country in  ['1', '2', '3', '4', '5']:
            while True:
                country = dic_countries[country]
                ite_country = list(df[(df['country'] == country)].loc[:, 'city'])
                num_list = 0
                os.system('cls')
                for x in ite_country:
                    num_list += 1
                    print(f'{num_list}.{x}')

                city = input('Número de la ciudad en la que quieres reservar: ')
                if city in ['1', '2', '3']:
                    city = ite_country[int(city)-1]

                    while True:
                        os.system('cls')
                        print(menu_rooms)
                        type_room = input('Número del tipo de habitaciones: ')

                        if type_room in ['1','2','3','4','5']:
                            t = df[df['city'] == city].loc[:, dic_rooms_name[type_room]]
                            if int(t.iloc[0]) > 0:
                                df.loc[df['city'] == city, dic_rooms_name[type_room]] = t-1
                                nights = input('Cuantas noches quieres quieres reservar: ')
                                price += dic_rooms_price[type_room]*int(nights)
                            else:
                                os.system('cls')
                                print('No nos quedan de estas habitaciones.')
                                input('Pulsa enter para continuar.')
                        elif type_room == '6':
                            return price
                        else:
                            os.system('cls')
                            print('No he entendido tu respuesta')
                            input('Pulsa enter para continuar.')

                else:
                    os.system('cls')
                    print('No he entendido tu respuesta')
                    input('Pulsa enter para continuar.')
        else:
            os.system('cls')
            print('No he entendido tu respuesta')
            input('Pulsa enter para continuar.')

def user_data():
    os.system('cls')
    print('Rellena los siguientes datos:')
    print('-----------------------------')
    dic_user['name'] = input('Nombre: ')
    dic_user['surname'] = input('Apellido: ')
    dic_user['id'] = input('ID/passport: ')

log_in()

while True:
    price = select_hotel()
    user_data()
    while True:
        os.system('cls')
        print(f'El preció de tus reservas seria de {price}$.')
        answer = input('Quieres confirmar la reserva (Si/No): ')
        answer = answer.lower()
        if answer == 'si' or answer == 's':
            os.system('cls')
            print('Reserva confimada!\nGracias por confiar en nuestros hoteles.')
            exit()
        elif answer == 'no' or answer == 'n':
            break
        else:
            os.system('cls')
            print('No he entendido tu respuesta')
            input('Pulsa enter para continuar.')






