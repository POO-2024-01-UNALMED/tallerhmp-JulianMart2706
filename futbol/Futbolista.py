from .Persona import Persona
from .Deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre: str, edad: int, altura: str, sexo: str,
                 golesMarcados: int, tarjetasRojas: int, piernaHabil: str, 
                 deporte: str = "Futbol", añosPracticando: int = 0):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)



    def get_golesMarcados(self):
        return self.__golesMarcados

    def get_tarjetasRojas(self):
        return self.__tarjetasRojas

    def get_piernaHabil(self):
        return self.__piernaHabil



    def set_golesMarcados(self, golesMarcados: int):
        self.__golesMarcados = golesMarcados

    def set_tarjetasRojas(self, tarjetasRojas: int):
        self.__tarjetasRojas = tarjetasRojas

    def set_piernaHabil(self, piernaHabil: str):
        self.__piernaHabil = piernaHabil



    def __str__(self):
        return (f"Mi nombre es {self.get_nombre()}, soy profesional en el deporte "
                f"{self.get_deporte()}. Tengo {self.get_edad()} años de edad y llevo "
                f"{self.get_añosPracticando()} años en el deporte.")
