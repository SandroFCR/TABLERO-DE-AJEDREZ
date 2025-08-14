import pygame
import os
import sys

ANCHO, ALTO = 640, 640
FILAS, COLUMNAS = 8, 8
TAM_CASILLA = ANCHO // COLUMNAS  

BLANCO = (245, 245, 220)
NEGRO  = (118, 150, 86)

pygame.init()
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ajedrez por DataSANDRO")

CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_IMAGENES = os.path.join(CARPETA_BASE, "image")  
PIEZAS_ARCHIVOS = {
    'pb': 'Chess_pdt60.png',   # Peón negro
    'pw': 'Chess_plt60.png',   # Peón blanco
    'tb': 'Chess_rdt60.png',   # Torre negra
    'tw': 'Chess_rlt60.png',   # Torre blanca
    'cb': 'Chess_ndt60.png',   # Caballo negro
    'cw': 'Chess_nlt60.png',   # Caballo blanco
    'ab': 'Chess_bdt60.png',   # Alfil negro
    'aw': 'Chess_blt60.png',   # Alfil blanco
    'qb': 'Chess_qdt60.png',   # Reina negra
    'qw': 'Chess_qlt60.png',   # Reina blanca
    'kb': 'Chess_kdt60.png',   # Rey negro
    'kw': 'Chess_klt60.png'    # Rey blanco
}

def depurar_carpeta_imagenes():
    print("[DEBUG] Carpeta Base:", CARPETA_BASE)
    print("[DEBUG] Carpeta Imagenes:", CARPETA_IMAGENES)
    if not os.path.isdir(CARPETA_IMAGENES):
        print("[ERROR] no existe la carpeta 'images'")
        return False
    archivos = os.listdir(CARPETA_IMAGENES)
    print("[DEBUG] archivos encontrados:", archivos)
    return True

def cargar_imagenes():
    if not depurar_carpeta_imagenes():
        pygame.quit(); sys.exit(1)
    imagenes = {}
    for clave, nombre_archivo in PIEZAS_ARCHIVOS.items():
        ruta = os.path.join(CARPETA_IMAGENES, nombre_archivo)
        if not os.path.isfile(ruta):
            print(f"[ERROR] falta el archivo: {ruta}")
            pygame.quit(); sys.exit(1)
        img = pygame.image.load(ruta)
        imagenes[clave] = pygame.transform.scale(img, (TAM_CASILLA, TAM_CASILLA))
    return imagenes

def dibujar_tablero(ventana):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            color = BLANCO if (fila + columna) % 2 == 0 else NEGRO
            x = columna * TAM_CASILLA
            y = fila * TAM_CASILLA
            pygame.draw.rect(ventana, color, (x, aaay, TAM_CASILLA, TAM_CASILLA))

def posiciones_iniciales():
    return [
        ['tb','cb','ab','qb','kb','ab','cb','tb'],
        ['pb']*8,
        ['']*8,
        ['']*8,
        ['']*8,
        ['']*8,
        ['pw']*8,
        ['tw','cw','aw','qw','kw','aw','cw','tw']
    ]

def dibujar_piezas(ventana, tablero, imagenes):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pieza = tablero[fila][columna]
            if pieza:
                x = columna * TAM_CASILLA
                y = fila * TAM_CASILLA
                ventana.blit(imagenes[pieza], (x, y))

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
