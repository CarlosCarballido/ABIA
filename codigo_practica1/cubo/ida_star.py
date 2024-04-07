from busqueda import Busqueda
from profundidad import BusquedaProfundidad
from nodos import NodoIDAStar

class BusquedaIDAStar(Busqueda):
    def __init__(self):
        pass
    
    def buscarSolucion(self, inicial):
        nodoActual = NodoIDAStar(inicial, None, None, 0, self.heuristicFunction(inicial))
        limite = self.heuristicFunction(inicial)
        busqueda_profundidad = BusquedaProfundidad()  # Creamos una instancia de BusquedaProfundidad
        
        while True:
            costo_limite_excedido, nuevo_limite = busqueda_profundidad.buscarSolucion(nodoActual, 0, limite)  # Llamamos al método buscarSolucion de BusquedaProfundidad
            if not costo_limite_excedido:
                return self.construirCamino(nodoActual)
            limite = nuevo_limite
        
        #return None  # No se llega a este punto, por lo que devolvemos None
    
    def construirCamino(self, nodo):
        camino = []
        while nodo.padre:
            camino.insert(0, nodo.operador)
            nodo = nodo.padre
        return camino
