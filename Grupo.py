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
        self.__lista_asignaturas = []

    @property
    def ngrupo(self):
        return self.__ngrupo
    
    @ngrupo.setter
    def ngrupo(self, ngrupo):
        self.__ngrupo = ngrupo

    @property
    def profesor(self):
        return self.__profesor
    
    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    @property
    def lista_asignaturas(self):
        return self.__lista_asignaturas
    
    @property
    def estudiantes(self):
        return self.__estudiantes
    
    @property  
    def asignatura(self):
        return self.__asignatura
    
    @asignatura.setter 
    def asignatura(self, asignatura):
        self.__asignatura = asignatura

    def agregar_asignatura(self, asignatura):  
        if len(self.__lista_asignaturas) == 0:
            self.__lista_asignaturas.append(self.__asignatura)
            return f"Asignatura {asignatura.nombre}, Código:{asignatura.codigo} ha sido agregada al grupo {self.__ngrupo}."           
        if asignatura not in self.__lista_asignaturas:
            self.__estudiantes.append(asignatura)
            return f"Estudiante {asignatura.codigo}, Matricula:{asignatura.codigo} ha sido agregado al grupo {self.__ngrupo}."
        else:
            return f"El estudiante {asignatura.codigo}, Matricula:{asignatura.codigo} ya está inscrito en el grupo."

    def eliminar_asignatura(self, codigo):
        for asignatura in self.__lista_asignaturas:
            if asignatura.codigo == codigo:
                self.__lista_asignaturas.remove(asignatura)
                return f"Estudiante con matrícula {codigo} ha sido eliminado del grupo."
        return f"No se encontró un estudiante con matrícula {codigo}."
    
    def agregar_estudiante(self, estudiante):             
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
            return f"Estudiante {estudiante.nombre}, Matricula:{estudiante.matricula} ha sido agregado al grupo {self.__ngrupo}."
        else:
            return f"El estudiante {estudiante.nombre}, Matricula:{estudiante.matricula} ya está inscrito en el grupo."

    def eliminar_estudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.matricula == matricula:
                self.__estudiantes.remove(estudiante)
                return f"Estudiante con matrícula {matricula} ha sido eliminado del grupo."
        return f"No se encontró un estudiante con matrícula {matricula}."

    def mostrar_info(self):
        info = f'El Grupo n°{self.__ngrupo} con el Profesor: {self.__profesor.nombre}\nCon las Asignaturas:\n'
        for asign in self.lista_asignaturas:
            info += f'{asign.nombre}, Codigo: {asign.codigo}\n'
        info += 'Y los Estudiantes:\n'
        for estudiante in self.estudiantes:
            info += f'{estudiante.nombre}, Matricula: {estudiante.matricula}\n'
        return info
    
    