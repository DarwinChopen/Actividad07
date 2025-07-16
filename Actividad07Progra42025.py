print("Actividad 7")
estudiantes={}
numeroEstudiantes=int(input("Ingrese la cantidad de estudiantes que desea ingresar"))
for i in range(numeroEstudiantes):
    print(f"\nEstudiante #{i + 1}")
    carnet = input("Ingrese el número de carnet: ")
    nombre = input("Ingrese el nombre completo: ")
    edad = int(input("Ingrese la edad: "))
    carrera = input("Ingrese la carrera: ")
    curso = input("Ingrese el Cursos: ")
    notaParcial=int(input("Ingrese Nota Del Parcial"))
    notaProyecto=int(input("Ingrese Nota del Proyecto"))


    estudiantes[carnet] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "cursos": {
            "Curso": curso,
            "notaParcial": notaParcial,
            "notaProyecto":notaProyecto
        }
    }