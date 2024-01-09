import os

# data
dic_fly = {'origin': None, 'destination': None, 'date': None,
           'condition': None, 'luggage': None, 'meal': None,
           'price': None, 'name': None, 'passport': None}

dic_keys = {'user': 'gonzalo', 'password': '1234'}

tabla_type_seat ="""\
+---+-----------------------+
| 1 | Primera Clase (1000$) |
+---+-----------------------+
| 2 | Economico (100$)      |
+---+-----------------------+\
"""
dic_countries = {'1': 'Turquia', '2': 'Grecia', '3': 'Libano', '4': 'España', '5': 'Portugal'}
countries = """\
+---+----------+
| 1 | Turquia   |
+---+----------+
| 2 | Grecia   |
+---+----------+
| 3 | Líbano   |
+---+----------+
| 4 | España   |
+---+----------+
| 5 | Portugal |
+---+----------+\
"""
type_meal = """\
+---+-------------+
| 1 | Regular     |
+---+-------------+
| 2 | Vegetariana |
+---+-------------+
| 3 | Kosher      |
+---+-------------+\
"""


# functions
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

def info_fly():

    while True:
        os.system("cls")
        print("Responde los siguientes preguntas para hacer una reserva:")
        print("-------------------------------------------------")
        print(countries)
        origin = input('Pais de salida: ')
        if origin in ['1', '2', '3', '4', '5']:
            dic_fly['origin'] = dic_countries[origin]
            break
        else:
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')
    while True:
        os.system("cls")
        print("Responde los siguientes preguntas para hacer una reserva:")
        print("-------------------------------------------------")
        print(countries)
        print(f"Salida: {dic_fly['origin']}")
        dest = input('País de destino: ')
        if dest in ['1', '2', '3', '4', '5']:
            if origin == dest:
                print('No puedes eleigr el mismo destino que país de llegada.')
                input('Pulsa enter para continuar.')
            else:
                dic_fly['destination'] = dic_countries[dest]
                break
        else:
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')

    dic_fly['date'] = input('Fecha de salida (dd/mm/yyyy): ')

    while True:
        os.system("cls")
        print("Responde los siguientes preguntas para hacer una reserva:")
        print("-------------------------------------------------")
        print(tabla_type_seat)
        seat = input('Que tipo de asiento quieres: ')
        if seat == '1':
            dic_fly['condition'] = 'Primera'
            dic_fly['price'] = 1000
            break
        elif seat == '2':
            dic_fly['condition'] = 'Economica'
            dic_fly['price'] = 100
            break
        else:
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')

    while True:
        os.system("cls")
        print("Responde los siguientes preguntas para hacer una reserva:")
        print("-------------------------------------------------")
        print('LLevar una maleta extra a parte de la de mano serian 100$.')
        luggage = input('Te gustaria facturar una maleta extra (Si/No): ')
        luggage = luggage.lower()
        if luggage == 'si' or luggage == 's':
            dic_fly['luggage'] = 'Maleta extra'
            dic_fly['price'] = dic_fly['price'] + 100
            break
        elif luggage == 'no' or luggage == 'n':
            dic_fly['luggage'] = 'Maleta solo de mano'
            break
        else:
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')

    while True:
        os.system("cls")
        print("Responde los siguientes preguntas para hacer una reserva:")
        print("-------------------------------------------------")
        print(type_meal)
        meal = input('Que tipo de comida quieres durante el vuelo: ')

        if meal == '1':
            dic_fly['meal'] = 'Regular'
            break
        elif meal == '2':
            dic_fly['meal'] = 'Vegetariana'
            break
        elif meal == '3':
            dic_fly['meal'] = 'Kosher'
            break
        else:
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')

    os.system("cls")
    print('Para terminar el proceso necesitamos una serie de datos personales.')
    print('------------------------------------------------------------------')
    dic_fly['name'] = input('Nombre y apellidos: ')
    dic_fly['passport'] = input('Número de pasaporte: ')


#  program

log_in()

while True:
    info_fly()
    os.system("cls")
    print(f"###### Información del vuelo ######\n"
          f"-------------------------------------\n"
          f"Nombre: {dic_fly['name']}\n"
          f"Passport: {dic_fly['passport']}\n"
          f"-------------------------------------\n"
          f"{dic_fly['origin']} ---> {dic_fly['destination']}\n"
          f"Fecha: {dic_fly['date']}\n"
          f"clase: {dic_fly['condition']}\n"
          f"Equipaje: {dic_fly['luggage']}\n"
          f"Comida: {dic_fly['meal']}\n"
          f"Precio: {dic_fly['price']}\n"
          f"-------------------------------------\n"
          f"-------------------------------------")

    while True:
        booking = input('Confirmar reserva (Si/No): ')
        booking = booking.lower()
        if booking == 'si':
            os.system("cls")
            print("Reserva lista. Gracias por su confianza en nuestros servicios.")
            exit()
        elif booking == 'no':
            break
        else:
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')




