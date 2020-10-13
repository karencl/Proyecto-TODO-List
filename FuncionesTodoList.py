# ----------------- Biblioteca extra usada -----------------
import os
"""
    Ésta biblioteca me permite consultar si un archivo existe o no.
    Y la utilizaré para verificar si el usuario que está corriendo el programa,
    ya tiene su archivo o es necesario crear uno nuevo.
"""

# ----------------- Funciones utilizadas en el programa -----------------


def solicita_datos_perfil():
    """Solicita los datos del usuario, para su perfil"""
    matricula = input("Ingresa tu matrícula: ")
    correo = input("Ingres tu correo electrónico: ")
    num_semestre = int(input("Cuéntanos cuál semestre te encuentras cursando: "))
    edad = int(input("¿Cuál es tu edad? "))
    return matricula, correo, num_semestre, edad


def mostrar_perfil(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes):
    """Muestra el perfil del usuario"""
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


def mostrar_materias(lista_materias):
    """Imprime la lista de materias"""
    print("Tus materias:")
    j = 1
    for i in lista_materias:
        print(j, "-", i)
        j += 1
    return lista_materias


def mostrar_pendientes(lista_materias, lista_pendientes, materia_seleccionada):
    """Imprime la lista de pendientes (dentro de la lista general de pendientes), de la materia deseada"""
    print("Pendientes de:", lista_materias[materia_seleccionada - 1])
    k = 1
    for i in lista_pendientes[materia_seleccionada - 1]:
        print(k, "-", i)
        k += 1
    tiempo_pendientes(k)


def tiempo_pendientes(n):
    """Calcula el tiempo estimado para completar los pendientes de una materia"""
    print("** Tiempo estimado para completar pendientes:", (n - 1) * 45, "min **")
    return n


def agregar_pendiente(lista, materia_seleccionada: int):
    """Agrega un pendiente a la lista de pendientes (dentro de la lista general de pendientes), de la materia deseada"""
    nuevo_pendiente = input("Ingresa pendiente: ")
    lista[materia_seleccionada - 1].append(nuevo_pendiente)


def tachar_pendiente(lista, materia_seleccionada: int):
    """Elimina un pendiente de la lista de pendientes (dentro de la lista general de pendientes),
    de la materia deseada"""
    pendiente_a_tachar = int(input("¿Cuál es el pendiente que quieres tachar? "))
    lista[materia_seleccionada - 1].pop(pendiente_a_tachar - 1)


# --------------Nuevas funciones para el archivo del usuario--------------------


def existe_archivo(ruta):
    """Revisa si el archivo con la ruta (nombre) dada, existe"""
    return os.path.isfile(ruta)


def leer_usuario(nombre):
    """Lee el archivo del usuario para obtener sus datos"""
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
    return nombre, matricula, correo, edad, num_semestre, num_materias, \
        lista_materias, num_total_pendientes, lista_pendientes


def escribir_nuevo_usuario(nombre, matricula, correo, edad, num_semestre, num_materias, num_total_pendientes,
                           lista_materias, lista_pendientes):
    """Si no existe ningún archivo para el usuario, crea uno nuevo"""
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

    # Guarda cada lista dentro de la lista pendientes, en el archivo .usuario (como Str). Cada una en una línea distinta
    for i in lista_pendientes:
        archivo_usuario.write(str(i) + "\n")
    archivo_usuario.close()
