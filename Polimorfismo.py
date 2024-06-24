class Vehiculo:
    def moverse(self):
        pass

class Coche(Vehiculo):
    def moverse(self):
        return "El coche está conduciendo"

class Bicicleta(Vehiculo):
    def moverse(self):
        return "La bicicleta está pedaleando"

# Crear objetos de diferentes clases
vehiculo1 = Coche()
vehiculo2 = Bicicleta()

# Utilizar polimorfismo
def mover_vehiculo(vehiculo):
    print(vehiculo.moverse())

mover_vehiculo(vehiculo1)  # El coche está conduciendo
mover_vehiculo(vehiculo2)  # La bicicleta está pedaleando
