import FuncionesTodoList as Funciones

# Listas utilizadas:
LISTA_MATERIAS = []    # Lista "simple"
LISTA_PENDIENTES = []  # Lista "simple", que posteriormente se le agregan más listas, convirtiéndola en lista anidada

print("Bienvenid@! \n¿Cómo te llamas?: ")

# Solicita nombre del usuario
nombre = input()
print("Hola", nombre,   "\nEsto es TODO List. \n"
                        "Aquí podrás anotar todos los pendientes que tengas,"
                        "con el fin de llevar una mejor organización"
                        "en tu día a día.")
print()

# Revisa si el archivo con el nombre existe
if Funciones.existe_archivo(nombre + ".usuario"):
    print("Leyendo datos del usuario...")
    print()
    (nombre, matricula, correo, edad, num_semestre, num_materias, LISTA_MATERIAS,
     num_total_pendientes, LISTA_PENDIENTES) = Funciones.leer_usuario(nombre)
else:
    # Si no, se solicitan los datos del usuario
    print("Danos tus datos para poder empezar!")
    matricula, correo, num_semestre, edad = Funciones.solicita_datos_perfil()
    num_materias = 0
    num_total_pendientes = 0
    print()

# Imprime perfil del usuario
print("Creando perfil...")
print()
Funciones.mostrar_perfil(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes)
print("Perfil creado con éxito! \nAhora estás list@ para empezar!")
print()

# Menú como un ciclo while
opcion_seleccionada = 1
while opcion_seleccionada != 7:
    print("¿Qué quieres hacer?")
    print("1) Ingresar una nueva materia")
    print("2) Borrar una materia")
    print("3) Ingresar un nuevo pendiente a una materia")
    print("4) Ver mis pendientes por materia")
    print("5) Ver mi perfil")
    print("6) Editar mi perfil")
    print("7) Salir")
    print()
    opcion_seleccionada = int(input("Ingresa la opción deseada: "))
    print()

    # opción 1 seleccionada (agregar materia)
    if opcion_seleccionada == 1:
        print("¿Cómo se llama la materia que quieres ingresar?")
        nombre_nueva_materia = input("Nombre: ")
        LISTA_MATERIAS.append(nombre_nueva_materia)  # Se añade la materia a la lista de materias
        LISTA_PENDIENTES.append([])  # Se crea una nueva lista en la lista de pendientes, para la materia creada
        num_materias += 1
        print()

    # opción 2 seleccionada (borrar materia)
    elif opcion_seleccionada == 2:
        Funciones.mostrar_materias(LISTA_MATERIAS)
        print()
        materia_seleccionada_op2 = int(input("¿Qué materia quieres borrar? "))
        print("Se eliminará la materia:", LISTA_MATERIAS[materia_seleccionada_op2 - 1])
        LISTA_MATERIAS.remove(LISTA_MATERIAS[materia_seleccionada_op2 - 1])  # Se elimina la materia de LISTA_MATERIAS
        num_materias -= 1
        num_total_pendientes -= len(LISTA_PENDIENTES[materia_seleccionada_op2 - 1])
        LISTA_PENDIENTES.remove(LISTA_PENDIENTES[materia_seleccionada_op2 - 1])  # Se elimina la lista de pendientes de
        print("Listo!")                                                          # dicha materia, dentro de la lista
        print()                                                                  # pendientes

    # opción 3 seleccionada (agregar pendiente)
    elif opcion_seleccionada == 3:
        Funciones.mostrar_materias(LISTA_MATERIAS)
        materia_seleccionada_op3 = int(input("¿A qué materia quieres ingresar un nuevo pendiente? "))
        print()
        print("Nuevo pendiente para la materia:", LISTA_MATERIAS[materia_seleccionada_op3 - 1])
        Funciones.agregar_pendiente(LISTA_PENDIENTES, materia_seleccionada_op3)
        num_total_pendientes += 1
        print()

    # opción 4 seleccionada (ver pendientes por materia)
    elif opcion_seleccionada == 4:
        Funciones.mostrar_materias(LISTA_MATERIAS)
        materia_seleccionada_op4 = int(input("¿De qué materia quieres ver tus pendientes? "))
        print()
        Funciones.mostrar_pendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op4)
        print()
        opcion4 = True
        while opcion4:
            print("¿Qué quieres hacer?")
            print("1) Agregar nuevo pendiente")
            print("2) Tachar un pendiente")
            print("3) Volver al menú principal")
            print()
            opcion = int(input("Ingresa la opción deseada: "))
            print()

            # opción 1 de opción 4 (agregar nuevo pendiente)
            if opcion == 1:
                Funciones.agregar_pendiente(LISTA_PENDIENTES, materia_seleccionada_op4)
                num_total_pendientes += 1
                print()
                Funciones.mostrar_pendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op4)
                print()

            # opción 2 de opción 4 (tachar pendiente)
            elif opcion == 2:
                Funciones.mostrar_pendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op4)
                print()
                Funciones.tachar_pendiente(LISTA_PENDIENTES, materia_seleccionada_op4)
                num_total_pendientes -= 1
                print()
                Funciones.mostrar_pendientes(LISTA_MATERIAS, LISTA_PENDIENTES, materia_seleccionada_op4)
                print()

            # opción 3 de opción 4 (volver al menú principal)
            elif opcion == 3:
                print("Volviendo al menú principal...")
                print()
                opcion4 = False

            # opción erronea de opción 4 (mensaje de error)
            else:
                print("****************** Selecciona una opción valida. ******************")
                print()

    # opción 5 seleccionada (ver perfil)
    elif opcion_seleccionada == 5:
        Funciones.mostrar_perfil(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes)
        print()

    # opción 6 seleccionada (editar perfil)
    elif opcion_seleccionada == 6:
        matricula, correo, num_semestre, edad = Funciones.solicita_datos_perfil()
        print()

    # opción 7 seleccionada (salir)
    elif opcion_seleccionada == 7:
        print("Has decidido salir.")
        print("Guardando datos del usuario...")
        Funciones.escribir_nuevo_usuario(nombre, matricula, correo, edad, num_semestre, num_materias, LISTA_MATERIAS,
                                         num_total_pendientes, LISTA_PENDIENTES)
        print()

    # opción erronea (mensaje de error)
    else:
        print("****************** Selecciona una opción valida. ******************")
        print()

print("Hasta pronto!")
