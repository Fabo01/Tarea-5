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
        return f'{self.nombre} imparte la asignatura {asignatura} durante {horas} horas.'

    def presentarse(self):
        edad = self.calcular_edad()
        return f'Hola, soy {self.nombre}, tengo {edad} años de edad, soy profesor del departamento de {self.departamento} y mi número de empleado es: {self.n_empleado}'