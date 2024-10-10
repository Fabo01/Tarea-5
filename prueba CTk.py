import customtkinter as CTk
from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico
import re
from datetime import datetime
from CTkMessagebox import CTkMessagebox as CTkM

class SistemaGestionUniversitariaApp(CTk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Sistema de Gestión Universitaria")
        self.geometry("800x600")

        # Datos
        self.estudiantes = []
        self.profesores = []
        self.asignaturas = []
        self.grupos = []
        self.programas = []

        # Crear el menú principal
        self.crear_menu_principal()

    def crear_menu_principal(self):
        # Crear el contenedor principal
        self.frame_principal = CTk.CTkFrame(self)
        self.frame_principal.pack(pady=20, padx=20, fill="both", expand=True)

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

        btn_agregar_estudiante = CTk.CTkButton(self.frame_principal, text="Agregar Estudiante", command=self.agregar_estudiante)
        btn_agregar_estudiante.pack(pady=10)

        btn_mostrar_estudiantes = CTk.CTkButton(self.frame_principal, text="Mostrar Estudiantes", command=self.mostrar_estudiantes)
        btn_mostrar_estudiantes.pack(pady=10)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.crear_menu_principal)
        btn_volver.pack(pady=20)

    # Función para agregar un estudiante (ventana adicional)
    def agregar_estudiante(self):
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
        btn_guardar = CTk.CTkButton(self.frame_principal, text="Guardar Estudiante", command=self.guardar_estudiante)
        btn_guardar.pack(pady=20)

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_estudiantes)
        btn_volver.pack(pady=20)

    def guardar_estudiante(self):
        nombre = self.entry_nombre.get()
        matricula = self.entry_matricula.get()
        carrera = self.entry_carrera.get()
        semestre = self.entry_semestre.get()
        fnac = self.entry_fnac.get()

        # Validar los datos utilizando las funciones
        if not all([nombre, matricula, carrera, semestre, fnac]):
            CTkM(title="Error", message="Todos los campos son obligatorios.", icon="error")
            return

        if not self.validar_nombre(nombre):
            return

        if not self.validar_matricula(matricula):
            return

        if not self.validar_semestre(semestre):
            return

        if not self.validar_fecha(fnac):
            return

        # Validación de duplicados por matrícula
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                CTkM(title="Error", message=f"Estudiante con matrícula {matricula} ya registrado.", icon="error")
                return

        # Si todas las validaciones son correctas, crear el nuevo estudiante
        nuevo_estudiante = Estudiante(nombre, fnac, matricula, carrera, semestre)
        self.estudiantes.append(nuevo_estudiante)
        CTkM(title="Éxito", message=f"Estudiante {nombre} agregado correctamente.", icon="info")

    # Función para mostrar los estudiantes
    def mostrar_estudiantes(self):
        self.limpiar_frame()
        titulo = CTk.CTkLabel(self.frame_principal, text="Lista de Estudiantes", font=("Arial", 24))
        titulo.pack(pady=20)

        if not self.estudiantes:
            CTk.CTkLabel(self.frame_principal, text="No hay estudiantes registrados.", text_color="red").pack()
        else:
            for estudiante in self.estudiantes:
                CTk.CTkLabel(self.frame_principal, text=f"{estudiante.nombre} - {estudiante.matricula}").pack()

        btn_volver = CTk.CTkButton(self.frame_principal, text="Volver", command=self.menu_estudiantes)
        btn_volver.pack(pady=20)

    # Función para limpiar el frame principal antes de mostrar un nuevo menú
    def limpiar_frame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def validar_nombre(self, nombre):
        if not re.match(r"^[A-Za-z\s]+$", nombre):
            CTkM(title="Error", message="El nombre solo puede contener letras.", icon="error")
            return False
        return True

# Validar que la matrícula sea numérica
    def validar_matricula(self, matricula):
        if not matricula.isdigit():
            CTkM(title="Error", message="La matrícula debe ser un número.", icon="error")
            return False
        return True

    # Validar que el semestre sea un número entero
    def validar_semestre(self, semestre):
        if not semestre.isdigit():
            CTkM(title="Error", message="El semestre debe ser un número entero.", icon="error")
            return False
        return True

    # Validar la fecha de nacimiento en formato DD/MM/AAAA
    def validar_fecha(self, fnac):
        try:
            datetime.strptime(fnac, "%d/%m/%Y")
            return True
        except ValueError:
            CTkM(title="Error", message="La fecha de nacimiento debe tener el formato DD/MM/AAAA.", icon="error")
            return False    

if __name__ == "__main__":
    app = SistemaGestionUniversitariaApp()
    app.mainloop()
