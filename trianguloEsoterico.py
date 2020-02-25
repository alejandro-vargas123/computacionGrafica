#programa3
import pygame
from libreria import *
import math




if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    #pygame.draw.line(ventana,[255,255,0],[0,ALTO/2],[ANCHO,ALTO/2])
    #pygame.draw.line(ventana,[255,255,0],[ANCHO/2,0],[ANCHO/2,ALTO])
    pygame.display.flip()
    fin = False
    ls = []
    flag = False
    reloj = pygame.time.Clock()
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print event.pos
                pygame.draw.line(ventana,AMARILLO,[450,100],[250,500])
                pygame.draw.line(ventana,AMARILLO,[450,100],[650,500])
                pygame.draw.line(ventana,AMARILLO,[250,500],[650,500])

                i = 0
                k=290
                while(i<9):
                    pygame.draw.line(ventana,AMARILLO,[450,100],[k,500])
                    k += 40
                    i += 1
                i = 0
                k=470
                j=140
                while(i<9):
                    pygame.draw.line(ventana,AMARILLO,[250,500],[k,j])
                    k += 20
                    j += 40
                    i += 1

                i = 0
                k=430
                j=140
                while(i<9):
                    pygame.draw.line(ventana,AMARILLO,[650,500],[k,j])
                    k -= 20
                    j += 40
                    i += 1
                pygame.display.flip()
        
        reloj.tick(24)
