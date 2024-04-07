from busqueda import *
from nodos import NodoVoraz

class BusquedaVoraz(Busqueda):
    
    # Implementa la búsqueda voraz.
    # Si encuentra solución, recupera la lista de Operadores empleados almacenada en los atributos de los objetos NodoVoraz.
    def buscarSolucion(self, inicial):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = dict()
        # Inicializa la lista de abiertos con el nodo inicial
        abiertos.append(NodoVoraz(inicial, None, None, self.heuristicFunction(inicial)))
        cerrados[inicial.cubo.visualizar()] = inicial
        while not solucion and len(abiertos) > 0:
            # Selecciona el nodo actual basándose en una heurística
            # (en el caso de búsqueda voraz, se selecciona el nodo con la heurística más baja)
            nodoActual = min(abiertos, key=lambda x: x.heuristica)
            abiertos.remove(nodoActual)  # Elimina el nodo actual de la lista de abiertos
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            else:
                cerrados[actual.cubo.visualizar()] = actual
                for operador in actual.operadoresAplicables():
                    hijo = actual.aplicarOperador(operador)
                    # Verifica si el hijo no está en los cerrados
                    if hijo.cubo.visualizar() not in cerrados.keys():
                        # Calcula la heurística para el hijo y crea un nuevo nodo voraz
                        # Agrega el nodo hijo a la lista de abiertos
                        abiertos.append(NodoVoraz(hijo, nodoActual, operador, self.heuristicFunction(hijo)))
                        cerrados[hijo.cubo.visualizar()] = hijo
        if solucion:
            lista = []
            nodo = nodoActual
            while nodo.padre is not None:  # Asciende hasta la raíz
                lista.insert(0, nodo.operador)
                nodo = nodo.padre
            return lista
        else:
            return None


    # Función para calcular la heurística del estado dado (puede variar según el problema)
    def calcularHeuristica(self, estado):
    # Obtiene el cubo del estado actual
        cubo_actual = estado.cubo
        # Inicializa el contador de casillas mal colocadas
        casillas_mal_colocadas = 0
        # Itera sobre cada cara del cubo
        for cara in cubo_actual.caras:
            # Itera sobre cada casilla de la cara
            for casilla in cara.casillas:
                # Comprueba si la casilla está en la posición correcta
                if casilla.color != cara.color:
                    # Incrementa el contador si la casilla está mal colocada
                    casillas_mal_colocadas += 1
        # Devuelve el número de casillas mal colocadas como heurística
        return casillas_mal_colocadas
