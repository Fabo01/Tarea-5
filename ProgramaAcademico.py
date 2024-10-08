from Grupo import Grupo

class ProgramaAcademico:
    def __init__(self, nombre:str, codigo:str):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__grupos = []

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
    def grupos(self):
        return self.__grupos
    
    def agregar_grupo(self, grupo):
        if grupo not in self.__grupos:
            self.__grupos.append(grupo)
            print(f"Grupo {grupo.ngrupo} ha sido agregado al programa {self.__nombre}.")
        else:
            print(f"El grupo {grupo.ngrupo} ya está registrado en el programa.")

    def eliminar_grupo(self, ngrupo):
        for grupo in self.__grupos:
            if grupo.ngrupo == ngrupo:
                self.__grupos.remove(grupo)
                print(f"Grupo {ngrupo} ha sido eliminado del programa.")
                return
        print(f"No se encontró un grupo con el número {ngrupo}.")

    def mostrar_info(self):
        print(f"Programa: {self.__nombre}, Código: {self.__codigo}")
        print("Grupos:")
        for grupo in self.__grupos:
            grupo.mostrar_info()    