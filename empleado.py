class Empleado():

    def __init__(self, id, nombres, apellidos):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos

    def establecer_id(self, id):
        self.__id = id

    def obtener_nombres(self, nombres):
        self.__nombres = nombres

    def obtener_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def obtener_id(self):
        return self.__id

    def obtener_nombres(self):
        return self.__nombres

    def obtener_apellidos(self):
        return self.__apellidos

    