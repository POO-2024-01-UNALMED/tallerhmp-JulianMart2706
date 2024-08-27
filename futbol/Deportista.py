class Deportista:
    def __init__(self, deporte: str = "Futbol", añosPracticando: int = 0):
        self.__deporte = deporte
        self.__añosPracticando = añosPracticando


    def get_deporte(self):
        return self.__deporte
    
    def get_añosPracticando(self):
        return self.__añosPracticando


    def set_deporte(self, deporte: str):
        self.__deporte = deporte

    def set_añosPracticando(self, añosPracticando: int):
        self.__añosPracticando = añosPracticando
