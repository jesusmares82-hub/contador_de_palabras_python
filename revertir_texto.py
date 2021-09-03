from entradas import EntradaUsuario


class RevertirTexto(EntradaUsuario):
    def revertir(self):
        datos = self.lista_strings()
        datos.reverse()
        return datos


if __name__ == '__main__':
    revertir = RevertirTexto()
    revertir.leer_datos()
    resultado = revertir.revertir()
    print(resultado)
