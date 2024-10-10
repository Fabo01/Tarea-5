from abc import ABC, abstractmethod

class MostrarInfo(ABC):
    
    @abstractmethod
    def mostrar_info(self):   #interfaz para mostrar información de Grupo, ProgramaAcademico y Asignatura
        pass