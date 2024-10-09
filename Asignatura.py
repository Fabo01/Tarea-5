from MostrarInfo import MostrarInfo

class Asignatura(MostrarInfo):
    def __init__(self, nombre, codigo, creditos):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self, creditos):
        self.__creditos = creditos

    def mostrar_info(self):
        print(f'Asignatura: {self.nombre}, Codigo: {self.codigo}, Creditos: {self.creditos}')