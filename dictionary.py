words = ['perro', 'gato', 'leon', 'oso', 'gato', 'buho', 'leon', 'oso', 'leon']

dictionary = {}

for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1
print(dictionary)
