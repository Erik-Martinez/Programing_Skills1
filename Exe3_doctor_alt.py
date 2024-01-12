import os
import pandas as pd

#data

## dic
df = pd.read_csv('data/doctors.csv', sep=";", encoding='windows-1252')

dic_keys = {'user': 'gonzalo', 'password': '1234'}

dic_specialty = {'1': 'medicina general', '2': 'urgencias', '3': 'analisis clinico',
                    '4': 'cardiologia', '5': 'neurologia', '6': 'nutricion',
                    '7': 'fisioterapia', '8': 'traumatologia', '9': 'medicina interna'}
list_appo = []
## menus
menu_spe = """\
+---+------------------+
| 1 | Medicina general |
+---+------------------+
| 2 | Urgencias        |
+---+------------------+
| 3 | Análisis Clínico |
+---+------------------+
| 4 | Neurología       |
+---+------------------+
| 5 | Nutrición        |
+---+------------------+
| 6 | Fisioterapia     |
+---+------------------+
| 7 | Traumatología    |
+---+------------------+
| 8 | Medicina Interna |
+---+------------------+
| S | Salir            |
+---+------------------+\
"""

menu_hor ="""\
+---+------------------+
| 1 | Mañana           |
+---+------------------+
| 2 | Tarde            |
+---+------------------+\
"""

menu_mor = """\
+---+-------+----+-------+
| 1 | 9:00  | 8  | 12:10 |
+---+-------+----+-------+
| 2 | 9:20  | 9  | 12:20 |
+---+-------+----+-------+
| 3 | 10:00 | 10 | 12:40 |
+---+-------+----+-------+
| 4 | 10:40 | 11 | 13:00 |
+---+-------+----+-------+
| 5 | 11:00 | 12 | 13:20 |
+---+-------+----+-------+
| 6 | 11:30 | 13 | 13:45 |
+---+-------+----+-------+
| 7 | 12:00 | 14 | 13:55 |
+---+-------+----+-------+\
"""

menu_after = """\
+---+-------+----+-------+
| 1 | 14:00 | 8  | 17:30 |
+---+-------+----+-------+
| 2 | 14:30 | 9  | 18:00 |
+---+-------+----+-------+
| 3 | 15:00 | 10 | 18:30 |
+---+-------+----+-------+
| 4 | 15:30 | 11 | 19:00 |
+---+-------+----+-------+
| 5 | 16:00 | 12 | 19:30 |
+---+-------+----+-------+
| 6 | 16:30 | 13 | 20:00 |
+---+-------+----+-------+
| 7 | 17:00 | 14 | 20:30 |
+---+-------+----+-------+\
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

def select_appo():

    while True:
        os.system('cls')

        print('##### Nueva cita #####')
        print(menu_spe)
        selector = input('Seleciona la especialidad:')
        selector = selector.lower()

        if selector in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if selector not in list_appo:
                while True:
                    os.system('cls')

                    print(menu_hor)
                    selector_hour = input('Seleciona horario preferente:')

                    if selector_hour not in ['1', '2']:
                        os.system('cls')
                        print('No he entendido tu respuesta')
                        input('Pulsa enter para continuar.')

                    else:
                        list_appo.append(selector)
                        ava_spe = df[(df['specialty'] == int(selector)) & (df['hour'] == int(selector_hour))]
                        return ava_spe, selector_hour
            else:
                os.system('cls')
                print('No puedes pedir una cita en una especialidad en la que ya tienes cita.')
                input('Pulsa enter para continuar.')



        elif selector == 's':
            exit()
        else:
            os.system('cls')
            print('No he entendido tu respuesta')
            input('Pulsa enter para continuar.')

def select_doctor(ava_spe, selector_hour):
    while True:
        os.system('cls')
        num = 1
        for x in ava_spe.loc[:, 'name']:
            print(f'{num}.{x}')
            num += 1
        selector = input('Seleciona el número del doctor por el que quieres ser atendido: ')
        os.system('cls')
        if selector in ['1', '2', '3']:
            if selector_hour == '1':
                print(menu_mor)
                input('Seleciona la hora que prefieras: ')

                os.system('cls')
                print('Tu cita esta registrada.')
                input('Pulsa enter para continuar.')
                return
            elif selector_hour == '2':
                print(menu_after)
                input('Seleciona la hora que prefieras: ')

                os.system('cls')
                print('Tu cita esta registrada.')
                input('Pulsa enter para continuar.')
                return
        else:
            os.system('cls')
            print('No he entendido tu respuesta')
            input('Pulsa enter para continuar.')

#code
log_in()

while True:
    ava_spe, selector_hour = select_appo()
    select_doctor(ava_spe, selector_hour)


