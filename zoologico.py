class Zoologico:

    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.__animales = []
        self.__empleados = []

    def establecer_id(self, id):
        self.__id = id

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def agregar_animal(self, animal):
        self.__animales.append(animal)

    def remover_animal(self, animal):
        self.__animales.remove(animal)

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def remover_empleado(self, empleado):
        self.__empleados.remove(empleado)

    def obtener_id(self):
        return self.__id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_animales(self):
        return self.__animales

    def obtener_empleados(self):
        return self.__empleados

    def __eq__(self, otro):
        if not isinstance(otro, Zoologico):
            return False

        return self.obtener_id() == otro.obtener_id()

    def __str__(self):
        animales = ", ".join(str(animal) for animal in self.obtener_animales())
        empleados = ", ".join(
            str(empleado) for empleado in self.obtener_empleados()
        )
        return (
            f"ID: {self.obtener_id()}, "
            f"Nombre: {self.obtener_nombre()}, "
            f"Animales: [{animales}], "
            f"Empleados: [{empleados}]"
        )
