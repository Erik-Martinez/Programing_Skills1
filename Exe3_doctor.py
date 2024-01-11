import os

# data
dic_doctors = {
    'doctor1': {
        'name': 'Federico Loverte',
        'specialty': '1',
        'avaliable': '1',
    },
    'doctor2': {
        'name': 'Matilde Socia',
        'specialty': '1',
        'avaliable': '2',
    },
    'doctor3': {
        'name': 'Lucia Nato',
        'specialty': '1',
        'avaliable': '1',
    },
    'doctor4': {
        'name': 'Triana Luca',
        'specialty': '2',
        'avaliable': '1',
    },
    'doctor5': {
        'name': 'Milo Santoro',
        'specialty': '2',
        'avaliable': '2',
    },
    'doctor6': {
        'name': 'Valentina Rossi',
        'specialty': '2',
        'avaliable': '2',
    },
    'doctor7': {
        'name': 'Gabriel Mancini',
        'specialty': '3',
        'avaliable': '1',
    },
    'doctor8': {
        'name': 'Isabella Conti',
        'specialty': '3',
        'avaliable': '2',
    },
    'doctor9': {
        'name': 'Alessandro Ferro',
        'specialty': '3',
        'avaliable': '2',
    },
    'doctor10': {
        'name': 'Camila Romano',
        'specialty': '4',
        'avaliable': '1',
    },
    'doctor11': {
        'name': 'Giovanni Pellegrino',
        'specialty': '4',
        'avaliable': '2',
    },
    'doctor12': {
        'name': 'Mia Barbieri',
        'specialty': '4',
        'avaliable': '1',
    },
    'doctor13': {
        'name': 'Lorenzo Cattaneo',
        'specialty': '5',
        'avaliable': '1',
    },
    'doctor14': {
        'name': 'Sophia Russo',
        'specialty': '5',
        'avaliable': '2',
    },
    'doctor15': {
        'name': 'Diego Martini',
        'specialty': '5',
        'avaliable': '1',
    },
    'doctor16': {
        'name': 'Emma Morelli',
        'specialty': '6',
        'avaliable': '1',
    },
    'doctor17': {
        'name': 'Luca Ferrari',
        'specialty': '6',
        'avaliable': '2',
    },
    'doctor18': {
        'name': 'Aria Bianchi',
        'specialty': '6',
        'avaliable': '1',
    },
    'doctor19': {
        'name': 'Liam De Santis',
        'specialty': '7',
        'avaliable': '1',
    },
    'doctor20': {
        'name': 'Elena Lombardi',
        'specialty': '7',
        'avaliable': '2',
    },
    'doctor21': {
        'name': 'Nicolas Rizzo',
        'specialty': '7',
        'avaliable': '2',
    },
    'doctor22': {
        'name': 'Olivia Gentile',
        'specialty': '8',
        'avaliable': '1',
    },
    'doctor23': {
        'name': 'Marco Leone',
        'specialty': '8',
        'avaliable': '2',
    },
    'doctor24': {
        'name': 'Sofia Piazza',
        'specialty': '8',
        'avaliable': '2',
    },
}

dic_specialities = {'1': 'medicina general', '2': 'urgencias', '3': 'analisis clinico',
                    '4': 'neurologia', '5': 'nutricion', '6': 'fisioterapia',
                    '7': 'traumatologia', '8': 'medicina interna'}

dic_sche = {'1': 'mañana', '2': 'tarde'}


dic_user = {
    'appo1': {
        'doctor': None,
        'specialty': None,
        'hour': None,
    },
    'appo2': {
        'doctor': None,
        'specialty': None,
        'hour': None,
    },
    'appo3': {
        'doctor': None,
        'specialty': None,
        'hour': None,
    },
}


diccionario = {}

for fila in tabla:
    diccionario[str(fila[0])] = fila[1]
    diccionario[str(fila[2])] = fila[3]

print(diccionario)



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
menu_


#funtions

def selecet_spe():

    os.system('cls')

    print(menu_spe)
    selector = input('Seleciona la especialidad:')

    ava_doc = []

    if selector in list(dic_specialities.keys()):
        for x in dic_doctors.values():
            if selector == x['specialty']:
                ava_doc.append(x)
        return ava_doc

    elif selector == 's':

        return


    else:
        os.system('cls')
        print('No he entendido tu respuesta')
        input('Pulsa enter para continuar.')

def select_hour(ava_doc):
    os.system('cls')

    print(menu_spe)
    selector = input('Seleciona tu horario preferente: ')



ava_doc = []
for x in dic_doctors.values():
    if '2' == x['specialty']:
        ava_doc.append(x)
print(ava_doc[1].get('name'))

ava_doc = selecet_spe()
print(lisa)