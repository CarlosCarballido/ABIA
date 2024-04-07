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
                #print(casilla)
                if casilla.posicionCorrecta == casilla.pos:
                    correctas_totales += 1
        return correctas_totales


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
    
    def heuristicFunctionColorClustering(self, estado):
        # Obtiene el cubo del estado actual
        cubo_actual = estado.cubo
        # Inicializa el contador de movimientos necesarios para agrupar colores
        movimientos_necesarios = 0
        # Itera sobre cada cara del cubo
        for cara in cubo_actual.caras:
            # Obtiene el color de la primera casilla de la cara
            color_base = cara.casillas[0].color
            # Itera sobre cada casilla de la cara
            for casilla in cara.casillas:
                # Compara el color de la casilla con el color base
                if casilla.color != color_base:
                    # Incrementa el contador de movimientos necesarios si el color no coincide
                    movimientos_necesarios += 1
        # Devuelve el número total de movimientos necesarios para agrupar colores
        return movimientos_necesarios
