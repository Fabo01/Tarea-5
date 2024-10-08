from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, fnacimiento):
        self.__nombre = nombre
        self.__edad = edad
        self.__fnacimiento = fnacimiento

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def fnacimiento(self):
        return self.__fnacimiento

    @fnacimiento.setter
    def fnacimiento(self, fnacimiento):
        self.__fnacimiento = fnacimiento

    @abstractmethod
    def presentarse(self):
        pass