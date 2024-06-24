class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # atributo privado
        self.__modelo = modelo  # atributo privado

    def obtener_marca(self):
        return self.__marca

    def establecer_marca(self, marca): 
        self.__marca = marca

    def obtener_modelo(self):
        return self.__modelo

    def establecer_modelo(self, modelo):
        self.__modelo = modelo

# Crear un objeto Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla")
print(mi_vehiculo.obtener_marca(), mi_vehiculo.obtener_modelo())  # Toyota
mi_vehiculo.establecer_marca("Honda")
print(mi_vehiculo.obtener_marca())  # Honda