class EntradaUsuario:

    def __init__(self):
        self.datos = []

    def leer_datos(self):
        while True:
            linea = input('>')
            if linea == 'done':
                break
            self.datos.append(linea)

    def lista_strings(self):
        #return [v for v in self.datos if not v.isnumeric()]
        valores =[]
        for valor in self.datos:
            if valor.isnumeric():
                continue

            valores.append(valor)

        return valores

    def lista_ints(self):
        # return [v for v in self.datos if v.isnumeric()]
        valores =[]
        for valor in self.datos:
            if not valor.isnumeric():
                continue

            valores.append(int(valor))

        return valores


if __name__ == '__main__':
    entrada = EntradaUsuario()
    entrada.leer_datos()
    print(entrada.lista_ints())
