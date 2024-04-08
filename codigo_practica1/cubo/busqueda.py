from nodos import *

from abc import abstractmethod
from abc import ABCMeta

#Interfaz genérico para algoritmos de búsqueda
class Busqueda(metaclass=ABCMeta):
    @abstractmethod
    def buscarSolucion(self, inicial, heuristica=0):
        pass
    
    def heuristicFunctionPosicionesCorrectas(self, estado):
        cubo_actual = estado.cubo
        correctas_totales = 0
        for cara in cubo_actual.caras:
            for casilla in cara.casillas:
                if casilla.posicionCorrecta == casilla.pos:
                    correctas_totales += 1
        return correctas_totales


    def heuristicFunctionCasillasMalColocadas(self, estado):
        cubo_actual = estado.cubo
        casillas_mal_colocadas = 0
        for cara in cubo_actual.caras:
            for casilla in cara.casillas:
                if casilla.color != cara.color:
                    casillas_mal_colocadas += 1 
        return casillas_mal_colocadas
    
    def heuristicFunctionColorClustering(self, estado):
        cubo_actual = estado.cubo
        movimientos_necesarios = 0
        for cara in cubo_actual.caras:
            color_base = cara.casillas[0].color
            for casilla in cara.casillas:
                if casilla.color != color_base:
                    movimientos_necesarios += 1
        return movimientos_necesarios
