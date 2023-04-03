import pygame
from time import sleep

# inicializa pygame
pygame.init()

ANCHO_PANTALLA = 600
LARGO_PANTALLA = 600

COLOR_FONDO = ( 220, 132, 73 )
COLOR_LINEAS_DIVISON = ( 69, 69, 69 )

# 0 = vacio, 1 = jugador 1, 2 = jugador 2
matriz_juego = [ 
    [ 0, 0, 0 ],
    [ 0, 0, 0 ],
    [ 0, 0, 0 ]
]

pantalla = pygame.display.set_mode([ ANCHO_PANTALLA, LARGO_PANTALLA ])
pygame.display.set_caption( '3 en raya' )

pantalla.fill( COLOR_FONDO )
def dibujar_tablero ():
    pygame.draw.line( pantalla, COLOR_LINEAS_DIVISON, ( ( ANCHO_PANTALLA // 3 ), 0 ), ( ( ANCHO_PANTALLA // 3 ), LARGO_PANTALLA ), 5 )
    pygame.draw.line( pantalla, COLOR_LINEAS_DIVISON, ( ( ANCHO_PANTALLA // 3 ) * 2, 0 ), ( ( ANCHO_PANTALLA // 3 ) * 2, LARGO_PANTALLA ), 5 )
    pygame.draw.line( pantalla, COLOR_LINEAS_DIVISON, ( 0, ( LARGO_PANTALLA // 3 ) ), ( ANCHO_PANTALLA, ( LARGO_PANTALLA // 3 ) ), 5 )
    pygame.draw.line( pantalla, COLOR_LINEAS_DIVISON, ( 0, ( LARGO_PANTALLA // 3 ) * 2 ), ( ANCHO_PANTALLA, ( LARGO_PANTALLA // 3 ) * 2 ), 5 )
    

def obtener_coordenadas ( fila, columna ):
    coordenadas = ( ( ANCHO_PANTALLA // 3 ) * columna + ( ANCHO_PANTALLA // 6 ), ( LARGO_PANTALLA // 3 ) * fila + ( LARGO_PANTALLA // 6 ) )
    return coordenadas

def dibujar_ficha ( fila, columna, jugador ):
    centro = obtener_coordenadas( fila, columna )
    if jugador == 1:
        COLOR_FICHA = ( 84, 3, 117 )
        pygame.draw.line( pantalla, COLOR_FICHA, ( centro[ 0 ] - ( ANCHO_PANTALLA // 9 ), centro[ 1 ] - ( LARGO_PANTALLA // 9 ) ), ( centro[ 0 ] + ( ANCHO_PANTALLA // 9 ), centro[ 1 ] + ( LARGO_PANTALLA // 9 ) ), 10 )
        pygame.draw.line( pantalla, COLOR_FICHA, ( centro[ 0 ] + ( ANCHO_PANTALLA // 9 ), centro[ 1 ] - ( LARGO_PANTALLA // 9 ) ), ( centro[ 0 ] - ( ANCHO_PANTALLA // 9 ), centro[ 1 ] + ( LARGO_PANTALLA // 9 ) ), 10 )
    if jugador == 2:
        COLOR_FICHA = ( 0, 255, 221 )
        pygame.draw.circle( pantalla, COLOR_FICHA, centro, ( ANCHO_PANTALLA // 9 ), 10 )

def actualizar_matriz_juego ( fila, columna, jugador ):
    matriz_juego[ fila ][ columna ] = jugador

def revisar_ganador ():
    for fila in matriz_juego:
        if fila[ 0 ] != 0 and fila[ 0 ] == fila[ 1 ] == fila[ 2 ]:
            return fila[ 0 ]
    for columna in range( 3 ):
        if matriz_juego[ 0 ][ columna ] != 0 and matriz_juego[ 0 ][ columna ] == matriz_juego[ 1 ][ columna ] == matriz_juego[ 2 ][ columna ]:
            return matriz_juego[ 0 ][ columna ]
    if matriz_juego[ 0 ][ 0 ] != 0 and matriz_juego[ 0 ][ 0 ] == matriz_juego[ 1 ][ 1 ] == matriz_juego[ 2 ][ 2 ]:
        return matriz_juego[ 0 ][ 0 ]
    if matriz_juego[ 0 ][ 2 ] != 0 and matriz_juego[ 0 ][ 2 ] == matriz_juego[ 1 ][ 1 ] == matriz_juego[ 2 ][ 0 ]:
        return matriz_juego[ 0 ][ 2 ]
    return 0

pygame.display.flip()

turno_jugador = 1

while True:
    sleep( 0.1 )
    pygame.display.flip()
    dibujar_tablero()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[ 0 ] < ANCHO_PANTALLA // 3:
                columna = 0
            elif pos[ 0 ] < ( ANCHO_PANTALLA // 3 ) * 2:
                columna = 1
            else:
                columna = 2
            if pos[ 1 ] < LARGO_PANTALLA // 3:
                fila = 0
            elif pos[ 1 ] < ( LARGO_PANTALLA // 3 ) * 2:
                fila = 1
            else:
                fila = 2

            if matriz_juego[ fila ][ columna ] == 0:
                dibujar_ficha( fila, columna, turno_jugador )
                actualizar_matriz_juego( fila, columna, turno_jugador )
                pygame.display.flip()
                if turno_jugador == 1:
                    turno_jugador = 2
                else:
                    turno_jugador = 1
                if revisar_ganador() != 0:
                    print( f"El ganador es: { revisar_ganador() }" )
                    pygame.quit()
                    quit()
