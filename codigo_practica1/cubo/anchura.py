from busqueda import *
from nodos import NodoAnchura


class BusquedaAnchura(Busqueda):
    
    def __init__(self) -> None:
        super().__init__()
        self.nodosAbiertosTotal = 1
        self.nodosAbiertosMax = 0
    
    #Implementa la búsqueda en anchura. Si encuentra solución recupera la lista de Operadores empleados almacenada en los atributos de los objetos NodoAnchura
    def buscarSolucion(self,inicial):
        nodoActual = None
        actual, hijo = None, None
        solucion = False
        abiertos = []
        cerrados = dict()
        abiertos.append(NodoAnchura(inicial, None, None))
        cerrados[inicial.cubo.visualizar()]=inicial
        while not solucion and len(abiertos)>0:
            
            if self.nodosAbiertosMax < len(abiertos):
                self.nodosAbiertosMax = len(abiertos)

            nodoActual = abiertos.pop(0)
            actual = nodoActual.estado
            if actual.esFinal():
                solucion = True
            else:

                cerrados[actual.cubo.visualizar()] = actual
                for operador in actual.operadoresAplicables():
                    hijo = actual.aplicarOperador(operador)
                    if hijo.cubo.visualizar() not in cerrados.keys():
                        abiertos.append(NodoAnchura(hijo, nodoActual, operador))
                        self.nodosAbiertosTotal += 1
                        cerrados[hijo.cubo.visualizar()] = hijo 
        if solucion:
            lista = []
            nodo = nodoActual
            while nodo.padre != None: #Asciende hasta la raíz
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