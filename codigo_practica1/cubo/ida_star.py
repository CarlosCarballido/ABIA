import time
from busqueda import Busqueda
from profundidad import BusquedaProfundidad
from nodos import NodoIDAStar

class BusquedaIDAStar(Busqueda):  
    
    def __init__(self) -> None:
        super().__init__()
        self.nodosAbiertosTotal = 1
        self.nodosAbiertosMax = 0
    
    def expandir_nodo(self, actual, nodoActual, abiertos, cerrados):
        for operador in actual.operadoresAplicables():
            hijo = actual.aplicarOperador(operador)
            if hijo.cubo.visualizar() not in cerrados.keys():
                coste = nodoActual.coste + operador.getCoste()
                abiertos.append(NodoIDAStar(hijo, nodoActual, operador, coste))
                cerrados[hijo.cubo.visualizar()] = hijo  
    
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
            if self.nodosAbiertosMax < len(abiertos):
                self.nodosAbiertosMax = len(abiertos)
            abiertos.remove(nodoActual)
            self.nodosAbiertosTotal += 1
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            else:
                cerrados[actual.cubo.visualizar()] = actual
                if nodoActual.coste < limite:
                    self.expandir_nodo(actual, nodoActual, abiertos, cerrados)
                else:
                    nodoActual = None
                    abiertos = []
                    cerrados = {}
                    limite += 1
                
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
        