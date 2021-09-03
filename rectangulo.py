from poligono import Poligono


class Rectangulo(Poligono):

    def __init__(self):
        super(Rectangulo, self).__init__(2)

    def obtener_base(self):
        return self.lados[0]

    def obtener_altura(self):
        return self.lados[1]

    def area(self):
        return float(self.obtener_base() * self.obtener_altura())

    def perimetro(self):
        return float(2 * self.obtener_base() + 2 * self.obtener_altura())


if __name__ == '__main__':
    rectangulo = Rectangulo()
    rectangulo.leer_lados()
    print("El area del rectangulo es: ", rectangulo.area())
    print("El perimetro del rectangulo es: ", rectangulo.perimetro())
