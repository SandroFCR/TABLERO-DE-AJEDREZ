class Pieza:
    def __init__(self, color):
        self.color = color

    def movimiento_valido(self, inicio, fin, tablero):
        raise NotImplementedError
        

class Torre(Pieza):
    def movimiento_valido(self, inicio, fin, tablero):
        x1, y1 = inicio
        x2, y2 = fin

        # 1. La torre solo se mueve en línea recta
        if x1 != x2 and y1 != y2:
            return False

        # 2. Revisar si hay piezas en el camino
        if x1 == x2:  # Movimiento vertical
            paso = 1 if y2 > y1 else -1
            for y in range(y1 + paso, y2, paso):
                if tablero[x1][y] is not None:
                    return False
        else:  # Movimiento horizontal
            paso = 1 if x2 > x1 else -1
            for x in range(x1 + paso, x2, paso):
                if tablero[x][y1] is not None:
                    return False

        # 3. Si pasa todas las comprobaciones → movimiento válido
        return True
