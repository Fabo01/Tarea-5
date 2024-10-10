from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from MostrarInfo import MostrarInfo

class Grupo(MostrarInfo):
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
    
    def agregar_estudiante(self, estudiante):             
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
            print(f"\nEstudiante {estudiante.nombre} ha sido agregado al grupo {self.__ngrupo}.")
        else:
            print(f"\nEl estudiante {estudiante.nombre} ya está inscrito en el grupo.")

    def eliminar_estudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.matricula == matricula:
                self.__estudiantes.remove(estudiante)
                print(f"\nEstudiante con matrícula {matricula} ha sido eliminado del grupo.")
                return
        print(f"\nNo se encontró un estudiante con matrícula {matricula}.")

    def mostrar_info(self):
        print(f"Grupo: {self.__ngrupo}, Asignatura: {self.__asignatura.nombre}, Profesor: {self.__profesor.nombre}")
        print("Estudiantes:")
        for estudiante in self.__estudiantes:
            edad = estudiante.calcular_edad()
            print(f" - {estudiante.nombre} de {edad} años, matrícula: {estudiante.matricula}")