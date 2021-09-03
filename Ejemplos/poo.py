class SerVivo:

    def respirar(self):
        print("Respirando")

class Animal:

    def __init__(self, edad, nombre, numero_patas=None):
        self.edad = edad
        self.numero_patas = numero_patas or 4


    def comer(self):
        if self.nombre == '':
            raise ValueError("El objeto no tiene definido un nombre")
        print(f"Comiendo ({self}): {self.nombre}")


class Perro(Animal, SerVivo):
    numero_patas = 4

    def __init__(self, nombre, raza='', color='', edad=0):
        super().__init__(edad, nombre, numero_patas=self.numero_patas)
        print(f"Se creo el objeto {self}")
        self.nombre = nombre
        self.raza = raza
        self.color = color

    def ladrar(self):
        print("Wuau! (", self.nombre, ")")
        print(f"Wuau! ({self.nombre})")
        print("Wuau! ({0})".format(self.nombre))
        print("Wuau! (" + self.nombre + ')')
        print("Wuau! (%s)" % self.nombre + ')')

    def __del__(self):
        print(f"Se elimina el objeto {self}")


perro_1 = Perro('Toby', raza='Pastor Aleman', color='Negro', edad=5)
print(perro_1, type(perro_1), perro_1.nombre, perro_1.raza, perro_1.color)
perro_1.ladrar()
perro_1.comer()
perro_1.respirar()
