import sys
import threading
import time
import os

# Importa las clases necesarias
from profundidad import BusquedaProfundidad
from anchura import BusquedaAnchura
from profundidad_iterativa import BusquedaProfundidadIterativa
from voraz import BusquedaVoraz
from a_star import BusquedaAStar
from ida_star import BusquedaIDAStar
from cubo import Cubo
from problemaRubik import Problema, EstadoRubik

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para obtener la opción del usuario con manejo de errores
def obtener_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje)
        if opcion in opciones:
            return opcion
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Función para ejecutar el contador en un hilo separado
def contador(tiempo_limite, solucion_encontrada):
    time.sleep(tiempo_limite)
    if not solucion_encontrada.is_set():
        print("Se ha alcanzado el límite de tiempo de 20 segundos.")
        os._exit(0)

# Inicializa el cubo
cubo = Cubo()

print("CUBO SIN MEZCLAR:\n" + cubo.visualizar())

copia_cubo_original = cubo.clonar()

# Mover frontal face
cubo.mover(cubo.F)

print("CUBO resultado del movimiento F:\n" + cubo.visualizar())

movs = int(sys.argv[1])

movsMezcla = cubo.mezclar(movs)

print("MOVIMIENTOS ALEATORIOS:", movs)
for m in movsMezcla:
    print(cubo.visualizarMovimiento(m) + " ")
print()
cubo_inicial_mezclado = cubo.visualizar()
print("CUBO INICIAL (MEZCLADO):\n" + cubo.visualizar())

opcion = obtener_opcion("Seleccione el número del algoritmo de búsqueda a emplear\n1: Anchura\n2: Profundidad\n3: Profundidad Iterativa\n4: Voraz\n5: A*\n6: IDA*\n", ["1", "2", "3", "4", "5", "6"])
limpiar_pantalla()

if opcion in ["1", "2", "3"]:
    algoritmos = {
        "1": BusquedaAnchura,
        "2": BusquedaProfundidad,
        "3": BusquedaProfundidadIterativa
    }
    busqueda = algoritmos[opcion]()
elif opcion in ["4", "5", "6"]:
    heuristica = obtener_opcion("Seleccione la heurística a emplear\n1: Número de casillas mal colocadas\n2: Número de casillas bien colocadas\n3: Color Clustering\n", ["1", "2", "3"])
    limpiar_pantalla()
    algoritmo = {
        "4": BusquedaVoraz,
        "5": BusquedaAStar,
        "6": BusquedaIDAStar
    }
    busqueda = algoritmo[opcion]()
    if heuristica == "1":
        busqueda.heuristicFunction = busqueda.heuristicFunctionCasillasMalColocadas
    elif heuristica == "2":
        busqueda.heuristicFunction = busqueda.heuristicFunctionPosicionesCorrectas
    elif heuristica == "3":
        busqueda.heuristicFunction = busqueda.heuristicFunctionColorClustering
else:
    print("Opción no válida")
    exit()

# Creación de un problema
problema = Problema(EstadoRubik(cubo), busqueda)

opcion = obtener_opcion("¿Desea establecer un límite de tiempo de ejecución de 20 segundos? (s/n): ", ["s", "n"])
limpiar_pantalla()
if opcion == "s":
    # Señal para indicar si se ha encontrado una solución
    solucion_encontrada = threading.Event()

    # Crea y ejecuta el hilo del contador
    tiempo_limite = 20  # Tiempo límite en segundos
    hilo_contador = threading.Thread(target=contador, args=(tiempo_limite, solucion_encontrada))
    hilo_contador.start()

print("SOLUCION:")
opsSolucion = problema.obtenerSolucion()

# Marca que se ha encontrado una solución
if opcion == "s":
    solucion_encontrada.set()

if opsSolucion is not None:
    print(f"CUBO INICIAL (MEZCLADO):\n{cubo_inicial_mezclado}\nMovimientos para resolver el cubo:{len(opsSolucion)}\nMovimientos:")
    for o in opsSolucion:
        print("\t" + cubo.visualizarMovimiento(o.getEtiqueta()) + " ")
        cubo.mover(o.movimiento)
    print("\nCUBO FINAL:\n" + cubo.visualizar())
    os._exit(0)
else:
    print("No se ha encontrado solución")
    os._exit(0)