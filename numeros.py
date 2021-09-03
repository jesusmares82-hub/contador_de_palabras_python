from entradas import EntradaUsuario


class CalcularNumeros(EntradaUsuario):

    def __init__(self, total=50):
        self.total = total
        super().__init__()

    def calcular(self):
        numeros = self.lista_ints()
        for i in range(len(numeros)):
            for j in range(len(numeros)):
                if i == j:
                    continue

                if (numeros[i] + numeros[j]) == self.total:
                    return i, j


if __name__ == '__main__':
    numeros = CalcularNumeros(total=100)
    numeros.leer_datos()
    resultado = numeros.calcular()
    print(resultado)
