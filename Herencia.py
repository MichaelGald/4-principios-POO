class Persona:
    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self.Edad = edad

    def MostrarInformacion(self):
        print(f"Nombre: {self.Nombre}, Edad: {self.Edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.Grado = grado

    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f"Grado: {self.Grado}")


# Uso
if __name__ == "__main__":
    estudiante = Estudiante("Juan Perez", 21, "Universidad")
    estudiante.MostrarInformacion()
    estudiante2 = Persona("Maria Garza", 24)
    estudiante2.MostrarInformacion()