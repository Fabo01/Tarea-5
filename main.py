from Asignatura import Asignatura
from Profesor import Profesor
from Estudiante import Estudiante
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico

if __name__ == "__main__":
    asignatura1 = Asignatura("Matemáticas", "MAT101", 4)
    profesor1 = Profesor("Juan", "Pérez", "01-01-1980", "1234", "Matemáticas")
    estudiante1 = Estudiante("Carlos", "García", "15-05-2000", "20201001", "Ingeniería", 3)
    
    grupo1 = Grupo(1, asignatura1, profesor1)
    grupo1.agregar_estudiante(estudiante1)
    
    grupo1.mostrar_informacion()