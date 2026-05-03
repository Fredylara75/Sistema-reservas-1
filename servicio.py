from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, costo_base):
        self._nombre = nombre
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def validar_disponibilidad(self):
        pass