import sys

#Añadir al path el directorio donde se encuentran los módulos
sys.path.append('..')

from profundidad import BusquedaProfundidad
from anchura import BusquedaAnchura
from profundidad_iterativa import BusquedaProfundidadIterativa
from voraz import BusquedaVoraz
from a_star import BusquedaAStar

from cubo import *
from cubo import Cubo
from problemaRubik import *

cubo = Cubo()

print("CUBO SIN MEZCLAR:\n" + cubo.visualizar())

copia_cubo_original = cubo.clonar()

#Mover frontal face
cubo.mover(cubo.F)

print("CUBO resultado del movimiento F:\n" + cubo.visualizar())

movs=int(sys.argv[1])

movsMezcla = cubo.mezclar(movs)

print("MOVIMIENTOS ALEATORIOS:",movs)
for m in movsMezcla:
    print(cubo.visualizarMovimiento(m) + " ")
print()

print("CUBO INICIAL (MEZCLADO):\n" + cubo.visualizar())

opcion = input("Seleccione el numero del algoritmo de búsqueda a emplear \n 1: Anchura\n 2: Profundidad\n 3: Profundidad Iterativa\n 4: Voraz\n 5: A*\n")
if opcion == "1":
    print("Busqueda en Anchura")
    busqueda = BusquedaAnchura()
elif opcion == "2":
    print("Busqueda en Profundidad")
    busqueda = BusquedaProfundidad()
elif opcion == "3":
    print("Busqueda en Profundidad Iterativa")
    busqueda = BusquedaProfundidadIterativa()
elif opcion == "4":
    print("Busqueda Voraz")
    busqueda = BusquedaVoraz()
elif opcion == "5":
    print("Busqueda A*")
    busqueda = BusquedaAStar()
    opcion = input("Seleccione la heurística a emplear \n 1: Número de casillas mal colocadas\n 2: Distancia de Manhattan\n")
    if opcion == "1":
        busqueda.heuristicFunction = busqueda.heuristicFunctionCasillasMalColocadas
    elif opcion == "2":
        busqueda.heuristicFunction = busqueda.heuristicFunctionManhattan
    else:
        print("Opción no válida")
        exit()
else:
    print("Opción no válida")
    exit()

#Creación de un problema
problema = Problema(EstadoRubik(cubo), busqueda)

print("SOLUCION:")
opsSolucion = problema.obtenerSolucion()

if opsSolucion != None:
    for o in opsSolucion:
        print(cubo.visualizarMovimiento(o.getEtiqueta()) + " ")
        cubo.mover(o.movimiento)
    print("\nCUBO FINAL:\n" + cubo.visualizar())
else:
    print("no se ha encontrado solución")