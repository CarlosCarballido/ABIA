from busqueda import *
from nodos import NodoAStar

class BusquedaAStar(Busqueda):
    
    # Implementa el algoritmo A*.
    # Si encuentra solución, recupera la lista de Operadores empleados almacenada en los atributos de los objetos NodoAStar.
    def buscarSolucion(self, inicial, estado_objetivo):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = dict()
        abiertos.append(NodoAStar(inicial, None, None, 0, self.calcularHeuristica(inicial, estado_objetivo)))
        cerrados[inicial.cubo.visualizar()] = inicial
        while not solucion and len(abiertos) > 0:
            nodoActual = min(abiertos, key=lambda x: x.coste + x.heuristica)
            abiertos.remove(nodoActual)
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            else:
                cerrados[actual.cubo.visualizar()] = actual
                for operador in actual.operadoresAplicables():
                    hijo = actual.aplicarOperador(operador)
                    if hijo.cubo.visualizar() not in cerrados.keys():
                        abiertos.append(NodoAStar(hijo, nodoActual, operador, nodoActual.coste + 1, self.calcularHeuristica(hijo, estado_objetivo)))
                        cerrados[hijo.cubo.visualizar()] = hijo
        if solucion:
            lista = []
            nodo = nodoActual
            while nodo.padre is not None:  
                lista.insert(0, nodo.operador)
                nodo = nodo.padre
            return lista
        else:
            return None

    # Función para calcular la heurística del estado dado (puede variar según el problema)
    def calcularHeuristica(self, estado, estado_objetivo):
        # Obtiene el cubo del estado actual y el cubo del estado objetivo
        cubo_actual = estado.cubo
        cubo_objetivo = estado_objetivo.cubo
        # Inicializa el contador de casillas mal colocadas
        casillas_mal_colocadas = 0
        # Itera sobre cada cara del cubo actual y del cubo objetivo
        for cara_actual, cara_objetivo in zip(cubo_actual.caras, cubo_objetivo.caras):
            # Itera sobre cada casilla de la cara actual y de la cara objetivo
            for casilla_actual, casilla_objetivo in zip(cara_actual.casillas, cara_objetivo.casillas):
                # Comprueba si la casilla está en la posición correcta
                if casilla_actual.color != casilla_objetivo.color:
                    # Incrementa el contador si la casilla está mal colocada
                    casillas_mal_colocadas += 1
        # Devuelve el número de casillas mal colocadas como heurística
        return casillas_mal_colocadas
