from busqueda import Busqueda
from profundidad import BusquedaProfundidad
from nodos import NodoIDAStar

class BusquedaIDAStar(Busqueda):    
    def buscarSolucion(self, inicial):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = {}
        limite = self.heuristicFunction(inicial)
        abiertos.append(NodoIDAStar(inicial, None, None, 0))
        cerrados[inicial.cubo.visualizar()] = inicial
        while not solucion and abiertos:
            nodoActual = min(abiertos, key=lambda x: x.coste)
            abiertos.remove(nodoActual)
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            else:
                cerrados[actual.cubo.visualizar()] = actual
                if nodoActual.coste < limite:
                    for operador in actual.operadoresAplicables():
                        hijo = actual.aplicarOperador(operador)
                        if hijo.cubo.visualizar() not in cerrados.keys():
                            coste = nodoActual.coste + operador.getCoste()
                            abiertos.append(NodoIDAStar(hijo, nodoActual, operador, coste))
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