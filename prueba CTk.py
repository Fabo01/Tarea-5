import customtkinter as CTk
from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico
import re
from datetime import datetime
from CTkMessagebox import CTkMessagebox as CTkM
from tkinter import ttk

class SistemaGestionUniversitariaApp(CTk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Sistema de Gestión Universitaria")
        self.geometry("1000x800")

        # Datos
        self.estudiantes = []
        self.profesores = []
        self.asignaturas = []
        self.grupos = []
        self.programas = []

        # Crear el menú principal
        self.frame_principal = CTk.CTkFrame(self)
        self.frame_principal.pack(pady=20, padx=20, fill="both", expand=True)
        self.crear_menu_principal()

    def crear_menu_principal(self):
        # Crear el contenedor principal 
        self.limpiar_frame()
        # Título del menú
        titulo = CTk.CTkLabel(self.frame_principal, text="Menú Principal", font=("Arial", 24))
        titulo.pack(pady=20)

        # Botones del menú principal
        btn_estudiantes = CTk.CTkButton(self.frame_principal, text="Gestionar Estudiantes", command=self.menu_estudiantes)
        btn_estudiantes.pack(pady=10)

        btn_profesores = CTk.CTkButton(self.frame_principal, text="Gestionar Profesores", command=self.menu_profesores)
        btn_profesores.pack(pady=10)

        btn_asignaturas = CTk.CTkButton(self.frame_principal, text="Gestionar Asignaturas", command=self.menu_asignaturas)
        btn_asignaturas.pack(pady=10)

        btn_grupos = CTk.CTkButton(self.frame_principal, text="Gestionar Grupos", command=self.menu_grupos)
        btn_grupos.pack(pady=10)

        btn_programas = CTk.CTkButton(self.frame_principal, text="Gestionar Programas Académicos", command=self.menu_programas)
        btn_programas.pack(pady=10)
        
    # Menú de estudiantes
    def menu_estudiantes(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Gestión de Estudiantes", font=("Arial", 24))
        titulo.pack(pady=20)

        btn_agregar_estudiante = CTk.CTkButton(self.frame_principal, text="Agregar Estudiante", command=self.crear_estudiante)
        btn_agregar_estudiante.pack(pady=10)

        btn_mostrar_estudiantes = CTk.CTkButton(self.frame_principal, text="Mostrar Estudiantes", command=self.mostrar_estudiantes)
        btn_mostrar_estudiantes.pack(pady=10)

        btn_estudiar_materia = CTk.CTkButton(self.frame_principal, text="Estudiar Materia", command=self.estudiar_materia)
        btn_estudiar_materia.pack(pady=10)

        btn_info_estudiante = CTk.CTkButton(self.frame_principal, text="Mostrar Información del Estudiante", command=self.mostrar_informacion_estudiante)
        btn_info_estudiante.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.crear_menu_principal)
        btn_volver.pack(pady=20)

    # Función para agregar un estudiante (ventana adicional)
    def crear_estudiante(self):
        self.limpiar_frame()
        titulo = CTk.CTkLabel(self.frame_principal, text="Agregar Estudiante", font=("Arial", 24))
        titulo.pack(pady=20)

        # Entradas de texto
        label_nombre = CTk.CTkLabel(self.frame_principal, text="Nombre:")
        label_nombre.pack()
        self.entry_nombre = CTk.CTkEntry(self.frame_principal)
        self.entry_nombre.pack()

        label_matricula = CTk.CTkLabel(self.frame_principal, text="Matrícula:")
        label_matricula.pack()
        self.entry_matricula = CTk.CTkEntry(self.frame_principal)
        self.entry_matricula.pack()

        label_carrera = CTk.CTkLabel(self.frame_principal, text="Carrera:")
        label_carrera.pack()
        self.entry_carrera = CTk.CTkEntry(self.frame_principal)
        self.entry_carrera.pack()

        label_semestre = CTk.CTkLabel(self.frame_principal, text="Semestre:")
        label_semestre.pack()
        self.entry_semestre = CTk.CTkEntry(self.frame_principal)
        self.entry_semestre.pack()

        label_fnac = CTk.CTkLabel(self.frame_principal, text="Fecha de Nacimiento (DD/MM/AAAA):")
        label_fnac.pack()
        self.entry_fnac = CTk.CTkEntry(self.frame_principal)
        self.entry_fnac.pack()

        # Botón para agregar
        btn_guardar = CTk.CTkButton(self.frame_principal, text="Guardar Estudiante", command=self.ingresar_estudiante)
        btn_guardar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_estudiantes)
        btn_volver.pack(pady=20)

    def ingresar_estudiante(self):
        nombre = self.entry_nombre.get()
        matricula = self.entry_matricula.get()
        carrera = self.entry_carrera.get()
        semestre = self.entry_semestre.get()
        fnac = self.entry_fnac.get()   

        # Validar que los campos no estén vacíos
        if not all([nombre, matricula, carrera, semestre, fnac]):
            CTkM(title="Error", message="Todos los campos son obligatorios.", icon="cancel")
            return

        if not self.validar_str(carrera, "carrea"):
            return

        # Validar el nombre
        if not self.validar_str(nombre, "nombre"):
            return

        # Validar que la matrícula y el semestre sean números positivos
        if not self.validar_numero(matricula, "matrícula"):
            return

        if not self.validar_numero(semestre, "semestre"):
            return

        # Validar la fecha de nacimiento
        if not self.validar_fecha(fnac):
            return

        # Validación de duplicados por matrícula
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                CTkM(title="Error", message=f"Estudiante con matrícula {matricula} ya registrado.", icon="cancel")
                return

        # Si todas las validaciones son correctas, crear el nuevo estudiante
        nuevo_estudiante = Estudiante(nombre, fnac, matricula, carrera, semestre)
        self.estudiantes.append(nuevo_estudiante)
        CTkM(title="Éxito", message=f"Estudiante {nombre} agregado correctamente.", icon="check")

    # Función para mostrar los estudiantes
    def mostrar_estudiantes(self):
        self.limpiar_frame()

        if not self.estudiantes:
            CTkM(title="Error", message="No hay estudiantes registrados.", icon="cancel")
            self.crear_menu_principal()
            return
        
        titulo = CTk.CTkLabel(self.frame_principal, text="Lista de Estudiantes", font=("Arial", 24))
        titulo.pack(pady=20)

        # Obtener los nombres de los atributos del primer estudiante
        columnas = list(vars(self.estudiantes[0]).keys())

        # Crear el Treeview
        self.tree_estudiantes = ttk.Treeview(self.frame_principal, columns=columnas, show="headings")

        for columna in columnas:
            columna_formateada = columna.replace("_", " ").capitalize()
            self.tree_estudiantes.heading(columna, text=columna_formateada)

        self.tree_estudiantes.pack(pady=10)

        # Llenar el Treeview con los estudiantes existentes
        for estudiante in self.estudiantes:
            valores = [getattr(estudiante, columna) for columna in columnas]
            self.tree_estudiantes.insert("", "end", values=valores)

        # Botón para eliminar
        btn_eliminar = CTk.CTkButton(self.frame_principal, text="Eliminar Estudiante", command=self.eliminar_estudiante)
        btn_eliminar.pack(pady=20)

        # Botón para volver
        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_estudiantes)
        btn_volver.pack(pady=20)


    def eliminar_estudiante(self):
        # Obtener la selección del Treeview
        fila = self.tree_estudiantes.selection()

        # Verificar si hay selección
        if not fila:
            CTkM(title="Error", message="Debe seleccionar un estudiante para eliminar.", icon="cancel")
            return

        # Obtener los valores del estudiante seleccionado
        estudiante_id = fila[0]
        valores = self.tree_estudiantes.item(estudiante_id, "values")
        matricula = valores[2]  # La matrícula es el tercer valor (índice 3) en la fila

        # Confirmar la eliminación
        confirmacion = CTkM(title="Confirmación", message=f"¿Está seguro de que desea eliminar al estudiante con matrícula {matricula}?", icon="warning", option_1="Cancelar", option_2="Eliminar")
        
        if confirmacion.get() == "Eliminar":
            # Eliminar el estudiante de la lista
            for estudiante in self.estudiantes:
                if estudiante.matricula == matricula:
                    self.estudiantes.remove(estudiante)
                    break

            # Eliminar el estudiante del Treeview
            self.tree_estudiantes.delete(estudiante_id)

            # Mostrar mensaje de éxito
            CTkM(title="Éxito", message=f"Estudiante con matrícula {matricula} eliminado correctamente.", icon="info")

    def estudiar_materia(self):
        # Limpiar el frame y preparar el menú para estudiar una materia
        self.limpiar_frame()

        if not self.asignaturas:
            CTkM(title="Error", message="No hay asignaturas creadas.", icon="cancel")
            self.crear_menu_principal()
            return
        
        if not self.estudiantes:
            CTkM(title="Error", message="No hay estudiantes en el sistema.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Estudiar Materia", font=("Arial", 24))
        titulo.pack(pady=20)

        # Seleccionar el estudiante
        label_matricula = CTk.CTkLabel(self.frame_principal, text="Ingrese la matrícula del estudiante:")
        label_matricula.pack()
        self.entry_matricula_estudio = CTk.CTkEntry(self.frame_principal)
        self.entry_matricula_estudio.pack()

        # Mostrar asignaturas disponibles

        label_asignatura = CTk.CTkLabel(self.frame_principal, text="Seleccione una Asignatura:")
        label_asignatura.pack()

        # Lista de asignaturas disponibles
        self.asignatura_seleccionada = CTk.CTkComboBox(self.frame_principal, values=[asignatura.nombre for asignatura in self.asignaturas])
        self.asignatura_seleccionada.pack()

        # Ingresar horas de estudio
        label_horas = CTk.CTkLabel(self.frame_principal, text="Ingrese el número de horas:")
        label_horas.pack()
        self.entry_horas_estudio = CTk.CTkEntry(self.frame_principal)
        self.entry_horas_estudio.pack()

        # Botón para confirmar
        btn_estudiar = CTk.CTkButton(self.frame_principal, text="Estudiar", command=self.confirmar_estudio)
        btn_estudiar.pack(pady=20)

        # Botón para volver
        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_estudiantes)
        btn_volver.pack(pady=20)

