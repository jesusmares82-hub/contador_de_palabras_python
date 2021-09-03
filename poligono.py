class Poligono:

    def __init__(self, numero_lados='', b='', h=''):
        self.numero_lados = numero_lados
        self.lados = []

    def leer_lados(self):
        while True:
            lado = float(input(">"))
            self.lados.append(lado)
            if len(self.lados) >= self.numero_lados:
                break

    def obtener_lados(self):
        return self.numero_lados


if __name__ == '__main__':
    poligono = Poligono()
    poligono.leer_lados()

