import animal

class Aguila(animal.Animal):

    def __init__(self, id, nombre, id_cuidador_principal, largo_alas, largo_pico):
        super().__init__(id, nombre, id_cuidador_principal)
        self.__largo_alas = largo_alas
        self.__largo_pico = largo_pico

    def establecer_largo_alas(self, largo_alas):
        self.__largo_alas = largo_alas

    def establecer_largo_pico(self, largo_pico):
        self.__largo_pico = largo_pico

    def obtener_largo_alas(self):
        return self.__largo_alas

    def establecer_largo_pico(self):
        return self.__largo_pico

    