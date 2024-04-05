

#Nodos a almacenar como parte de los algoritmos de búsqueda

class Nodo:
    def __init__(self, estado, padre):
        self.estado=estado
        self.padre=padre




#Nodos usados por la BusquedaAnchura. 
#Añade el Operador usado para generar el estado almacenado en este Nodo. 
#Usado para simplificar la reconstrucción del camino solución.

class NodoAnchura(Nodo):
    def __init__(self, estado, padre, operador):
        super().__init__(estado, padre)
        self.operador=operador

# Nodos usados por la BusquedaProfundidad y BusquedaProfundidadIterativa
# Añade el atributo de profundidad para registrar la profundidad del nodo

class NodoProfundidad(Nodo):
    def __init__(self, estado, padre):
        super().__init__(estado, padre)
class NodoProfundidadIterativa(Nodo):
    def __init__(self, estado, padre, operador, profundidad):
        super().__init__(estado, padre)
        self.operador=operador
        self.profundidad=profundidad
class NodoVoraz:
    def __init__(self, estado, padre, operador, heuristica):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.heuristica = heuristica

class NodoAStar:
    def __init__(self, estado, padre, operador, coste, heuristica):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.coste = coste
        self.heuristica = heuristica
