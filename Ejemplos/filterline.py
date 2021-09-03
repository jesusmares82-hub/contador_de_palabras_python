text = input("Ingresa el nombre del archivo: ")

try:
    file = open(text, mode='r')
    for linea in file:
        if not linea.startswith('From:'):
            continue
        if 'uct.ac.za' not in linea:
            continue
        print(linea.strip())
except FileNotFoundError:
    print("El archivo no existe.❗️")
