
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
                        "curso": curso,
                        "notaTarea": notaTarea,
                        "notaParcial": notaParcial,
                        "notaProyecto": notaProyecto
                    }
                }
        case 2:
            print("Listado de Estudiantes")
            for carnet, datos in estudiantes.items():
                print(f"\nCarnet: {carnet}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Edad: {datos['edad']}")
                print(f"Carrera: {datos['carrera']}")
                for curso, datos in estudiantes.items():
                    print(f":Curso {datos['cursos']['curso']}")
                    print(f"Nota Tarea: {datos['cursos']['notaTarea']}")
                    print(f"Nota Parcial: {datos['cursos']['notaParcial']}")
                    print(f"Nota Proyecto: {datos['cursos']['notaProyecto']}")

        case 3:
            print("Busqueda de Estudiantes por carne")
            buscando=input("Inngrese el Carne a Buscar: ")
            if buscando in estudiantes:
                estudiante=estudiantes[buscando]
                print("Estudiante Encontrado")
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Edad: {estudiante['edad']}")
                print(f"Carrera: {estudiante['carrera']}")
                print(f"Curso: {estudiante['cursos']['curso']}")
                print(f"Nota Tarea: {estudiante['cursos']['notaTarea']}")
                print(f"Nota Parcial: {estudiante['cursos']['notaParcial']}")
                print(f"Nota Proyecto: {estudiante['cursos']['notaProyecto']}")

            else:
                print("El estudiante no se encontro")


        case 4:
            print("saliendo...")
            break
        case _:
             print("Opcion invalida")



