def lines(filename, find):
    count_lines = 0
    for line in filename:
        if not len(line) > 1:
            continue
        if find not in line:
            continue
        print(line.strip())
        count_lines += 1
    return count_lines


file = input("Ingresa el nombre del archivo:")
word = input("Ingresa la palabra a buscar:")
try:
    file = open(file, mode='r')
    count = lines(file, word)
    if count != 0:
        print("El archivo tiene la palabra", word, "en", count, "lineas")
    else:
        print("No se encontró la palabra")
except FileNotFoundError as error:
    print("El archivo no existe.❗️")
