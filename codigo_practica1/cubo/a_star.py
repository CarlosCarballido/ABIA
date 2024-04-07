from nodos import NodoAStar
from busqueda import Busqueda

class BusquedaAStar(Busqueda):
    def __init__(self):
        pass

    def buscarSolucion(self, inicial):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = {}
        
        print(f"Funcion heuristica: {type(self.heuristicFunction)}")
        
        """if self.heuristicFunction == self.heuristicFunctionCasillasMalColocadas:
            heuristicFunction = self.heuristicFunctionCasillasMalColocadas
        elif heuristicFunction == 2:
            heuristicFunction = self.heuristicFunctionManhattan
        elif heuristicFunction == 3:
            pass
        else:
            return None"""
        # Agrega el nodo inicial a la lista de abiertos con un costo heurístico inicial de 0
        abiertos.append(NodoAStar(inicial, None, None, 0, self.heuristicFunction(inicial)))
        cerrados[inicial.cubo.visualizar()] = inicial
        while not solucion and abiertos:
            # Selecciona el nodo actual basándose en la suma del costo heurístico y el costo acumulado hasta el momento
            nodoActual = min(abiertos, key=lambda x: x.coste + x.heuristica)
            abiertos.remove(nodoActual)  # Elimina el nodo actual de la lista de abiertos
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            else:
                cerrados[actual.cubo.visualizar()] = actual
                for operador in actual.operadoresAplicables():
                    hijo = actual.aplicarOperador(operador)
                    if hijo.cubo.visualizar() not in cerrados.keys():
                        # Calcula el costo heurístico del hijo y crea un nuevo nodo A* con el costo acumulado y la heurística
                        coste = nodoActual.coste + operador.getCoste()
                        abiertos.append(NodoAStar(hijo, nodoActual, operador, coste, self.heuristicFunction(hijo)))
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
