import pygame
import transformaciones as t
Ancho=600
Alto=600
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[250,0,0]
BLANCO=[255,255,255]
NEGRO=[0,0,0]


if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    a=[150,100]
    b=[400,100]
    pygame.draw.line(pantalla,VERDE,[300,0],[300,600])
    pygame.draw.line(pantalla,VERDE,[0,300],[600,300])
    pygame.display.flip()
    reloj=pygame.time.Clock()
    cont=0
    fin=False
    ls = []

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.button
                if len(ls) < 3:
                    p = list(event.pos)
                    ls.append(p)
                if len(ls) == 3:
                    print ls
                    if event.button == 5:
                        p0=t.rotar(2,ls[0])
                        p1=t.rotar(2,ls[1])
                        p2=t.rotar(2,ls[2])
                        pantalla.fill([0,0,0])
                        
                        ls = [p0,p1,p2]
                        pygame.draw.line(pantalla,[255,255,0],p0,p1)
                        pygame.draw.line(pantalla,[255,255,0],p1,p2)
                        pygame.draw.line(pantalla,[255,255,0],p2,p0)
                        pygame.display.flip()

                    if event.button == 4:
                        p0=t.rotar2(2,ls[0])
                        p1=t.rotar2(2,ls[1])
                        p2=t.rotar2(2,ls[2])
                        pantalla.fill([0,0,0])

                        ls = [p0,p1,p2]
                        pygame.draw.line(pantalla,[255,255,0],p0,p1)
                        pygame.draw.line(pantalla,[255,255,0],p1,p2)
                        pygame.draw.line(pantalla,[255,255,0],p2,p0)
                        pygame.display.flip()
            #Si es 5 se tiene que aplicar rotacion horaria
            #Si es 4 se tiene que aplicar rotacio antihoraria



        reloj.tick(5)
