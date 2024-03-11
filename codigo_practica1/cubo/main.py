import sys

#Añadir al path el directorio donde se encuentran los módulos
sys.path.append('..')

from profundidad import BusquedaProfundidad
from anchura import BusquedaAnchura
from profundidad_iterativa import BusquedaProfundidadIterativa

from cubo import *
from cubo import Cubo
from problemaRubik import *

cubo = Cubo()

print("CUBO SIN MEZCLAR:\n" + cubo.visualizar())

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

#Creación de un problema
problema = Problema(EstadoRubik(cubo), BusquedaAnchura())

print("SOLUCION:")
opsSolucion = problema.obtenerSolucion()

if opsSolucion != None:
    for o in opsSolucion:
        print(cubo.visualizarMovimiento(o.getEtiqueta()) + " ")
        cubo.mover(o.movimiento)
    print("\nCUBO FINAL:\n" + cubo.visualizar())
else:
    print("no se ha encontrado solución")