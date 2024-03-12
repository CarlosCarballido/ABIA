

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
    def __init__(self, estado, padre, operador, profundidad):
        super().__init__(estado, padre)
        self.operador = operador
        self.profundidad = profundidad
