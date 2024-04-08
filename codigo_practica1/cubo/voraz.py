import time
from busqueda import *
from nodos import NodoVoraz

class BusquedaVoraz(Busqueda):
    
    def __init__(self) -> None:
        super().__init__()
        self.nodosAbiertosTotal = 1
        self.nodosAbiertosMax = 0
    
    def buscarSolucion(self, inicial):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = dict()
        abiertos.append(NodoVoraz(inicial, None, None, self.heuristicFunction(inicial)))
        cerrados[inicial.cubo.visualizar()] = inicial
        while not solucion and len(abiertos) > 0:
            if self.nodosAbiertosMax < len(abiertos):
                self.nodosAbiertosMax = len(abiertos)
            
            # Selecciona el nodo actual basándose en la heurística mas baja
            nodoActual = min(abiertos, key=lambda x: x.heuristica)
            abiertos.remove(nodoActual)
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            else:
                cerrados[actual.cubo.visualizar()] = actual
                for operador in actual.operadoresAplicables():
                    hijo = actual.aplicarOperador(operador)
                    if hijo.cubo.visualizar() not in cerrados.keys():
                        abiertos.append(NodoVoraz(hijo, nodoActual, operador, self.heuristicFunction(hijo)))
                        self.nodosAbiertosTotal += 1
                        cerrados[hijo.cubo.visualizar()] = hijo
        if solucion:
            lista = []
            nodo = nodoActual
            while nodo.padre is not None:
                lista.insert(0, nodo.operador)
                nodo = nodo.padre
                
            print("Total Nodos abiertos: ", self.nodosAbiertosTotal)
            print("Máximo de nodos abiertos sinmultaneamente: ", self.nodosAbiertosMax)
            print("Total nodos cerrados: ", len(cerrados))
            print("Total nodos explorados: ", self.nodosAbiertosTotal + len(cerrados))
            print("Profundidad de la solución: ", len(lista))
            return lista
        else:
            return None