class File:

    def __init__(self):
        self.file_name = ""
        self.text = ""

    def read_file_name(self):
        self.file_name = input("Enter the file name: ")

    def open_file(self):
        try:
            with open(self.file_name, 'r') as f:
                self.text: str = f.read()
            print(self.text)
        except FileNotFoundError as error:
            print(error)
            print("The file you are trying to open does not exist!")

    def unwanted_chars(self):
        unwanted = [',', '.', '¡', '!', '¿', '?', '(', ')', '"', "'"]
        for char in unwanted:
            self.text = self.text.replace(char, '')
        return text

    def get_words(self):
        self.text = self.unwanted_chars()
        words = self.text.lower().split()
        return words

    def get_dictionary(self):
        words = self.get_words()
        dictionary = {}
        for word in words:
            dictionary[word] = dictionary.get(word, 0) + 1
        return dictionary

    def repeat_words(self):
        tmp = list()
        dictionary = self.get_dictionary()
        for k, v in dictionary.items():
            tmp.append((v, k))
        tmp = sorted(tmp, reverse=True)
        return tmp

    def show_10_most_repeated(self):
        result = self.repeat_words()
        print("10 most repeated words: \n", result[:10])


my_file = File()
my_file.read_file_name()
my_file.open_file()
