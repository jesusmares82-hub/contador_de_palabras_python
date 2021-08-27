dictionary = {}
flag = 'error'

while flag == 'error':
    text = input("Enter the file name: ")
    try:
        with open(text, 'r') as f:
            text: str = f.read()
        words = text.lower().split()
        for word in words:
            dictionary[word] = dictionary.get(word, 0) + 1
        flag = 'done'
        break
    except FileNotFoundError:
        print("The file you are trying to open does not exist!")
tmp = list()
for k, v in dictionary.items():
    tmp.append((v, k))
tmp = sorted(tmp, reverse=True)
print("10 most repeated words: \n", tmp[:10])
