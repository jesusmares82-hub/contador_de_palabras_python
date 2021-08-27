dictionary = {}

text = input("Ingresa el nombre del archivo: ")
try:
    with open(text, 'r') as f:
        text: str = f.read()
    words = text.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
except FileNotFoundError:
    print("El archivo que intentas abrir no existe!")
print(dictionary)
