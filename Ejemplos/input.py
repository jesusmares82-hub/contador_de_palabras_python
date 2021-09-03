class Input:
    tmp = []

    def read_data(self):
        text = ''
        while text != 'done':
            text = input("> ")
            if not text != 'done':
                continue
            self.tmp.append(text)

    def to_string_list(self):
        print(self.tmp)

    def to_int_list(self):
        try:
            tmp = list(map(int, self.tmp))
            print(tmp)
            return tmp
        except ValueError:
            print("No es una list de int")

    def revert(self):
        pass

    def calculate(self):
        pass


class ReverseText(Input):

    def __init__(self):
        super(ReverseText, self).__init__()

    def revert(self):
        print(self.tmp[::-1])


class CalculateNumbers(Input):

    def __init__(self):
        super(CalculateNumbers, self).__init__()

    def calculate(self):
        dif = {}
        nums = self.to_int_list()
        if nums is not None:
            for i, num in enumerate(nums):
                n = 50 - num
                if n not in dif:
                    dif[num] = i
                else:
                    print([dif[n], i])
        else:
            print("La list no es valid")


input_1 = ReverseText()
input_1.read_data()
"input_1.to_int_list()"
input_1.to_string_list()
input_1.revert()

"input_1 = CalculateNumbers()"
"input_1.read_data()"
"input_1.to_int_list()"
"input_1.calculate()"
