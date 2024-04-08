class Nodo:
    def __init__(self, estado, padre):
        self.estado=estado
        self.padre=padre

class NodoAnchura(Nodo):
    def __init__(self, estado, padre, operador):
        super().__init__(estado, padre)
        self.operador=operador

class NodoProfundidad(Nodo):
    def __init__(self, estado, padre, operador):
        super().__init__(estado, padre)
        self.operador=operador
class NodoProfundidadIterativa(Nodo):
    def __init__(self, estado, padre, operador, profundidad):
        super().__init__(estado, padre)
        self.operador=operador
        self.profundidad=profundidad
class NodoVoraz:
    def __init__(self, estado, padre, operador, heuristica):
        super().__init__(estado, padre)
        self.operador = operador
        self.heuristica = heuristica

class NodoAStar:
    def __init__(self, estado, padre, operador, coste, heuristica):
        super().__init__(estado, padre)
        self.operador = operador
        self.coste = coste
        self.heuristica = heuristica

class NodoIDAStar:
    def __init__(self, estado, padre, operador, coste):
        super().__init__(estado, padre)
        self.operador = operador
        self.coste = coste