import pygame
import transformaciones as t
import math
Ancho=600
Alto=600
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[250,0,0]
BLANCO=[255,255,255]
NEGRO=[0,0,0]

a1 = [50,50]
a2 = [150,150]
a3 = [150,50]


if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    pygame.draw.line(pantalla,VERDE,[300,0],[300,600])
    pygame.draw.line(pantalla,VERDE,[0,300],[600,300])
    pygame.display.flip()
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                pygame.draw.line(pantalla,VERDE,a1,a2)
                pygame.draw.line(pantalla,VERDE,a2,a3)
                pygame.draw.line(pantalla,VERDE,a3,a1)
                if event.key == pygame.K_LEFT:
                    a1 = t.trans([-5,0],a1)
                    a2 = t.trans([-5,0],a2)
                    a3 = t.trans([-5,0],a3)
                    pantalla.fill(NEGRO)
                    pygame.draw.line(pantalla,VERDE,a1,a2)
                    pygame.draw.line(pantalla,VERDE,a2,a3)
                    pygame.draw.line(pantalla,VERDE,a3,a1)
                    pygame.draw.line(pantalla,VERDE,[300,0],[300,600])
                    pygame.draw.line(pantalla,VERDE,[0,300],[600,300])
                if event.key == pygame.K_RIGHT:
                    a1 = t.trans([5,0],a1)
                    a2 = t.trans([5,0],a2)
                    a3 = t.trans([5,0],a3)
                    pantalla.fill(NEGRO)
                    pygame.draw.line(pantalla,VERDE,a1,a2)
                    pygame.draw.line(pantalla,VERDE,a2,a3)
                    pygame.draw.line(pantalla,VERDE,a3,a1)
                    pygame.draw.line(pantalla,VERDE,[300,0],[300,600])
                    pygame.draw.line(pantalla,VERDE,[0,300],[600,300])
                if event.key == pygame.K_DOWN:
                    a1 = t.trans([0,5],a1)
                    a2 = t.trans([0,5],a2)
                    a3 = t.trans([0,5],a3)
                    pantalla.fill(NEGRO)
                    pygame.draw.line(pantalla,VERDE,a1,a2)
                    pygame.draw.line(pantalla,VERDE,a2,a3)
                    pygame.draw.line(pantalla,VERDE,a3,a1)
                    pygame.draw.line(pantalla,VERDE,[300,0],[300,600])
                    pygame.draw.line(pantalla,VERDE,[0,300],[600,300])
                if event.key == pygame.K_UP:
                    a1 = t.trans([0,-5],a1)
                    a2 = t.trans([0,-5],a2)
                    a3 = t.trans([0,-5],a3)
                    pantalla.fill(NEGRO)
                    pygame.draw.line(pantalla,VERDE,a1,a2)
                    pygame.draw.line(pantalla,VERDE,a2,a3)
                    pygame.draw.line(pantalla,VERDE,a3,a1)
                    pygame.draw.line(pantalla,VERDE,[300,0],[300,600])
                    pygame.draw.line(pantalla,VERDE,[0,300],[600,300])
                '''
                if event.key == pygame.K_SPACE:
                    polar = 1
                '''
        pygame.display.flip()
