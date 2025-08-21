import pygame
from recursos import ANCHO, ALTO, cargar_imagenes
from tablero import dibujar_tablero, dibujar_piezas
from logica import posiciones_iniciales

pygame.init()
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ajedrez por DataSANDRO")

def main():
    imagenes = cargar_imagenes()
    tablero = posiciones_iniciales()
    en_ejecucion = True

    while en_ejecucion:
        dibujar_tablero(VENTANA)
        dibujar_piezas(VENTANA, tablero, imagenes)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_ejecucion = False

    pygame.quit()

if __name__ == "__main__":
    main()
