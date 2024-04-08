import time
from busqueda import *
from nodos import NodoProfundidadIterativa

class BusquedaProfundidadIterativa(BusquedaNoInformada):
    
    def buscarSolucion(self, inicial):
        profundidad_maxima = 0
        solucion = None

        while solucion is None:
            solucion = self.buscarConProfundidad(inicial, profundidad_maxima)
            profundidad_maxima += 1
        print("Profundidad máxima alcanzada: ", profundidad_maxima - 1)
        return solucion

    def buscarConProfundidad(self, inicial, profundidad_maxima):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = dict()
        abiertos.append(NodoProfundidadIterativa(inicial, None, None, 0))  # Inicializa la profundidad en 0
        cerrados[inicial.cubo.visualizar()] = inicial
        while not solucion and len(abiertos) > 0:
            
            if self.nodosAbiertosMax < len(abiertos):
                self.nodosAbiertosMax = len(abiertos)
            
            nodoActual = abiertos.pop()
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            elif nodoActual.profundidad < profundidad_maxima:
                cerrados[actual.cubo.visualizar()] = actual
                for operador in actual.operadoresAplicables():
                    hijo = actual.aplicarOperador(operador)
                    if hijo.cubo.visualizar() not in cerrados.keys():
                        abiertos.append(NodoProfundidadIterativa(hijo, nodoActual, operador, nodoActual.profundidad + 1))
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