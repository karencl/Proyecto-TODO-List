"""Biblioteca extra usada"""
import os   # Ésta biblioteca me permite consultar si un archivo existe o no.
            # Y la utilizaré para verificar si el usuario que está corriendo el programa,
            # ya tiene su archivo o es necesario crear uno nuevo.


"""Funciones utilizadas en el programa"""

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
    print("Año de nacimiento: ", 2020 - edad)
    print("* Se encuentra cursando el semestre:", num_semestre)
    print("* Semestres por cursar:", 8 - num_semestre)
    print("Número de materias agregadas:", num_materias)
    print("Número total de pendientes:", num_total_pendientes)
    print("··················································")
    print()


# Imprime la lista de materias
def mostrarMaterias(lista_materias):
    print("Tus materias:")
    j = 1
    for i in lista_materias:
        print(j, "-", i)
        j += 1
    return lista_materias


# Imprime la lista de pendientes (dentro de la lista general de pendientes), de la materia deseada
def mostrarPendientes(lista_materias, lista_pendientes, materia_seleccionada):
    print("Pendientes de:", lista_materias[materia_seleccionada - 1])
    k = 1
    for i in lista_pendientes[materia_seleccionada - 1]:
        print(k, "-", i)
        k += 1
    tiempoPendientes(k)


# Calcula el tiempo estimado para completar los pendientes de una materia
def tiempoPendientes(n):
    print("** Tiempo estimado para completar pendientes:", (n - 1) * 45, "min **")
    return n


# Agrega un pendiente a la lista de pendientes (dentro de la lista general de pendientes), de la materia deseada
def agregarPendiente(lista, materia_seleccionada: int):
    nuevo_pendiente = input("Ingresa pendiente: ")
    lista[materia_seleccionada - 1].append(nuevo_pendiente)


# Elimina un pendiente de la lista de pendientes (dentro de la lista general de pendientes), de la materia deseada
def tacharPendiente(lista, materia_seleccionada: int):
    tachar_pendiente = int(input("¿Cuál es el pendiente que quieres tachar? "))
    lista[materia_seleccionada - 1].pop(tachar_pendiente - 1)


"""--------------Nuevas funciones para el archivo del usuario--------------------"""

def existeArchivo(ruta):
    return os.path.isfile(ruta)


def leerUsuario(nombre):
    lista_pendientes = []
    archivo_usuario = open(nombre + ".usuario", "r")
    nombre = archivo_usuario.readline().rstrip()
    matricula = archivo_usuario.readline().rstrip()
    correo = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    num_semestre = int(archivo_usuario.readline())
    num_materias = int(archivo_usuario.readline())
    num_total_pendientes = int(archivo_usuario.readline())

    # Lee las listas (materias y pendientes) del archivo .usuario (como Str), y luego las convierte en listas nuevamente
    listas = archivo_usuario.readlines()
    materias = listas[0].replace("[", "").replace("]", "").replace(",", "").replace("'", "")
    lista_materias = materias.split()
    for i in range(1, len(lista_materias) + 1):
        pendientes = listas[i].replace("[", "").replace("]", "").replace(",", "").replace("'", "")
        pen_temp = pendientes.split()
        lista_pendientes.append(pen_temp)
    archivo_usuario.close()
    return nombre, matricula, correo, edad, num_semestre, num_materias, lista_materias, num_total_pendientes, lista_pendientes


def escribirNuevoUsuario(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes, lista_materias, lista_pendientes):
    archivo_usuario = open(nombre + ".usuario", "w")
    archivo_usuario.write(nombre + "\n")
    archivo_usuario.write(matricula + "\n")
    archivo_usuario.write(correo + "\n")
    archivo_usuario.write(str(edad) + "\n")
    archivo_usuario.write(str(num_semestre) + "\n")
    archivo_usuario.write(str(num_materias) + "\n")

    # Guarda la lista de materias en el archivo .usuario (como Str)
    archivo_usuario.write(str(lista_materias) + "\n")
    archivo_usuario.write(str(num_total_pendientes) + "\n")

    # Guarda cada lista dentro de la lista pendientes, en el archivo .usuario (como Str)
    for i in lista_pendientes:
        archivo_usuario.write(str(i) + "\n")
    archivo_usuario.close()

