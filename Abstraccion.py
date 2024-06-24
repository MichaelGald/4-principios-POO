from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# Uso
if __name__ == "__main__":
    perro = Perro()
    gato = Gato()
    perro.hacer_sonido()  # Guau
    gato.hacer_sonido()   # Miau

