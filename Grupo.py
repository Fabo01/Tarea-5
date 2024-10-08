from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura

class Grupo:
    def __init__(self, ngrupo:int, asignatura:Asignatura, profesor:Profesor):
        self.__ngrupo = ngrupo
        self.__asignatura = asignatura
        self.__profesor = profesor
        self.__estudiantes = []

    @property
    def ngrupo(self):
        return self.__ngrupo
    
    @ngrupo.setter
    def ngrupo(self, ngrupo):
        self.__ngrupo = ngrupo

    @property
    def asignatura(self):
        return self.__asignatura
    
    @asignatura.setter
    def asignatura(self, asignatura):
        self.__asignatura = asignatura

    @property
    def profesor(self):
        return self.__profesor
    
    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    @property
    def estudiantes(self):
        return self.__estudiantes
    
    def agregar_estudiante(self, estudiante):              ###  REVISAR  ###o
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} ha sido agregado al grupo {self.__ngrupo}.")
        else:
            print(f"El estudiante {estudiante.nombre} ya está inscrito en el grupo.")

    def eliminar_estudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.matricula == matricula:
                self.__estudiantes.remove(estudiante)
                print(f"Estudiante con matrícula {matricula} ha sido eliminado del grupo.")
                return
        print(f"No se encontró un estudiante con matrícula {matricula}.")

    def mostrar_info(self):
        print(f"Grupo: {self.__ngrupo}, Asignatura: {self.__asignatura.nombre}, Profesor: {self.__profesor.nombre}")
        print("Estudiantes:")
        for estudiante in self.__estudiantes:
            print(f" - {estudiante.nombre} {estudiante.edad}, matrícula: {estudiante.matricula}")