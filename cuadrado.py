from poligono import Poligono


class Cuadrado(Poligono):

    def __init__(self):
        super(Cuadrado, self).__init__(1)

    def obtener_lado(self):
        return self.lados[0]

    def area(self):
        return float(self.obtener_lado() **2)

    def perimetro(self):
        return float(self.obtener_lado() * 4)


if __name__ == '__main__':
    cuadrado = Cuadrado()
    cuadrado.leer_lados()
    print("El area del cuadrado es: ", cuadrado.area())
    print("El area del cuadrado es: ", cuadrado.perimetro())
