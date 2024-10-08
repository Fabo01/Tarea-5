from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, fnacimiento, matricula, carrera, semestre):
        super().__init__(nombre, edad, fnacimiento)
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre

    @property 
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def carrera(self):
        return self.__carrera
    
    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    @property
    def semestre(self):
        return self.__semestre
    
    @semestre.setter
    def semestre(self, semestre):
        self.__semestre = semestre

    def estudiar(self, asignatura, horas):
        print(f'{self.nombre} estudia {asignatura} durante {horas} horas.')

    def presentarse(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Semestre: {self.semestre}, Matricula: {self.matricula}')