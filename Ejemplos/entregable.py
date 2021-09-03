def unwanted_chars(my_text):
    unwanted = [',', '.', '¡', '!', '¿', '?', '(', ')', '"', "'"]
    for char in unwanted:
        my_text = my_text.replace(char, '')
    return my_text


def get_words(my_text):
    my_text = unwanted_chars(my_text)
    words = my_text.lower().split()
    return words


def get_dictionary(my_text):
    words = get_words(my_text)
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary


def repeat_words(my_text):
    tmp = list()
    dictionary = get_dictionary(my_text)
    for k, v in dictionary.items():
        tmp.append((v, k))
    tmp = sorted(tmp, reverse=True)
    return tmp


def show_10_most_repeated(my_text):
    result = repeat_words(my_text)
    print("10 most repeated words: \n", result[:10])


flag = 'error'

while flag == 'error':
    text = input("Enter the file name: ")
    try:
        with open(text, 'r') as f:
            text: str = f.read()
            show_10_most_repeated(text)
        flag = 'done'
        break
    except FileNotFoundError as error:
        print(error)
        print("The file you are trying to open does not exist!")
