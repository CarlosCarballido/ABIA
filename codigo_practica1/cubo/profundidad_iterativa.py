from busqueda import *
from nodos import NodoProfundidadIterativa

class BusquedaProfundidadIterativa(Busqueda):
    
    # Implementa la búsqueda en profundidad iterativa.
    # Si encuentra solución, recupera la lista de Operadores empleados almacenada en los atributos de los objetos NodoProfundidadIterativa.
    def buscarSolucion(self, inicial):
        profundidad_maxima = 0
        solucion = None
        # Itera hasta que se encuentra una solución o se alcanza la profundidad máxima
        while solucion is None:
            solucion = self.buscarConProfundidad(inicial, profundidad_maxima)
            profundidad_maxima += 1
        return solucion

    # Realiza una búsqueda en profundidad con una profundidad máxima específica
    def buscarConProfundidad(self, inicial, profundidad_maxima):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = dict()
        abiertos.append(NodoProfundidadIterativa(inicial, None, None, 0))  # Inicializa la profundidad en 0
        cerrados[inicial.cubo.visualizar()] = inicial
        while not solucion and len(abiertos) > 0:
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