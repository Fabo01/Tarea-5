from abc import ABC, abstractmethod
from datetime import datetime
class Persona(ABC):
    def __init__(self, nombre, fnacimiento):      # Clase abstracta para Estudiante y Profesor
        self.__nombre = nombre

        self.__fnacimiento = fnacimiento

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def fnacimiento(self):
        return self.__fnacimiento

    @fnacimiento.setter
    def fnacimiento(self, fnacimiento):
        self.__fnacimiento = fnacimiento

    def calcular_edad(self): #Función para calcular la edad en base a la fecha de nacimiento
        fecha_nac = datetime.strptime(self.__fnacimiento, "%d/%m/%Y")
        fecha_actual = datetime.now()
        edad = fecha_actual.year - fecha_nac.year
        # Si aún no ha cumplido años este año, restar 1
        if (fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day):
            edad -= 1
        return edad

    @abstractmethod
    def presentarse(self): #Método abstracto para presentarse en Estudiante y Profesor
        pass