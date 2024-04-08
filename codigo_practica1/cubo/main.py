import sys
import time
import matplotlib.pyplot as plt

# Importa las clases necesarias
from anchura import BusquedaAnchura
from profundidad_iterativa import BusquedaProfundidadIterativa
from a_star import BusquedaAStar
from ida_star import BusquedaIDAStar
from cubo import Cubo
from problemaRubik import Problema, EstadoRubik

# Inicializa el cubo
cubo = Cubo()
cubo_inicial = cubo.clonar()

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
cubo_inicial_mezclado = cubo.clonar()
print("CUBO INICIAL (MEZCLADO):\n" + cubo.visualizar())

# Lista de algoritmos de búsqueda
algoritmos = {
    "1": BusquedaAnchura(),
    "2": BusquedaProfundidadIterativa(),
    "4": BusquedaAStar(),
    "5": BusquedaIDAStar()
}

# Lista de heurísticas para la búsqueda A*
heuristicas_a_star = {
    "1": BusquedaAStar().heuristicFunctionCasillasMalColocadas,
    "2": BusquedaAStar().heuristicFunctionPosicionesCorrectas,
    "3": BusquedaAStar().heuristicFunctionColorClustering
}

# Lista de heurísticas para la búsqueda IDA*
heuristicas_ida_star = {
    "1": BusquedaIDAStar().heuristicFunctionCasillasMalColocadas,
    "2": BusquedaIDAStar().heuristicFunctionPosicionesCorrectas,
    "3": BusquedaIDAStar().heuristicFunctionColorClustering
}

# Listas para almacenar los tiempos de búsqueda y los nombres de los algoritmos
tiempos_busqueda = []
nombres_algoritmos = []

# Después de mezclar el cubo
cubo_inicial_mezclado = cubo.clonar()

# Bucle sobre todos los algoritmos de búsqueda
for opcion_busqueda, busqueda in algoritmos.items():
    nombre_algoritmo = busqueda.__class__.__name__
    nombres_algoritmos.append(nombre_algoritmo)
    
    # Lista para almacenar los tiempos de búsqueda para este algoritmo
    tiempos_heuristicas = []
    
    # Check if the algorithm is not greedy search
    if opcion_busqueda != "3":  # Avoiding greedy search (Búsqueda Voraz)
        
        # If the algorithm requires a heuristic
        if opcion_busqueda == "4":  # Búsqueda A*
            # Bucle sobre todas las heurísticas para la búsqueda A*
            for opcion_heuristica, heuristicFunction in heuristicas_a_star.items():
                # Configura la heurística
                busqueda.heuristicFunction = heuristicFunction
                
                # Creación de un problema
                problema = Problema(EstadoRubik(cubo_inicial_mezclado), busqueda)
                
                # Resolución del problema
                tiempo_inicio = time.time()
                opsSolucion = problema.obtenerSolucion()
                tiempo_final = time.time()
                
                # Calcula el tiempo de búsqueda
                tiempo_busqueda = tiempo_final - tiempo_inicio
                tiempos_heuristicas.append(tiempo_busqueda)
        
            # Almacena el tiempo más corto de todas las heurísticas para este algoritmo
            tiempos_busqueda.append(min(tiempos_heuristicas))
        elif opcion_busqueda == "5":  # Búsqueda IDA*
            # Bucle sobre todas las heurísticas para la búsqueda IDA*
            for opcion_heuristica, heuristicFunction in heuristicas_ida_star.items():
                # Configura la heurística
                busqueda.heuristicFunction = heuristicFunction
                
                # Creación de un problema
                problema = Problema(EstadoRubik(cubo_inicial_mezclado), busqueda)
                
                # Resolución del problema
                tiempo_inicio = time.time()
                opsSolucion = problema.obtenerSolucion()
                tiempo_final = time.time()
                
                # Calcula el tiempo de búsqueda
                tiempo_busqueda = tiempo_final - tiempo_inicio
                tiempos_heuristicas.append(tiempo_busqueda)
        
            # Almacena el tiempo más corto de todas las heurísticas para este algoritmo
            tiempos_busqueda.append(min(tiempos_heuristicas))
        else:
            # Creación de un problema para los otros algoritmos
            problema = Problema(EstadoRubik(cubo_inicial_mezclado), busqueda)
            
            # Resolución del problema
            tiempo_inicio = time.time()
            opsSolucion = problema.obtenerSolucion()
            tiempo_final = time.time()
            
            # Calcula el tiempo de búsqueda
            tiempo_busqueda = tiempo_final - tiempo_inicio
            tiempos_busqueda.append(tiempo_busqueda)

# Genera la gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(nombres_algoritmos, tiempos_busqueda, color='skyblue')
plt.xlabel('Algoritmo de Búsqueda')
plt.ylabel('Tiempo de Búsqueda (segundos)')
plt.title('Tiempo de Búsqueda por Algoritmo de Búsqueda')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
