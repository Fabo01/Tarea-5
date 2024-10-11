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

        # btn_profesores = CTk.CTkButton(self.frame_principal, text="Gestionar Profesores", command=self.menu_profesores)
        # btn_profesores.pack(pady=10)

        # btn_asignaturas = CTk.CTkButton(self.frame_principal, text="Gestionar Asignaturas", command=self.menu_asignaturas)
        # btn_asignaturas.pack(pady=10)

        # btn_grupos = CTk.CTkButton(self.frame_principal, text="Gestionar Grupos", command=self.menu_grupos)
        # btn_grupos.pack(pady=10)

        # btn_programas = CTk.CTkButton(self.frame_principal, text="Gestionar Programas Académicos", command=self.menu_programas)
        # btn_programas.pack(pady=10)
        
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

    def estudiar_materia(self):
        # Limpiar el frame y preparar el menú para estudiar una materia
        self.limpiar_frame()

        if not self.asignaturas:
            CTkM(title="Error", message="No hay asignaturas creadas.", icon="cancel")
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

        estudiante.estudiar(asignatura, int(horas))
        CTkM(title="Éxito", message=f"{estudiante.nombre} ha estudiado {asignatura} durante {horas} horas.", icon="info")

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

        CTkM(
            title="Información del Estudiante",
            message=f"Nombre: {estudiante.nombre}\n"
                    f"Matrícula: {estudiante.matricula}\n"
                    f"Carrera: {estudiante.carrera}\n"
                    f"Semestre: {estudiante.semestre}\n"
                    f"Edad: {estudiante.calcular_edad()}",
            icon="info"
        )


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
            datetime.strptime(fnac, "%d/%m/%Y")
            return True
        except ValueError:
            CTkM(title="Error", message="La fecha de nacimiento debe tener el formato DD/MM/AAAA.", icon="cancel")
            return False    

if __name__ == "__main__":
    app = SistemaGestionUniversitariaApp()
    app.mainloop()
