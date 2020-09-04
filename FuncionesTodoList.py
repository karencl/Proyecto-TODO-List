def solicitaDatosPerfil():
    matricula = input("Ingresa tu matrícula: ")
    correo = input("Ingres tu correo electrónico: ")
    num_semestre = int(input("Cuéntanos cuál semestre te encuentras cursando: "))
    edad = int(input("¿Cuál es tu edad? "))
    return matricula, correo, num_semestre, edad


def mostrarPerfil(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes):
    print("PERFIL de", nombre)
    print("··················································")
    print("Nombre:", nombre)
    print("Matrícula:", matricula)
    print("Correo:", correo)
    print("Edad: ", edad)
    print("Año de nacimiento: ", 2020 - edad)  # 1 operador
    print("* Se encuentra cursando el semestre:", num_semestre)
    print("* Semestres por cursar:", 8 - num_semestre)  # 2 operador
    print("Número de materias agregadas:", num_materias)
    print("Número total de pendientes:", num_total_pendientes)
    print("··················································")
    print()


def mostrarMaterias(lista_materias):
    print("Tus materias:")
    j = 1
    for i in lista_materias:
        print(j, "-", i)
        j += 1
    return lista_materias


def mostrarPendientes(lista_materias, lista_pendientes, materia_seleccionada):
    print("Pendientes de:", lista_materias[materia_seleccionada - 1])
    k = 1
    for i in lista_pendientes[materia_seleccionada - 1]:
        print(k, "-", i)
        k += 1
    tiempoPendientes(k)


def tiempoPendientes(n):
    print("** Tiempo estimado para completar pendientes:", (n - 1) * 45, "min **")
    return n


def agregarPendiente(lista, materia_seleccionada: int):
    nuevo_pendiente = input("Ingresa pendiente: ")
    lista[materia_seleccionada - 1].append(nuevo_pendiente)


def tacharPendiente(lista, materia_seleccionada: int):
    tachar_pendiente = int(input("¿Cuál es el pendiente que quieres tachar? "))
    lista[materia_seleccionada - 1].pop(tachar_pendiente - 1)

