from poligono import Poligono


class Triangulo(Poligono):
    """
    Definir un traingulo equilatero.
    """

    def __init__(self):
        super(Triangulo, self).__init__(1)

    def obtener_lado(self):
        return self.lados[0]

    def area(self):
        return (self.obtener_lado() ** 2) * 0.4333

    def perimetro(self):
        return self.obtener_lado() * 3


if __name__ == '__main__':
    triangulo = Triangulo()
    triangulo.leer_lados()
    print("El area del triangulo es: ", triangulo.area())
    print("El perimero del triangulo es: ", triangulo.perimetro())
