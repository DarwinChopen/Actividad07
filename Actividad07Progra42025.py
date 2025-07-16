print("Actividad 7")
while True:
    print("Actividad 7")
    print("1. Agregar Estudiantes")
    print("2. Mostrar estudiantes y sus cursos")
    print("3. Buscar por Carne")
    print("4. Salir")
    try:
        opcion=int(input("Ingrese una Opcion: "))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            estudiantes = {}
            numeroEstudiantes = int(input("Ingrese la cantidad de estudiantes que desea ingresar"))
            for i in range(numeroEstudiantes):
                print(f"\nEstudiante #{i + 1}")
                carnet = input("Ingrese el número de carnet: ")
                nombre = input("Ingrese el nombre completo: ")
                edad = int(input("Ingrese la edad: "))
                carrera = input("Ingrese la carrera: ")
                numeroCuros = int(input("Ingrese el Numero de Cursos que desea Ingresar"))
                for x in range(numeroCuros):
                    curso = input("Ingrese el Cursos: ")
                    notaTarea = int(input("Ingrese la Nota de la Tarea"))
                    notaParcial = int(input("Ingrese Nota Del Parcial"))
                    notaProyecto = int(input("Ingrese Nota del Proyecto"))

                estudiantes[carnet] = {
                    "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                    "cursos": {
                        "Curso": curso,
                        "notaTarea": notaTarea,
                        "notaParcial": notaParcial,
                        "notaProyecto": notaProyecto
                    }
                }
        case 2:
            print("Listado de Estudiantes")






        case 4:
            print("saliendo...")
            break
        case _:
             print("Opcion invalida")



