class Vehiculo:

    def __init__(self, marca, modelo='', color=''):
        print(f"Se creo el objeto {self}")
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print("Acelera! (", self.marca, ")")

    def frenar(self):
        print("Frena! (", self.marca, ")")

    def __del__(self):
        print(f"Se elimina el objeto {self}")


vehiculo_1 = Vehiculo('Toyota', modelo='Avanza', color='Negro')
print(vehiculo_1, type(vehiculo_1), vehiculo_1.marca, vehiculo_1.modelo, vehiculo_1.color)
vehiculo_1.acelerar()
vehiculo_1.frenar()

vehiculo_2 = Vehiculo('Nissan', modelo='Sentra', color='Rojo')
print(vehiculo_2, type(vehiculo_2), vehiculo_2.marca, vehiculo_2.modelo, vehiculo_2.color)
vehiculo_2.acelerar()
vehiculo_2.frenar()
vehiculo_2.frenar()