# Confirmar el estudio de la materia
    def confirmar_estudio(self):
        matricula = self.entry_matricula_estudio.get()
        asignatura = self.asignatura_seleccionada.get()
        horas = self.entry_horas_estudio.get()

        estudiante = self.buscar_estudiante(matricula)
        if not estudiante:
            CTkM(title="Error", message=f"No se encontró un estudiante con matrícula {matricula}.", icon="cancel")
            return

        if not self.validar_numero(horas, "horas"):
            return

        CTkM(title="Éxito", message=f"{estudiante.estudiar(asignatura, horas)}", icon="info")

    def mostrar_informacion_estudiante(self):
        self.limpiar_frame()

        if not self.estudiantes:
            CTkM(title="Error", message="No hay estudiantes creados.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Información del Estudiante", font=("Arial", 24))
        titulo.pack(pady=20)

        # Seleccionar el estudiante por matrícula
        label_matricula = CTk.CTkLabel(self.frame_principal, text="Ingrese la matrícula del estudiante:")
        label_matricula.pack()
        self.entry_matricula_info = CTk.CTkEntry(self.frame_principal)
        self.entry_matricula_info.pack()

        btn_mostrar = CTk.CTkButton(self.frame_principal, text="Mostrar Información", command=self.mostrar_detalle_estudiante)
        btn_mostrar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_estudiantes)
        btn_volver.pack(pady=20)

    # Función para mostrar los detalles del estudiante
    def mostrar_detalle_estudiante(self):
        matricula = self.entry_matricula_info.get()
        estudiante = self.buscar_estudiante(matricula)

        if not estudiante:
            CTkM(title="Error", message=f"No se encontró un estudiante con matrícula {matricula}.", icon="cancel")
            return

        CTkM(title="Información del Estudiante", message=f"{estudiante.presentarse()}" ,icon="info")
        
    # Menú de profesores
    def menu_profesores(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Gestión de Profesores", font=("Arial", 24))
        titulo.pack(pady=20)

        btn_agregar_profesor = CTk.CTkButton(self.frame_principal, text="Agregar Profesor", command=self.crear_profesor)
        btn_agregar_profesor.pack(pady=10)

        btn_mostrar_profesores = CTk.CTkButton(self.frame_principal, text="Mostrar Profesores", command=self.mostrar_profesores)
        btn_mostrar_profesores.pack(pady=10)

        btn_ensenar_asignatura = CTk.CTkButton(self.frame_principal, text="Enseñar Asignatura", command=self.enseñar_asignatura)
        btn_ensenar_asignatura.pack(pady=10)

        btn_info_profesor = CTk.CTkButton(self.frame_principal, text="Mostrar Información del Profesor", command=self.mostrar_informacion_profesor)
        btn_info_profesor.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.crear_menu_principal)
        btn_volver.pack(pady=20)

    # Función para agregar un profesor
    def crear_profesor(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Agregar Profesor", font=("Arial", 24))
        titulo.pack(pady=20)

        label_nombre = CTk.CTkLabel(self.frame_principal, text="Nombre:")
        label_nombre.pack()
        self.entry_nombre_profesor = CTk.CTkEntry(self.frame_principal)
        self.entry_nombre_profesor.pack()

        label_n_empleado = CTk.CTkLabel(self.frame_principal, text="Número de Empleado:")
        label_n_empleado.pack()
        self.entry_n_empleado = CTk.CTkEntry(self.frame_principal)
        self.entry_n_empleado.pack()

        label_departamento = CTk.CTkLabel(self.frame_principal, text="Departamento:")
        label_departamento.pack()
        self.entry_departamento = CTk.CTkEntry(self.frame_principal)
        self.entry_departamento.pack()

        label_fnac = CTk.CTkLabel(self.frame_principal, text="Fecha de Nacimiento (DD/MM/AAAA):")
        label_fnac.pack()
        self.entry_fnac = CTk.CTkEntry(self.frame_principal)
        self.entry_fnac.pack()

        # Botón para guardar el profesor
        btn_guardar = CTk.CTkButton(self.frame_principal, text="Guardar Profesor", command=self.ingresar_profesor)
        btn_guardar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_profesores)
        btn_volver.pack(pady=20)

    def ingresar_profesor(self):
        nombre = self.entry_nombre_profesor.get()
        n_empleado = self.entry_n_empleado.get()
        departamento = self.entry_departamento.get()
        fnac = self.entry_fnac.get()

        for profesor in self.profesores:
            if profesor.n_empleado == n_empleado:
                CTkM(title="Error", message=f"Ya existe un profesor con número de empleado {n_empleado}.", icon="cancel")
                return

        if not all([nombre, n_empleado, departamento]):
            CTkM(title="Error", message="Todos los campos son obligatorios.", icon="cancel")
            return

        if not self.validar_str(departamento, "departamento"):
            return

        if not self.validar_str(nombre, "nombre"):
            return

        if not self.validar_numero(n_empleado, "número de empleado"):
            return

        if not self.validar_fecha(fnac):
            return
        nuevo_profesor = Profesor(nombre, fnac, n_empleado, departamento)
        self.profesores.append(nuevo_profesor)
        CTkM(title="Éxito", message=f"Profesor {nombre} agregado correctamente.", icon="check")

    def mostrar_profesores(self):
        self.limpiar_frame()

        if not self.profesores:
            CTkM(title="Error", message="No hay profesores registrados.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Lista de Profesores", font=("Arial", 24))
        titulo.pack(pady=20)

        columnas = list(vars(self.profesores[0]).keys())

        self.tree_profesores = ttk.Treeview(self.frame_principal, columns=columnas, show="headings")

        for columna in columnas:
            columna_formateada = columna.replace("_", " ").capitalize()
            self.tree_profesores.heading(columna, text=columna_formateada)

        self.tree_profesores.pack(pady=10)

        for profesor in self.profesores:
            valores = [getattr(profesor, columna) for columna in columnas]
            self.tree_profesores.insert("", "end", values=valores)

        btn_eliminar = CTk.CTkButton(self.frame_principal, text="Eliminar Profesor", command=self.eliminar_profesor)
        btn_eliminar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_profesores)
        btn_volver.pack(pady=20)

    def eliminar_profesor(self):
        fila = self.tree_profesores.selection()

        if not fila:
            CTkM(title="Error", message="Debe seleccionar un profesor para eliminar.", icon="cancel")
            return

        profesor_id = fila[0]
        valores = self.tree_profesores.item(profesor_id, "values")
        n_empleado = valores[2]  # lo mismo que con estudiantes

        confirmacion = CTkM(title="Confirmación", message=f"¿Está seguro de que desea eliminar al profesor con número de empleado {n_empleado}?", icon="warning", option_1="Cancelar", option_2="Eliminar")

        if confirmacion.get() == "Eliminar":
            for profesor in self.profesores:
                if profesor.n_empleado == n_empleado:
                    self.profesores.remove(profesor)
                    break

            self.tree_profesores.delete(profesor_id)
            CTkM(title="Éxito", message=f"Profesor con número de empleado {n_empleado} eliminado correctamente.", icon="info")

    def enseñar_asignatura(self):
        self.limpiar_frame()

        if not self.asignaturas:
            CTkM(title="Error", message="No hay asignaturas creadas.", icon="cancel")
            self.crear_menu_principal()
            return

        if not self.profesores:
            CTkM(title="Error", message="No hay profesores en el sistema.", icon="cancel")
            self.crear_menu_principal()
            return
        
        titulo = CTk.CTkLabel(self.frame_principal, text="Enseñar Asignatura", font=("Arial", 24))
        titulo.pack(pady=20)

        label_n_empleado = CTk.CTkLabel(self.frame_principal, text="Ingrese el número de empleado del profesor:")
        label_n_empleado.pack()
        self.entry_n_empleado_ensenar = CTk.CTkEntry(self.frame_principal)
        self.entry_n_empleado_ensenar.pack()

        label_asignatura = CTk.CTkLabel(self.frame_principal, text="Seleccione una Asignatura:")
        label_asignatura.pack()
        self.asignatura_seleccionada_profesor = CTk.CTkComboBox(self.frame_principal, values=[asignatura.nombre for asignatura in self.asignaturas])
        self.asignatura_seleccionada_profesor.pack()

        label_horas = CTk.CTkLabel(self.frame_principal, text="Ingrese el número de horas:")
        label_horas.pack()
        self.entry_horas_enseñar = CTk.CTkEntry(self.frame_principal)
        self.entry_horas_enseñar.pack()

        btn_ensenar = CTk.CTkButton(self.frame_principal, text="Enseñar", command=self.confirmar_enseñanza)
        btn_ensenar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_profesores)
        btn_volver.pack(pady=20)

    def confirmar_enseñanza(self):
        n_empleado = self.entry_n_empleado_ensenar.get()
        asignatura = self.asignatura_seleccionada_profesor.get()
        horas = self.entry_horas_enseñar.get()

        profesor = self.buscar_profesor(n_empleado)
        if not profesor:
            CTkM(title="Error", message=f"No se encontró un profesor con número de empleado {n_empleado}.", icon="cancel")
            return

        if not self.validar_numero(horas, "horas"):
            return
        
        CTkM(title="Éxito", message=f"{profesor.enseñar(asignatura, horas)}", icon="info")

    def mostrar_informacion_profesor(self):
        self.limpiar_frame()

        if not self.profesores:
            CTkM(title="Error", message="No hay profesores registrados.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Información del Profesor", font=("Arial", 24))
        titulo.pack(pady=20)

        # Seleccionar el profesor por número de empleado
        label_n_empleado = CTk.CTkLabel(self.frame_principal, text="Ingrese el número de empleado del profesor:")
        label_n_empleado.pack()
        self.entry_n_empleado_info = CTk.CTkEntry(self.frame_principal)
        self.entry_n_empleado_info.pack()

        btn_mostrar = CTk.CTkButton(self.frame_principal, text="Mostrar Información", command=self.mostrar_detalle_profesor)
        btn_mostrar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_profesores)
        btn_volver.pack(pady=20)

    # Función para mostrar los detalles del profesor
    def mostrar_detalle_profesor(self):
        n_empleado = self.entry_n_empleado_info.get()
        profesor = self.buscar_profesor(n_empleado)

        if not profesor:
            CTkM(title="Error", message=f"No se encontró un profesor con número de empleado {n_empleado}.", icon="cancel")
            return

        # Mostrar los detalles del profesor en un cuadro de mensaje
        CTkM(title="Información del Profesor", message=f"{profesor.presentarse()}",icon="info")

    # Menú de asignaturas
    def menu_asignaturas(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Gestión de Asignaturas", font=("Arial", 24))
        titulo.pack(pady=20)

        btn_agregar_asignatura = CTk.CTkButton(self.frame_principal, text="Agregar Asignatura", command=self.crear_asignatura)
        btn_agregar_asignatura.pack(pady=10)

        btn_mostrar_asignaturas = CTk.CTkButton(self.frame_principal, text="Mostrar Asignaturas", command=self.mostrar_asignaturas)
        btn_mostrar_asignaturas.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.crear_menu_principal)
        btn_volver.pack(pady=20)

    def crear_asignatura(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Agregar Asignatura", font=("Arial", 24))
        titulo.pack(pady=20)

        label_codigo = CTk.CTkLabel(self.frame_principal, text="Código de la Asignatura:")
        label_codigo.pack()
        self.entry_codigo_asignatura = CTk.CTkEntry(self.frame_principal)
        self.entry_codigo_asignatura.pack()

        label_nombre = CTk.CTkLabel(self.frame_principal, text="Nombre de la Asignatura:")
        label_nombre.pack()
        self.entry_nombre_asignatura = CTk.CTkEntry(self.frame_principal)
        self.entry_nombre_asignatura.pack()

        label_creditos = CTk.CTkLabel(self.frame_principal, text="Créditos:")
        label_creditos.pack()
        self.entry_creditos_asignatura = CTk.CTkEntry(self.frame_principal)
        self.entry_creditos_asignatura.pack()

        btn_guardar = CTk.CTkButton(self.frame_principal, text="Guardar Asignatura", command=self.ingresar_asignatura)
        btn_guardar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_asignaturas)
        btn_volver.pack(pady=20)

    # Función para ingresar la asignatura
    def ingresar_asignatura(self):
        codigo = self.entry_codigo_asignatura.get()
        nombre = self.entry_nombre_asignatura.get()
        creditos = self.entry_creditos_asignatura.get()

        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                CTkM(title="Error", message=f"Ya existe una asignatura con el código {codigo}.", icon="cancel")
                return
            
        # Validar los datos
        if not all([codigo, nombre, creditos]):
            CTkM(title="Error", message="Todos los campos son obligatorios.", icon="cancel")
            return

        if not self.validar_numero(creditos, "créditos"):
            return

        # Crear la nueva asignatura
        nueva_asignatura = Asignatura(nombre, codigo, creditos)
        self.asignaturas.append(nueva_asignatura)
        CTkM(title="Éxito", message=f"Asignatura {nombre} agregada correctamente.", icon="check")

    def mostrar_asignaturas(self):
        self.limpiar_frame()

        if not self.asignaturas:
            CTkM(title="Error", message="No hay asignaturas registradas.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Lista de Asignaturas", font=("Arial", 24))
        titulo.pack(pady=20)

        columnas = list(vars(self.asignaturas[0]).keys())

        self.tree_asignaturas = ttk.Treeview(self.frame_principal, columns=columnas, show="headings")

        for columna in columnas:
            columna_formateada = columna.replace("_", " ").capitalize()
            self.tree_asignaturas.heading(columna, text=columna_formateada)

        self.tree_asignaturas.pack(pady=10)

        for asignatura in self.asignaturas:
            valores = [getattr(asignatura, columna) for columna in columnas]
            self.tree_asignaturas.insert("", "end", values=valores)

        btn_eliminar = CTk.CTkButton(self.frame_principal, text="Eliminar Asignatura", command=self.eliminar_asignatura)
        btn_eliminar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_asignaturas)
        btn_volver.pack(pady=20)

    def eliminar_asignatura(self):
        fila = self.tree_asignaturas.selection()

        if not fila:
            CTkM(title="Error", message="Debe seleccionar una asignatura para eliminar.", icon="cancel")
            return

        asignatura_id = fila[0]
        valores = self.tree_asignaturas.item(asignatura_id, "values")
        codigo = valores[1]  # El código de la asignatura está en el segundo valor

        confirmacion = CTkM(title="Confirmación", message=f"¿Está seguro de que desea eliminar la asignatura con código {codigo}?", icon="warning", option_1="Cancelar", option_2="Eliminar")

        if confirmacion.get() == "Eliminar":
            for asignatura in self.asignaturas:
                if asignatura.codigo == codigo:
                    self.asignaturas.remove(asignatura)
                    break

            self.tree_asignaturas.delete(asignatura_id)
            CTkM(title="Éxito", message=f"Asignatura con código {codigo} eliminada correctamente.", icon="info")

    # Menú de grupos
    def menu_grupos(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Gestión de Grupos", font=("Arial", 24))
        titulo.pack(pady=20)

        btn_agregar_grupo = CTk.CTkButton(self.frame_principal, text="Crear Grupo", command=self.crear_grupo)
        btn_agregar_grupo.pack(pady=10)

        btn_mostrar_grupos = CTk.CTkButton(self.frame_principal, text="Mostrar Grupos", command=self.mostrar_grupos)
        btn_mostrar_grupos.pack(pady=10)

        btn_gestionar_estudiantes = CTk.CTkButton(self.frame_principal, text="Gestionar Estudiantes del Grupo", command=self.gestionar_estudiantes_grupo)
        btn_gestionar_estudiantes.pack(pady=10)

        btn_gestionar_estudiantes = CTk.CTkButton(self.frame_principal, text="Gestionar Asignaturas del Grupo", command=self.gestionar_asignaturas_grupo)
        btn_gestionar_estudiantes.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.crear_menu_principal)
        btn_volver.pack(pady=20)

    def crear_grupo(self):
        self.limpiar_frame()

        if not self.asignaturas:
            CTkM(title="Error", message="No hay asignaturas creadas.", icon="cancel")
            self.crear_menu_principal()
            return

        if not self.profesores:
            CTkM(title="Error", message="No hay profesores en el sistema.", icon="cancel")
            self.crear_menu_principal()
            return
        
        titulo = CTk.CTkLabel(self.frame_principal, text="Crear Grupo", font=("Arial", 24))
        titulo.pack(pady=20)

        label_ngrupo = CTk.CTkLabel(self.frame_principal, text="Número de Grupo:")
        label_ngrupo.pack()
        self.entry_ngrupo = CTk.CTkEntry(self.frame_principal)
        self.entry_ngrupo.pack()

        label_asignatura = CTk.CTkLabel(self.frame_principal, text="Código de la Asignatura:")
        label_asignatura.pack()
        self.entry_asignatura = CTk.CTkEntry(self.frame_principal)
        self.entry_asignatura.pack()

        label_profesor = CTk.CTkLabel(self.frame_principal, text="Número de Empleado del Profesor:")
        label_profesor.pack()
        self.entry_profesor = CTk.CTkEntry(self.frame_principal)
        self.entry_profesor.pack()

        btn_guardar_grupo = CTk.CTkButton(self.frame_principal, text="Guardar Grupo", command=self.ingresar_grupo)
        btn_guardar_grupo.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_grupos)
        btn_volver.pack(pady=20)

    # Función para ingresar el grupo
    def ingresar_grupo(self):
        ngrupo = self.entry_ngrupo.get()
        codigo_asignatura = self.entry_asignatura.get()
        n_empleado = self.entry_profesor.get()

        # Validaciones
        if not all([ngrupo, codigo_asignatura, n_empleado]):
            CTkM(title="Error", message="Todos los campos son obligatorios.", icon="cancel")
            return

        if not self.validar_numero(ngrupo, "Número de Grupo"):
            return

        if not self.validar_numero(n_empleado, "Número de Empleado"):
            return
        
        # Verificar si el grupo ya existe
        for grupo in self.grupos:
            if grupo.ngrupo == ngrupo:
                CTkM(title="Error", message=f"El grupo con número {ngrupo} ya existe.", icon="cancel")
                return

        # Buscar asignatura y profesor
        asignatura = self.buscar_asignatura(codigo_asignatura)
        profesor = self.buscar_profesor(n_empleado)

        if not asignatura or not profesor:
            CTkM(title="Error", message="Asignatura o Profesor no encontrado.", icon="cancel")
            return

        # Crear el nuevo grupo
        nuevo_grupo = Grupo(ngrupo, asignatura, profesor)
        self.grupos.append(nuevo_grupo)
        CTkM(title="Éxito", message=f"Grupo {ngrupo} creado correctamente.", icon="check")

    def mostrar_grupos(self):
        self.limpiar_frame()

        if not self.grupos:
            CTkM(title="Error", message="No hay grupos creados.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Lista de Grupos", font=("Arial", 24))
        titulo.pack(pady=20)

        columnas = ["Número de Grupo", "Asignatura Instanciada", "Profesor"]

        self.tree_grupos = ttk.Treeview(self.frame_principal, columns=columnas, show="headings")

        for columna in columnas:
            self.tree_grupos.heading(columna, text=columna)

        self.tree_grupos.pack(pady=10)

        for grupo in self.grupos:
            valores = [grupo.ngrupo, grupo.asignatura.nombre, grupo.profesor.nombre]
            self.tree_grupos.insert("", "end", values=valores)

        btn_mostrar_detalles = CTk.CTkButton(self.frame_principal, text="Mostrar Detalles", command=self.mostrar_detalles_grupo)
        btn_mostrar_detalles.pack(pady=20)

        btn_mostrar_detalles = CTk.CTkButton(self.frame_principal, text="Eliminar Grupo", command=self.eliminar_grupo)
        btn_mostrar_detalles.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_grupos)
        btn_volver.pack(pady=20)

    def mostrar_detalles_grupo(self):
        # Obtener selección del Treeview
        seleccion = self.tree_grupos.selection()

        if not seleccion:
            CTkM(title="Error", message="Debe seleccionar un grupo para ver los detalles.", icon="cancel")
            return

        grupo_id = seleccion[0]
        valores = self.tree_grupos.item(grupo_id, "values")
        ngrupo = valores[0]

        grupo = self.buscar_grupo(ngrupo)

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo}.", icon="cancel")
            return
        # Mostrar los detalles en un cuadro de diálogo
        CTkM(title="Detalles del Grupo", message=f"{grupo.mostrar_info()}", icon="info")

    def eliminar_grupo(self):
        seleccion = self.tree_grupos.selection()

        if not seleccion:
            CTkM(title="Error", message="Debe seleccionar un grupo para eliminar.", icon="cancel")
            return

        grupo_id = seleccion[0]
        valores = self.tree_grupos.item(grupo_id, "values")
        ngrupo = valores[0]

        grupo = self.buscar_grupo(ngrupo)

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo}.", icon="cancel")
            return

        # Eliminar el grupo de la lista y del Treeview
        self.grupos.remove(grupo)
        self.tree_grupos.delete(grupo_id)
        CTkM(title="Éxito", message=f"Grupo {ngrupo} eliminado correctamente.", icon="info")

    def gestionar_estudiantes_grupo(self):
        self.limpiar_frame()

        if not self.grupos:
            CTkM(title="Error", message="No hay grupos creados.", icon="cancel")
            self.crear_menu_principal()
            return
        
        if not self.estudiantes:
            CTkM(title="Error", message="No hay estudiantes en el sistema.", icon="cancel")
            self.crear_menu_principal()
            return
        
        titulo = CTk.CTkLabel(self.frame_principal, text="Gestionar Estudiantes en Grupo", font=("Arial", 24))
        titulo.pack(pady=20)

        label_ngrupo = CTk.CTkLabel(self.frame_principal, text="Número de Grupo:")
        label_ngrupo.pack()
        self.entry_ngrupo_gestion = CTk.CTkEntry(self.frame_principal)
        self.entry_ngrupo_gestion.pack()

        label_matricula = CTk.CTkLabel(self.frame_principal, text="Matrícula del Estudiante:")
        label_matricula.pack()
        self.entry_matricula_gestion = CTk.CTkEntry(self.frame_principal)
        self.entry_matricula_gestion.pack()

        btn_agregar_estudiante = CTk.CTkButton(self.frame_principal, text="Agregar Estudiante", command=self.agregar_estudiante_grupo)
        btn_agregar_estudiante.pack(pady=10)

        btn_eliminar_estudiante = CTk.CTkButton(self.frame_principal, text="Eliminar Estudiante", command=self.eliminar_estudiante_grupo)
        btn_eliminar_estudiante.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_grupos)
        btn_volver.pack(pady=20)

    # Agregar estudiante a grupo
    def agregar_estudiante_grupo(self):
        ngrupo = self.entry_ngrupo_gestion.get()
        matricula = self.entry_matricula_gestion.get()

        grupo = self.buscar_grupo(ngrupo)
        estudiante = self.buscar_estudiante(matricula)

        if estudiante in grupo.estudiantes:
            CTkM(title="Error", message=f"El estudiante con matrícula {matricula} ya está en el grupo {ngrupo}.", icon="cancel")
            return

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo}.", icon="cancel")
            return

        if not estudiante:
            CTkM(title="Error", message=f"No se encontró un estudiante con matrícula {matricula}.", icon="cancel")
            return
        
        CTkM(title="Éxito", message=f"{grupo.agregar_estudiante(estudiante)}", icon="check")

    # Eliminar estudiante de grupo
    def eliminar_estudiante_grupo(self):
        ngrupo = self.entry_ngrupo_gestion.get()
        matricula = self.entry_matricula_gestion.get()

        grupo = self.buscar_grupo(ngrupo)

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo}.", icon="cancel")
            return

        estudiante = self.buscar_estudiante(matricula)
        if not estudiante:
            CTkM(title="Error", message=f"No se encontró un estudiante con matrícula {matricula}.", icon="cancel")
            return

        # Confirmación antes de eliminar
        confirmacion = CTkM(title="Confirmación", message=f"¿Está seguro de que desea eliminar al estudiante {estudiante.nombre}, Matricula: {estudiante.matricula} del grupo {ngrupo}?", icon="warning", option_1="Cancelar", option_2="Eliminar")
        
        if confirmacion.get() == "Eliminar":
            # Verificar si el estudiante está en el grupo
            if estudiante not in grupo.estudiantes:
                CTkM(title="Error", message=f"El estudiante con matrícula {matricula} no está en el grupo {ngrupo}.", icon="cancel")
                return
            # Eliminar el estudiante del grupo
            CTkM(title="Éxito", message=f"{grupo.eliminar_estudiante(matricula)}", icon="info")


    def gestionar_asignaturas_grupo(self):
        self.limpiar_frame()

        if not self.grupos:
            CTkM(title="Error", message="No hay grupos creados.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Gestión de Asignaturas en Grupos", font=("Arial", 24))
        titulo.pack(pady=20)

        label_ngrupo = CTk.CTkLabel(self.frame_principal, text="Número de Grupo:")
        label_ngrupo.pack()
        self.entry_ngrupo_asignaturas = CTk.CTkEntry(self.frame_principal)
        self.entry_ngrupo_asignaturas.pack()

        label_asignatura = CTk.CTkLabel(self.frame_principal, text="Código de la Asignatura:")
        label_asignatura.pack()
        self.entry_asignatura = CTk.CTkEntry(self.frame_principal)
        self.entry_asignatura.pack()

        btn_agregar_asignatura = CTk.CTkButton(self.frame_principal, text="Agregar Asignatura", command=self.agregar_asignatura_grupo)
        btn_agregar_asignatura.pack(pady=10)

        btn_eliminar_asignatura = CTk.CTkButton(self.frame_principal, text="Eliminar Asignatura", command=self.eliminar_asignatura_grupo)
        btn_eliminar_asignatura.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_grupos)
        btn_volver.pack(pady=20)

    def agregar_asignatura_grupo(self):
        ngrupo = self.entry_ngrupo_asignaturas.get()
        codigo_asignatura = self.entry_asignatura.get()

        grupo = self.buscar_grupo(ngrupo)

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo}.", icon="cancel")
            return

        asignatura = self.buscar_asignatura(codigo_asignatura)

        if not asignatura:
            CTkM(title="Error", message=f"No se encontró la asignatura con código {codigo_asignatura}.", icon="cancel")
            return
        
        if asignatura in grupo.lista_asignaturas:
            CTkM(title="Error", message=f"La asignatura con código {codigo_asignatura} ya está en el grupo {ngrupo}.", icon="cancel")
            return
        
        CTkM(title="Éxito", message=f"{grupo.agregar_asignatura(asignatura)}", icon="check")  

    def eliminar_asignatura_grupo(self):
        ngrupo = self.entry_ngrupo_asignaturas.get()
        codigo_asignatura = self.entry_asignatura.get()

        grupo = self.buscar_grupo(ngrupo)

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo}.", icon="cancel")
            return

        asignatura = self.buscar_asignatura(codigo_asignatura)
        if not asignatura:
            CTkM(title="Error", message=f"No se encontró la asignatura con código {codigo_asignatura}.", icon="cancel")
            return

        # Confirmación antes de eliminar
        confirmacion = CTkM(title="Confirmación", message=f"¿Está seguro de que desea eliminar la asignatura {asignatura.nombre} del grupo {ngrupo}?", icon="warning", option_1="Cancelar", option_2="Eliminar")
        
        if confirmacion.get() == "Eliminar":
            # Verificar si la asignatura está en el grupo
            if asignatura not in grupo.lista_asignaturas:
                CTkM(title="Error", message=f"La asignatura con código {codigo_asignatura} no está en el grupo {ngrupo}.", icon="cancel")
                return

            # Eliminar la asignatura del grupo
            CTkM(title="Éxito", message=f"{grupo.eliminar_asignatura(codigo_asignatura)}", icon="info")

    # Menú de programas académicos
    def menu_programas(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Gestión de Programas Académicos", font=("Arial", 24))
        titulo.pack(pady=20)

        btn_agregar_programa = CTk.CTkButton(self.frame_principal, text="Crear Programa Académico", command=self.crear_programa_academico)
        btn_agregar_programa.pack(pady=10)

        btn_mostrar_programas = CTk.CTkButton(self.frame_principal, text="Mostrar Programas", command=self.mostrar_programas)
        btn_mostrar_programas.pack(pady=10)

        btn_gestionar_grupos_programa = CTk.CTkButton(self.frame_principal, text="Gestionar Grupos en Programas", command=self.menu_gestion_grupos_programa)
        btn_gestionar_grupos_programa.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.crear_menu_principal)
        btn_volver.pack(pady=20)

    def crear_programa_academico(self):
        self.limpiar_frame()

        titulo = CTk.CTkLabel(self.frame_principal, text="Crear Programa Académico", font=("Arial", 24))
        titulo.pack(pady=20)

        label_nombre_programa = CTk.CTkLabel(self.frame_principal, text="Nombre del Programa:")
        label_nombre_programa.pack()
        self.entry_nombre_programa = CTk.CTkEntry(self.frame_principal)
        self.entry_nombre_programa.pack()

        label_codigo_programa = CTk.CTkLabel(self.frame_principal, text="Código del Programa:")
        label_codigo_programa.pack()
        self.entry_codigo_programa = CTk.CTkEntry(self.frame_principal)
        self.entry_codigo_programa.pack()

        btn_guardar_programa = CTk.CTkButton(self.frame_principal, text="Guardar Programa", command=self.ingresar_programa_academico)
        btn_guardar_programa.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_programas)
        btn_volver.pack(pady=20)

    # Función para ingresar el programa académico
    def ingresar_programa_academico(self):
        nombre_programa = self.entry_nombre_programa.get()
        codigo_programa = self.entry_codigo_programa.get()

        # Validaciones
        if not all([nombre_programa, codigo_programa]):
            CTkM(title="Error", message="Todos los campos son obligatorios.", icon="cancel")
            return
        
        if not self.validar_numero(codigo_programa, "código del programa"):
            return
        # Verificar si el programa ya existe
        for programa in self.programas:
            if programa.codigo == codigo_programa:
                CTkM(title="Error", message=f"El programa con código {codigo_programa} ya existe.", icon="cancel")
                return

        # Crear el nuevo programa académico
        nuevo_programa = ProgramaAcademico(nombre_programa, codigo_programa)
        self.programas.append(nuevo_programa)
        CTkM(title="Éxito", message=f"Programa {nombre_programa} creado correctamente.", icon="check")

    def mostrar_programas(self):
        self.limpiar_frame()

        if not self.programas:
            CTkM(title="Error", message="No hay programas académicos creados.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Lista de Programas Académicos", font=("Arial", 24))
        titulo.pack(pady=20)

        columnas = ["Código del Programa", "Nombre del Programa"]

        self.tree_programas = ttk.Treeview(self.frame_principal, columns=columnas, show="headings")
    
        for columna in columnas:
            self.tree_programas.heading(columna, text=columna)

        self.tree_programas.pack(pady=10)

        for programa in self.programas:
            valores = [programa.codigo, programa.nombre]
            self.tree_programas.insert("", "end", values=valores)

        btn_mostrar_detalles = CTk.CTkButton(self.frame_principal, text="Mostrar Detalles", command=self.mostrar_detalles_programa)
        btn_mostrar_detalles.pack(pady=10)

        btn_eliminar_programa = CTk.CTkButton(self.frame_principal, text="Eliminar Programa", command=self.eliminar_programa)
        btn_eliminar_programa.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_programas)
        btn_volver.pack(pady=20)

    def mostrar_detalles_programa(self):
        seleccion = self.tree_programas.selection()

        if not seleccion:
            CTkM(title="Error", message="Debe seleccionar un programa académico para ver los detalles.", icon="cancel")
            return

        programa_id = seleccion[0]
        valores = self.tree_programas.item(programa_id, "values")
        codigo_programa = valores[0]

        programa = self.buscar_programa(codigo_programa)

        if not programa:
            CTkM(title="Error", message=f"No se encontró el programa con código {codigo_programa}.", icon="cancel")
            return

        CTkM(title="Detalles del Programa Académico", message=f"{programa.mostrar_info()}", icon="info")

    def eliminar_programa(self):
        seleccion = self.tree_programas.selection()

        if not seleccion:
            CTkM(title="Error", message="Debe seleccionar un programa académico para eliminar.", icon="cancel")
            return

        programa_id = seleccion[0]
        valores = self.tree_programas.item(programa_id, "values")
        codigo_programa = valores[0]

        programa = self.buscar_programa(codigo_programa)

        if not programa:
            CTkM(title="Error", message=f"No se encontró el programa con código {codigo_programa}.", icon="cancel")
            return

        # Confirmación antes de eliminar
        confirmacion = CTkM(title="Confirmación", message=f"¿Está seguro de que desea eliminar el programa {programa.nombre}?", icon="warning", option_1="Cancelar", option_2="Eliminar")
        
        if confirmacion.get() == "Eliminar":
            # Eliminar el programa de la lista y del Treeview
            self.programas.remove(programa)
            self.tree_programas.delete(programa_id)
            CTkM(title="Éxito", message=f"Programa {programa.nombre} eliminado correctamente.", icon="info")

    def menu_gestion_grupos_programa(self):
        self.limpiar_frame()

        if not self.programas:
            CTkM(title="Error", message="No hay programas académicos creados.", icon="cancel")
            self.crear_menu_principal()
            return
        
        if not self.grupos:
            CTkM(title="Error", message="No hay grupos creados.", icon="cancel")
            self.crear_menu_principal()
            return

        titulo = CTk.CTkLabel(self.frame_principal, text="Gestión de Grupos en Programas", font=("Arial", 24))
        titulo.pack(pady=20)

        label_codigo_programa = CTk.CTkLabel(self.frame_principal, text="Código del Programa:")
        label_codigo_programa.pack()
        self.entry_codigo_programa_grupos = CTk.CTkEntry(self.frame_principal)
        self.entry_codigo_programa_grupos.pack()

        label_ngrupo = CTk.CTkLabel(self.frame_principal, text="Número de Grupo:")
        label_ngrupo.pack()
        self.entry_ngrupo_programa = CTk.CTkEntry(self.frame_principal)
        self.entry_ngrupo_programa.pack()

        btn_agregar_grupo_programa = CTk.CTkButton(self.frame_principal, text="Agregar Grupo", command=self.agregar_grupo_programa)
        btn_agregar_grupo_programa.pack(pady=10)

        btn_eliminar_grupo_programa = CTk.CTkButton(self.frame_principal, text="Eliminar Grupo", command=self.eliminar_grupo_programa)
        btn_eliminar_grupo_programa.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_programas)
        btn_volver.pack(pady=20)

    def agregar_grupo_programa(self):
        codigo_programa = self.entry_codigo_programa_grupos.get()
        ngrupo = self.entry_ngrupo_programa.get()

        programa = self.buscar_programa(codigo_programa)

        if not programa:
            CTkM(title="Error", message=f"No se encontró el programa con código {codigo_programa}.", icon="cancel")
            return

        grupo = self.buscar_grupo(ngrupo)

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo}.", icon="cancel")
            return

        if grupo in programa.grupos:
            CTkM(title="Error", message=f"El grupo con número {ngrupo} ya está en el programa {programa.nombre}.", icon="cancel")
            return
        
        CTkM(title="Éxito", message=f"{programa.agregar_grupo(grupo)}.", icon="check")

    def eliminar_grupo_programa(self):
        codigo_programa = self.entry_codigo_programa_grupos.get()
        ngrupo = self.entry_ngrupo_programa.get()

        # Buscar el programa académico
        programa = self.buscar_programa(codigo_programa)

        if not programa:
            CTkM(title="Error", message=f"No se encontró el programa con código {codigo_programa}.", icon="cancel")
            return

        # Buscar el grupo dentro del programa
        grupo = self.buscar_grupo(ngrupo)

        if not grupo:
            CTkM(title="Error", message=f"No se encontró el grupo con número {ngrupo} en el programa {programa.nombre}.", icon="cancel")
            return

        # Confirmación antes de eliminar
        confirmacion = CTkM(title="Confirmación", message=f"¿Está seguro de que desea eliminar el grupo {ngrupo} del programa {programa.nombre}?", icon="warning", option_1="Cancelar", option_2="Eliminar")

        if confirmacion.get() == "Eliminar":
            # Eliminar el grupo del programa
            CTkM(title="Éxito", message=f"{programa.eliminar_grupo(ngrupo)}", icon="info")

    # Métodos auxiliares para buscar asignaturas y profesores
    def buscar_programa(self, codigo):
        for programa in self.programas:
            if programa.codigo == codigo:
                return programa
        return None

    def buscar_asignatura(self, codigo_asignatura):
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo_asignatura:
                return asignatura
        return None

    def buscar_profesor(self, n_empleado):
        for profesor in self.profesores:
            if profesor.n_empleado == n_empleado:
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
    
    # Función para limpiar el frame principal antes de mostrar un nuevo menú
    def limpiar_frame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    # Función para validar cadenas de texto
    def validar_str(self, valor, atributo):
        if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚüÜñÑ\s]+$", valor):
            CTkM(title="Error", message=f"Para ingresar {atributo} es necesario que sean solo caracteres validos.", icon="cancel")
            return False
        return True

    # Función para validar números positivos
    def validar_numero(self, valor, atributo):
        if not valor.isdigit() or int(valor) <= 0:
            CTkM(title="Error", message=f"Para ingresar {atributo} es necesario que sean números positivos.", icon="cancel")
            return False
        return True

    # Validar la fecha de nacimiento en formato DD/MM/AAAA
    def validar_fecha(self, fnac):
        try:
            fecha_nac = datetime.strptime(fnac, "%d/%m/%Y")
            fecha_actual = datetime.now()

            if fecha_nac > fecha_actual:
                CTkM(title="Error", message="La fecha de nacimiento no puede ser en el futuro.", icon="cancel")
                return False

            return True
        except ValueError:
            CTkM(title="Error", message="La fecha de nacimiento debe tener el formato DD/MM/AAAA.", icon="cancel")
            return False
    

if __name__ == "__main__":
    app = SistemaGestionUniversitariaApp()
    app.mainloop()
