import os
import sys
import pygame

# --- Configuración básica ---
ANCHO, ALTO = 640, 640
FILAS, COLUMNAS = 8, 8
TAM_CASILLA = ANCHO // COLUMNAS

BLANCO = (245, 245, 220)
NEGRO = (118, 150, 86)

# --- Rutas ---
CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_IMAGENES = os.path.join(CARPETA_BASE, "image")

# --- Archivos de las piezas ---
PIEZAS_ARCHIVOS = {
    'pb': 'Chess_pdt60.png',  # Peón negro
    'pw': 'Chess_plt60.png',  # Peón blanco
    'tb': 'Chess_rdt60.png',  # Torre negra
    'tw': 'Chess_rlt60.png',  # Torre blanca
    'cb': 'Chess_ndt60.png',  # Caballo negro
    'cw': 'Chess_nlt60.png',  # Caballo blanco
    'ab': 'Chess_bdt60.png',  # Alfil negro
    'aw': 'Chess_blt60.png',  # Alfil blanco
    'qb': 'Chess_qdt60.png',  # Reina negra
    'qw': 'Chess_qlt60.png',  # Reina blanca
    'kb': 'Chess_kdt60.png',  # Rey negro
    'kw': 'Chess_klt60.png'   # Rey blanco
}

# --- Función para cargar imágenes ---
def cargar_imagenes():
    if not os.path.isdir(CARPETA_IMAGENES):
        print(f"[ERROR] No existe la carpeta: {CARPETA_IMAGENES}")
        sys.exit(1)

    imagenes = {}
    for clave, nombre_archivo in PIEZAS_ARCHIVOS.items():
        ruta = os.path.join(CARPETA_IMAGENES, nombre_archivo)
        if not os.path.isfile(ruta):
            print(f"[ERROR] Falta el archivo: {ruta}")
            sys.exit(1)
        img = pygame.image.load(ruta)
        imagenes[clave] = pygame.transform.scale(img, (TAM_CASILLA, TAM_CASILLA))
    return imagenes
