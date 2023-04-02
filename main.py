import pygame
from time import sleep

# inicializa pygame
pygame.init()

ancho_pantalla = 600
largo_pantalla = 600

pantalla = pygame.display.set_mode([ ancho_pantalla, largo_pantalla ])
pygame.display.set_caption( '3 en raya' )

pygame.display.flip()

while True:
    sleep( 1 )
