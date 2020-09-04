import FuncionesTodoList as Funciones

LISTA_MATERIAS = []
LISTA_PENDIENTES = []

print("Bienvenid@! \n¿Cómo te llamas?")

# Solicita nombre del usuario
nombre = input()
print("Hola", nombre, "\nEsto es TODO List. \n"
                      "Aquí podrás anotar todos los pendientes que tengas,"
                      "con el fin de llevar una mejor organización"
                      "en tu día a día.")
print()

# Solicita datos del usuario
print("Danos tus datos para poder empezar!")
matricula, correo, num_semestre, edad = Funciones.solicitaDatosPerfil()
num_materias = 0
num_total_pendientes = 0
print()

# imprime perfil del usuario
print("Creando perfil...")
print()
Funciones.mostrarPerfil(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes)
print("Perfil creado con éxito! \nAhora estás list@ para empezar!")
print()

# Menú como un ciclo while
opcion_seleccionada = 1
while opcion_seleccionada != 6:
    print("¿Qué quieres hacer?")
    print("1) Ingresar una nueva materia")
    print("2) Ingresar un nuevo pendiente a una materia")
    print("3) Ver mis pendientes por materia")
    print("4) Ver mi perfil")
    print("5) Editar mi perfil")
    print("6) Salir")
    print()
    opcion_seleccionada = int(input("Ingresa la opción deseada: "))
    print()

    # opción 1 seleccionada (agregar materia)
    if opcion_seleccionada == 1:
        print("¿Cómo se llama la materia que quieres ingresar?")
        nombre_nueva_materia = input("Nombre: ")
        LISTA_MATERIAS.append(nombre_nueva_materia)
        LISTA_PENDIENTES.append([])
        num_materias += 1
        print()

    # opción 2 seleccionada (agregar pendiente)
    elif opcion_seleccionada == 2:
        Funciones.mostrarMaterias(LISTA_MATERIAS)
        materia_seleccionada_op2 = int(input("¿A qué materia quieres ingresar un nuevo pendiente? "))
        print()
        print("Nuevo pendiente para la materia:", LISTA_MATERIAS[materia_seleccionada_op2 - 1])
        Funciones.agregarPendiente(LISTA_PENDIENTES, materia_seleccionada_op2)
        num_total_pendientes += 1
        print()

    # opción 3 seleccionada (ver pendientes por materia)
    elif opcion_seleccionada == 3:
        Funciones.mostrarMaterias(LISTA_MATERIAS)
        materia_seleccionada_op3 = int(input("¿De qué materia quieres ver tus pendientes? "))
        print()
        Funciones.mostrarPendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op3)
        print()
        salir = False
        while salir == False:
            print("¿Qué quieres hacer?")
            print("1) Agregar nuevo pendiente")
            print("2) Tachar un pendiente")
            print("3) Volver al menú principal")
            print()
            opcion = int(input("Ingresa la opción deseada: "))
            print()

            # opción 1 (agregar nuevo pendiente)
            if opcion == 1:
                Funciones.agregarPendiente(LISTA_PENDIENTES, materia_seleccionada_op3)
                num_total_pendientes += 1
                print()
                Funciones.mostrarPendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op3)
                print()

            # opción 2 (tachar pendiente)
            elif opcion == 2:
                Funciones.mostrarPendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op3)
                print()
                Funciones.tacharPendiente(LISTA_PENDIENTES, materia_seleccionada_op3)
                num_total_pendientes -= 1
                print()
                Funciones.mostrarPendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op3)
                print()

            # opción 3 (volver al menú principal)
            elif opcion == 3:
                print("Volviendo al menú principal...")
                print()
                salir = True

            # opción erronea (mensaje de error)
            else:
                print("****************** Selecciona una opción valida. ******************")
                print()

    # opción 4 seleccionada (ver perfil)
    elif opcion_seleccionada == 4:
        Funciones.mostrarPerfil(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes)
        print()

    # opción 5 seleccionada (editar perfil)
    elif opcion_seleccionada == 5:
        matricula, correo, num_semestre, edad = Funciones.solicitaDatosPerfil()
        print()

    # opción 6 seleccionada (salir)
    elif opcion_seleccionada == 6:
        print("Has decidido salir.")
        print()

    # opción erronea (mensaje de error)
    else:
        print("****************** Selecciona una opción valida. ******************")
        print()

print("Hasta pronto!")
