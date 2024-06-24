from abc import ABC, abstractmethod

# Clase base abstracta para empleados
class Empleado(ABC):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 18:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser mayor o igual a 18 años.")
    
    @abstractmethod
    def calcular_salario(self):
        pass
    
    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")

# Clase concreta para Empleado de Tiempo Completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, edad, salario_base, bonificaciones):
        super().__init__(nombre, edad)
        self.salario_base = salario_base
        self.bonificaciones = bonificaciones
    
    def calcular_salario(self):
        return self.salario_base + self.bonificaciones
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo: Empleado de Tiempo Completo")
        print(f"Salario Base: ${self.salario_base}, Bonificaciones: ${self.bonificaciones}")
        print(f"Salario Total: ${self.calcular_salario()}")

# Clase concreta para Empleado por Horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, edad, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, edad)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo: Empleado por Horas")
        print(f"Horas Trabajadas: {self.horas_trabajadas}, Tarifa por Hora: ${self.tarifa_por_hora}")
        print(f"Salario Total: ${self.calcular_salario()}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear empleados
    empleado1 = EmpleadoTiempoCompleto("Juan", 30, 3000, 1000)
    empleado2 = EmpleadoPorHoras("María", 25, 80, 15)
    empleado3 = EmpleadoPorHoras("Marlon", 20, 100, 10)
    
    # Mostrar información de los empleados
    empleado1.mostrar_informacion()
    print("-----------------------")
    empleado2.mostrar_informacion()
    print("-----------------------")
    empleado3.mostrar_informacion()
