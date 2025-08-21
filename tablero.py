import pygame
from recursos import FILAS, COLUMNAS, TAM_CASILLA, BLANCO, NEGRO

def dibujar_tablero(ventana):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            color = BLANCO if (fila + columna) % 2 == 0 else NEGRO
            x = columna * TAM_CASILLA
            y = fila * TAM_CASILLA
            pygame.draw.rect(ventana, color, (x, y, TAM_CASILLA, TAM_CASILLA))

def dibujar_piezas(ventana, tablero, imagenes):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pieza = tablero[fila][columna]
            if pieza:
                x = columna * TAM_CASILLA
                y = fila * TAM_CASILLA
                ventana.blit(imagenes[pieza], (x, y))

