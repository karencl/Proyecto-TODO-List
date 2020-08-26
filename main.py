# import funcionesTodoList as Funciones

LISTA_MATERIAS = []
LISTA_PENDIENTES = []

print("Bienvenid@! \n¿Cómo te llamas?")

# Solicita nombre del usuario
nombre = input()
print("Hola", nombre, "\nEsto es TODO List. \n"
                      "Aquí podrás anotar todos los pendientes que tengas,"
                      "con el fin de llevar una mejor organización"
                      "en tu día a día.")

# Solicita datos del usuario
print("Danos tus datos para poder empezar!")
matricula = input("Ingresa tu matrícula: ")
correo = input("Ingres tu correo electrónico: ")
num_semestre = int(input("Cuéntanos cuál semestre te encuentras cursando: "))
num_materias = 0
num_total_pendientes = 0

# imprime perfil del usuario
print("Creando perfil...")
print()
print("PERFIL de", nombre)
print("·················································")
print("Nombre:", nombre)
print("Matrícula:", matricula)
print("Correo:", correo)
print("* Se encuentra cursando el semestre:", num_semestre)
print("* Semestres por cursar:", 8 - num_semestre)
print("Número de materias agregadas:", num_materias)
print("Número total de pendientes:", num_total_pendientes)
print("·················································")
print()
print("Perfil creado con éxito! \nAhora estás list@ para empezar!")
print()

# Menú como un ciclo while
opcion_seleccionada = 1
while opcion_seleccionada != 0:
    print("¿Qué quieres hacer?")
    print("1) Ingresar una nueva materia")
    print("2) Ingresar un nuevo pendiente a una materia")
    print("3) Ver mis pendientes por materia")
    print("4) Ver mi perfil")
    print("0) Salir")
    print()
    opcion_seleccionada = int(input("Ingresa la opción deseada: "))
    print()

    # opción 1 seleccionada
    if opcion_seleccionada == 1:
        print("¿Cómo se llama la materia que quieres ingresar?")
        nombre_nueva_materia = input("Nombre: ")
        LISTA_MATERIAS.append(nombre_nueva_materia)
        LISTA_PENDIENTES.append([])
        num_materias += 1
        print()

    # opción 2 seleccionada
    elif opcion_seleccionada == 2:
        print("Tus materias:")
        j = 1
        for i in LISTA_MATERIAS:
            print(j, "-", i)
            j += 1
        materia_seleccionada_op2 = int(input("¿A qué materia quieres ingresar un nuevo pendiente? "))
        print()
        print("Nuevo pendiente para la materia:", LISTA_MATERIAS[materia_seleccionada_op2 - 1])
        nuevo_pendiente = input("Ingresa pendiente: ")
        LISTA_PENDIENTES[materia_seleccionada_op2 - 1].append(nuevo_pendiente)
        num_total_pendientes += 1
        print()

    # opción 3 seleccionada
    elif opcion_seleccionada == 3:
        print("Tus materias:")
        j = 1
        for i in LISTA_MATERIAS:
            print(j, "-", i)
            j += 1
        materia_seleccionada_op3 = int(input("¿De qué materia quieres ver tus pendientes? "))
        print()
        print("Pendientes de: ", LISTA_MATERIAS[materia_seleccionada_op3 - 1])
        k = 1
        for i in LISTA_PENDIENTES[materia_seleccionada_op3 - 1]:
            print(k, "-", i)
            k += 1
        print("Tiempo estimado para completar pendientes:", (k - 1) * 45, "min")
        print()

    # opción 4 seleccionada
    elif opcion_seleccionada == 4:
        print("PERFIL de", nombre)
        print("·················································")
        print("Nombre:", nombre)
        print("Matrícula:", matricula)
        print("Correo:", correo)
        print("* Se encuentra cursando el semestre:", num_semestre)
        print("Número de materias agregadas:", num_materias)
        print("Número total de pendientes:", num_total_pendientes)
        print("·················································")
        print()

    elif opcion_seleccionada == 0:
        print("Has decidido salir.")
        print()

    else:
        print("Selecciona una opción valida.")
        print()

print("Hasta pronto!")
