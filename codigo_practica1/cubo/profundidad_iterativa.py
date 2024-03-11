from cubo.busqueda import Busqueda


class BusquedaProfundidadIterativa(Busqueda):
    
    def __init__(self, edges) -> None:
        super().__init__()
        self.edges = edges
        self.adjuntos = {}
        for adjunto, edje in edges:
            if adjunto not in self.adjuntos:
                self.graph[adjunto] = []
            self.graph[adjunto].append(edje)
        
    def buscarSolucion(self,inicial):
        pila = [inicial]
        
        explorado = []

        while pila:
            ultimo = pila.pop()
            if ultimo not in explorado:
                print(ultimo, end=" ")
                explorado.add(ultimo)
                if ultimo in self.adjuntos:
                    pila.extend(vecino for vecino in self.adjuntos[ultimo] if vecino not in explorado)