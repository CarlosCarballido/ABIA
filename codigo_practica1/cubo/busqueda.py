from nodos import *

from abc import abstractmethod
from abc import ABCMeta

#Interfaz genérico para algoritmos de búsqueda
class Busqueda(metaclass=ABCMeta):
    @abstractmethod
    def buscarSolucion(self, inicial, heuristica=0):
        pass
    
    def heuristicFunctionManhattan(self, estado):
        cubo_actual = estado.cubo
        distancia_manhattan = 0
        for cara in cubo_actual.caras:
            for casilla in cara.casillas:
                #TODO: Implementar la función heurística de distancia de Manhattan
                raise NotImplementedError

    def heuristicFunctionCasillasMalColocadas(self, estado):
        # Implementa tu función heurística aquí
        # Por ejemplo, una heurística común para el cubo de Rubik podría ser el número de casillas mal colocadas
        cubo_actual = estado.cubo
        casillas_mal_colocadas = 0
        for cara in cubo_actual.caras:
            for casilla in cara.casillas:
                if casilla.color != cara.color:
                    casillas_mal_colocadas += 1 
        return casillas_mal_colocadas