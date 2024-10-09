from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, fnacimiento, nempleado, departamento):
        super().__init__(nombre, fnacimiento)
        self.__n_empleado = nempleado
        self.__departamento = departamento

    @property 
    def n_empleado(self):
        return self.__n_empleado
    
    @n_empleado.setter
    def n_empleado(self, n_empleado):
        self.__n_empleado = n_empleado

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    def enseñar(self, asignatura, horas):
        print(f'{self.nombre} imparte la asignatura {asignatura} durante {horas} horas.')

    def presentarse(self):
        edad = self.calcular_edad()
        print(f'Nombre: {self.nombre}, Edad: {edad}, Departamento: {self.departamento}, Num. Empleado: {self.n_empleado}')