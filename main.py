from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico
import re
class SistemaGestionUniversitaria:
    def __init__(self):
        self.estudiantes = [] #listas para almacenar objetos
        self.profesores = []
        self.asignaturas = []
        self.grupos = []
        self.programas = []

    def menu_principal(self):
        while True:
            print("\n====== Menú Principal ======\n") #menu principal
            print("1. Gestionar Estudiantes")
            print("2. Gestionar Profesores")
            print("3. Gestionar Asignaturas")
            print("4. Gestionar Grupos")
            print("5. Gestionar Programas Académicos")
            print("6. Salir")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.menu_estudiantes()
            elif opcion == "2":
                self.menu_profesores()
            elif opcion == "3":
                self.menu_asignaturas()
            elif opcion == "4":
                self.menu_grupos()
            elif opcion == "5":
                self.menu_programas()
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")

    # Menú para gestionar estudiantes
    def menu_estudiantes(self):
        while True:
            print("\n====== Gestión de Estudiantes ======\n")
            print("1. Agregar Estudiante")
            print("2. Eliminar Estudiante")
            print("3. Mostrar Estudiantes")
            print("4. Estudiar")
            print("5. Volver al Menú Principal")

            opcion = input("\nSeleccione una opción:")

            if opcion == "1":
                self.agregar_estudiante()
            elif opcion == "2":
                self.eliminar_estudiante()
            elif opcion == "3":
                self.mostrar_estudiantes()
            elif opcion == "4":
                self.estudiar()
            elif opcion == "5":
                break
            else:
                print("\nOpción no válida, por favor intente de nuevo.")

    def agregar_estudiante(self):
        nombre = self.validar_str(input("\nIngrese el nombre del estudiante: "), "Nombre")
        matricula = self.validar_int(input("Ingrese la matrícula del estudiante: "), "Matrícula")
        carrera = self.validar_str(input("Ingrese la carrera: "), "Carrera")
        semestre = self.validar_int(input("Ingrese el semestre: "), "Semestre")
        fnac = self.validar_date(input("Ingrese la fecha de nacimiento (DD/MM/AAAA): "), "Fecha de Nacimiento(DD/MM/AAAA)")

        if None in (nombre, matricula, carrera, semestre, fnac):
            print("\nError: Alguno de los datos no se ha ingresado, por favor intente de nuevo.")
            return
        # Validación de duplicados por matrícula
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                print(f"\nEl estudiante con matrícula {matricula} ya está registrado.")
                return

        nuevo_estudiante = Estudiante(nombre, fnac, matricula, carrera, semestre)
        self.estudiantes.append(nuevo_estudiante)
        print(f"\nEstudiante {nombre} agregado correctamente.")

    def eliminar_estudiante(self):
        matricula = self.validar_int(input("\nIngrese la matrícula del estudiante a eliminar: "), "Matrícula")

        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                self.estudiantes.remove(estudiante)
                print(f"\nEstudiante con matrícula {matricula} eliminado.")
                return

        print(f"\nNo se encontró un estudiante con matrícula {matricula}.")

    def estudiar(self):
        matricula = self.validar_int(input("Ingrese la matrícula del estudiante: "), "Matrícula")
        estudiante = self.buscar_estudiante(matricula)

        if not estudiante:
            print(f"\nNo se encontró un estudiante con matrícula {matricula}.")
            return

        print("\n===== Asignaturas Disponibles =====")
        for asignatura in self.asignaturas:
            print(f"Asignatura: {asignatura.nombre}, Código: {asignatura.codigo}")

        codigo_asignatura = self.validar_int(input("Ingrese el código de la asignatura que desea estudiar: "), "Código de Asignatura")
        asignatura = self.buscar_asignatura(codigo_asignatura)

        if not asignatura:
            print(f"\nNo se encontró una asignatura con código {codigo_asignatura}.")
            return
        horas = self.validar_int(input("Ingrese el número de horas: "), "Número de horas")
        
        if horas is None:
            print("\nError: Número de horas no válido.")
            return

        estudiante.estudiar(asignatura, horas)

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("\nNo hay estudiantes registrados.")
        else:
            print("\n====== Lista de Estudiantes ======\n")
            for estudiante in self.estudiantes:
                estudiante.presentarse()

    # Menú para gestionar profesores
    def menu_profesores(self):
        while True:
            print("\n====== Gestión de Profesores ======\n")
            print("1. Agregar Profesor")
            print("2. Eliminar Profesor")
            print("3. Mostrar Profesores")
            print("4. Enseñar")
            print("4. Volver al Menú Principal")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.agregar_profesor()
            elif opcion == "2":
                self.eliminar_profesor()
            elif opcion == "3":
                self.mostrar_profesores()
            elif opcion == "4":
                self.enseñar()
            elif opcion == "5":
                break
            else:
                print("\nOpción no válida, por favor intente de nuevo.")

    def agregar_profesor(self):
        nombre = self.validar_str(input("\nIngrese el nombre del profesor: "), "Nombre")
        n_empleado = self.validar_int(input("Ingrese el número de empleado: "), "Número de Empleado")
        departamento = self.validar_str(input("Ingrese el departamento: "), "Departamento")
        fnac = self.validar_date(input("Ingrese la fecha de nacimiento (DD/MM/AAAA): "), "Fecha de Nacimiento(DD/MM/AAAA)")

        if None in (nombre, n_empleado, departamento, fnac):
            print("\nError: Alguno de los datos no se ha ingresado, por favor intente de nuevo.")
            return
        # Validación de duplicados por número de empleado
        for profesor in self.profesores:
            if profesor.n_empleado == n_empleado:
                print(f"\nEl profesor con número de empleado {n_empleado} ya está registrado.")
                return

        nuevo_profesor = Profesor(nombre, fnac, n_empleado, departamento)
        self.profesores.append(nuevo_profesor)
        print(f"\nProfesor {nombre} agregado correctamente.")

    def eliminar_profesor(self):
        n_empleado = self.validar_int(input("\nIngrese el número de empleado del profesor a eliminar: "), "Número de Empleado")

        for profesor in self.profesores:
            if profesor.n_empleado == n_empleado:
                self.profesores.remove(profesor)
                print(f"\nProfesor con número de empleado {n_empleado} eliminado.")
                return

        print(f"\nNo se encontró un profesor con número de empleado {n_empleado}.")

    def enseñar(self):
        num_empleado = self.validar_int(input("Ingrese el número de empleado del profesor: "), "Número de Empleado")
        profesor = self.buscar_profesor(num_empleado)

        if not profesor:
            print(f"\nNo se encontró un profesor con número de empleado {num_empleado}.")
            return

        # Mostrar las asignaturas disponibles
        print("\n===== Asignaturas Disponibles =====")
        for asignatura in self.asignaturas:
            print(f"Asignatura: {asignatura.nombre}, Código: {asignatura.codigo}")

        codigo_asignatura = self.validar_int(input("Ingrese el código de la asignatura que desea enseñar: "), "Código de Asignatura")
        asignatura = self.buscar_asignatura(codigo_asignatura)

        if not asignatura:
            print(f"\nNo se encontró una asignatura con código {codigo_asignatura}.")
            return

        profesor.enseñar(asignatura.nombre)
    

    def mostrar_profesores(self):
        if not self.profesores:
            print("\nNo hay profesores registrados.")
        else:
            print("\n====== Lista de Profesores ======\n")
            for profesor in self.profesores:
                profesor.presentarse()

    # Menú para gestionar asignaturas
    def menu_asignaturas(self):
        while True:
            print("\n====== Gestión de Asignaturas ======\n")
            print("1. Agregar Asignatura")
            print("2. Eliminar Asignatura")
            print("3. Mostrar Asignaturas")
            print("4. Volver al Menú Principal")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.agregar_asignatura()
            elif opcion == "2":
                self.eliminar_asignatura()
            elif opcion == "3":
                self.mostrar_asignaturas()
            elif opcion == "4":
                break
            else:
                print("\nOpción no válida, por favor intente de nuevo.")

    def agregar_asignatura(self):
        nombre = input("\nIngrese el nombre de la asignatura: ")
        codigo = input("Ingrese el código de la asignatura: ")
        creditos = self.validar_int(input("Ingrese los créditos: "), "Créditos")

        if None in (nombre, codigo, creditos):
            print("\nError: Alguno de los datos no se ha ingresado, por favor intente de nuevo.")
            return
        # Validación de duplicados por código
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                print(f"\nLa asignatura con código {codigo} ya está registrada.")
                return

        nueva_asignatura = Asignatura(nombre, codigo, creditos)
        self.asignaturas.append(nueva_asignatura)
        print(f"\nAsignatura {nombre} agregada correctamente.")

    def eliminar_asignatura(self):
        codigo = input("\nIngrese el código de la asignatura a eliminar: ")

        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                self.asignaturas.remove(asignatura)
                print(f"\nAsignatura con código {codigo} eliminada.")
                return

        print(f"\nNo se encontró una asignatura con código {codigo}.")

    def mostrar_asignaturas(self):
        if not self.asignaturas:
            print("\nNo hay asignaturas registradas.")
        else:
            print("\n====== Lista de Asignaturas ======\n")
            for asignatura in self.asignaturas:
                asignatura.mostrar_info()

    # Menú para gestionar grupos
    def menu_grupos(self):
        while True:
            print("\n====== Gestión de Grupos ======\n")
            print("1. Agregar Grupo")
            print("2. Eliminar Grupo")
            print("3. Mostrar Grupos")
            print("4. Agregar Estudiante a un Grupo") 
            print("5. Eliminar Estudiante de un Grupo")  
            print("6. Volver al Menú Principal")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.agregar_grupo()
            elif opcion == "2":
                self.eliminar_grupo()
            elif opcion == "3":
                self.mostrar_grupos()
            elif opcion == "4":
                self.agregar_estudiante_grupo()
            elif opcion == "5":
                self.eliminar_estudiante_grupo()    
            elif opcion == "6":
                break
            else:
                print("\nOpción no válida, por favor intente de nuevo.")

    def agregar_estudiante_grupo(self):
        numero_grupo = self.validar_int(input("\nIngrese el número del grupo: "), "Número de Grupo")
        matricula = self.validar_int(input("Ingrese la matrícula del estudiante: "), "Matrícula")

        grupo = self.buscar_grupo(numero_grupo)
        estudiante = self.buscar_estudiante(matricula)

        if not grupo:
            print(f"\nNo se encontró el grupo con número {numero_grupo}.")
            return

        if not estudiante:
            print(f"\nNo se encontró el estudiante con matrícula {matricula}.")
            return
        grupo.agregar_estudiante(estudiante)

    def eliminar_estudiante_grupo(self):
        numero_grupo = self.validar_int(input("\nIngrese el número del grupo: "), "Número de Grupo")
        matricula = self.validar_int(input("Ingrese la matrícula del estudiante a eliminar: "), "Matrícula")

        grupo = self.buscar_grupo(numero_grupo)

        if not grupo:
            print(f"\nNo se encontró el grupo con número {numero_grupo}.")
            return
        if not matricula:
            print("\nError: Matrícula no válida.")
            return
        grupo.eliminar_estudiante(matricula)

    def agregar_grupo(self):
        numero_grupo = self.validar_int(input("\nIngrese el número del grupo: "), "Número de Grupo")
        codigo_asignatura = input("Ingrese el código de la asignatura: ")
        num_empleado = self.validar_int(input("Ingrese el número de empleado del profesor: "), "Número de Empleado")

        # Buscar la asignatura
        asignatura = None
        for asign in self.asignaturas:
            if asign.codigo == codigo_asignatura:
                asignatura = asign
                break
        if not asignatura:
            print(f"\nNo se encontró una asignatura con código {codigo_asignatura}.")
            return

        # Buscar el profesor
        profesor = None
        for prof in self.profesores:
            if prof.n_empleado == num_empleado:
                profesor = prof
                break
        if not profesor:
            print(f"\nNo se encontró un profesor con número de empleado {num_empleado}.")
            return

        nuevo_grupo = Grupo(int(numero_grupo), asignatura, profesor)
        self.grupos.append(nuevo_grupo)
        print(f"\nGrupo {numero_grupo} agregado correctamente.")

    def eliminar_grupo(self):
        numero_grupo = self.validar_int(input("\nIngrese el número del grupo a eliminar: "), "Número de Grupo")

        for grupo in self.grupos:
            if grupo.ngrupo == int(numero_grupo):
                self.grupos.remove(grupo)
                print(f"\nGrupo {numero_grupo} eliminado.")
                return

        print(f"\nNo se encontró un grupo con número {numero_grupo}.")

    def mostrar_grupos(self):
        if not self.grupos:
            print("\nNo hay grupos registrados.")
        else:
            print("\n====== Lista de Grupos ======\n")
            for grupo in self.grupos:
                grupo.mostrar_info()

    def menu_programas(self):
        while True:
            print("\n====== Gestión de Programas Académicos ======\n")
            print("1. Agregar Programa Académico")
            print("2. Eliminar Programa Académico")
            print("3. Mostrar Programas Académicos")
            print("4. Agregar Grupo a un Programa Académico")  # Nueva opción
            print("5. Eliminar Grupo de un Programa Académico")  # Nueva opción
            print("6. Volver al Menú Principal")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.agregar_programa()
            elif opcion == "2":
                self.eliminar_programa()
            elif opcion == "3":
                self.mostrar_programas()
            elif opcion == "4":
                self.agregar_grupo_programa()
            elif opcion == "5":
                self.eliminar_grupo_programa()
            elif opcion == "6":
                break
            else:
                print("\nOpción no válida, por favor intente de nuevo.")

    def agregar_programa(self):
        nombre = input("\nIngrese el nombre del programa académico: ")
        codigo = input("Ingrese el código del programa académico: ")

        # Validación de duplicados por código
        for programa in self.programas:
            if programa.codigo == codigo:
                print(f"\nEl programa académico con código {codigo} ya está registrado.")
                return

        nuevo_programa = ProgramaAcademico(nombre, codigo)
        self.programas.append(nuevo_programa)
        print(f"\nPrograma académico {nombre} agregado correctamente.")

    def eliminar_programa(self):
        codigo = input("\nIngrese el código del programa académico a eliminar: ")

        for programa in self.programas:
            if programa.codigo == codigo:
                self.programas.remove(programa)
                print(f"\nPrograma académico con código {codigo} eliminado.")
                return

        print(f"\nNo se encontró un programa académico con código {codigo}.")

    def mostrar_programas(self):
        if not self.programas:
            print("\nNo hay programas académicos registrados.")
        else:
            print("\n====== Lista de Programas Académicos ======\n")
            for programa in self.programas:
                programa.mostrar_info() 

    def agregar_grupo_programa(self):
        codigo_programa = input("\nIngrese el código del programa académico: ")

        # Buscar el programa académico
        programa = self.buscar_programa(codigo_programa)
        if not programa:
            print(f"\nNo se encontró un programa académico con código {codigo_programa}.")
            return

        numero_grupo = self.validar_int(input("Ingrese el número del grupo a agregar: "), "Número de Grupo")
        if numero_grupo is None:
            return  # Si la validación falla, termina el proceso

        # Buscar el grupo existente
        grupo = self.buscar_grupo(numero_grupo)
        if not grupo:
            print(f"\nNo se encontró un grupo con número {numero_grupo}.")
            return
        # Agregar el grupo existente al programa académico
        programa.agregar_grupo(grupo)

    # Método para eliminar un grupo de un programa académico
    def eliminar_grupo_programa(self):
        codigo_programa = input("\nIngrese el código del programa académico: ")

        programa = self.buscar_programa(codigo_programa)
        if not programa:
            print(f"\nNo se encontró un programa académico con código {codigo_programa}.")
            return

        numero_grupo = input("Ingrese el número del grupo a eliminar: ")

        programa.eliminar_grupo(int(numero_grupo))

    # Método para buscar un programa académico por código
    def buscar_programa(self, codigo):
        for programa in self.programas:
            if programa.codigo == codigo:
                return programa
        return None

    # Métodos auxiliares para buscar asignaturas y profesores
    def buscar_asignatura(self, codigo_asignatura):
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo_asignatura:
                return asignatura
        return None

    def buscar_profesor(self, num_empleado):
        for profesor in self.profesores:
            if profesor.n_empleado == num_empleado:
                return profesor
        return None 

    def buscar_grupo(self, numero_grupo):
        for grupo in self.grupos:
            if grupo.ngrupo == numero_grupo:
                return grupo
        return None

    def buscar_estudiante(self, matricula):
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                return estudiante
        return None  

    # Validar que el campo sea un número entero
    def validar_int(self, valor, campo_nombre):
        try:
            return int(valor)
        except ValueError:
            print(f"\nError: {campo_nombre} debe ser un número entero.")
            return None

    # Validar que el campo sea una cadena no vacía
    def validar_str(self, valor, campo_nombre):
        if not valor.strip():
            print(f"\nError: {campo_nombre} no puede estar vacío.")
            return None
        # Validar que la cadena solo contenga letras y espacios
        if not re.match(r"^[A-Za-z\s]+$", valor):
            print(f"\nError: {campo_nombre} solo puede contener letras.")
            return None
        return valor.strip()

    # Validar formato de fecha (DD/MM/AAAA)
    def validar_date(self, fecha, campo_nombre):
        if re.match(r"^\d{2}/\d{2}/\d{4}$", fecha):
            return fecha
        else:
            print(f"\nError: {campo_nombre} debe tener el formato DD/MM/AAAA.")
            return None                
# Ejecutar el sistema
sistema = SistemaGestionUniversitaria()
sistema.menu_principal()
