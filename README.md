# Proyecto para la materia: Pensamiento computacional para ingeniería.
Este trabajo es parte del proyecto para la materia "Pensamiento computacional para ingeniería".

En este, se trabajarán conceptos básicos de programación y se pondrán en práctica los procesos de estos, con el fin de entender la lógica de los programas de computadora y aprender el funcionamiento de los mismos.


# Proyecto-TODO-List

Mi proyecto se llama: "TODO List".

Este proyecto tiene como finalidad ayudar al usuario a llevar un mejor control de su tiempo durante el día, con la oportunidad de anotar tareas, agregar listas como materias o cualquier otra forma para clasificar los pendientes deseados y modificarlos agregarndo o marcarcando como completado un pendiente. 
Y finalmente, por supuesto se va a tener la oportunidad de llevar la cuenta (automática) de todos los pendientes por hacer.

En este trabajo, pondré en práctica el uso de variables con diferentes tipos de datos (string, int, bool), el uso de contadores crecientes y decrecientes para llevar un control de cuántos pendientes quedan por hacer, el uso de listas para clasificar pendientes, el uso de funciones y ciclos para facilitar tanto la escritura, como la lectura y funcionamiento del programa y finalmente, el uso de documentos tipo .txt para brindarle una mejor experiencia a todo usuario que pruebe el programa.


# Funcionalidad del programa

-Iniciar o agregarse como usuario

-Explorar menú de opciones

-Agregar listas para clasificar pendientes (ejemplo: materias)

-Agregar pendientes a listas

-Tachar pendientes de listas

-Ver listas y pendientes (Y también cuántos listas tienes creadas y cuantos pendientes tienes en TOTAL)

-Ver perfil del usuario

-Salir


# Ejemplo de algoritmo del programa

DESPUÉS DE HABER INGRESADO LOS DATOS DEL USUARIO...

-Definir la opción temporatl para entrar el ciclo (ejemplo: op = 1)
1. *Ciclo para el menú* (while) --> (while op != 0:)
2. Opciones a elegir
- pedir al usuario la opción deseada (input)
3. Casos para cada opción (agregar lista/ agregar pendiente/ tachar pendiente/ ver perfil) - condicionales (if/elif/else) --> (ejemplo: elif op == 1:)
  3.1 Código para cada opción
  - en caso de requerir algún dato, pedíselo al usuario (inputs) --> (ejemplo: nuevo_pendiente = int(input("Ingresa el nuevo pendiente:")) )
4. Salir del ciclo (solo cuando "op" sea 0)

CONTINUAR CON LO DEMÁS DEL CÓDIGO
