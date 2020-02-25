import pygame
ANCHO = 900
ALTO = 800
NEGRO = [0,0,0]
AMARILLO = [255,255,0]

def plano(ventana, pos):
    '''
    ventana: Es la ventana que se esta usando
    pos: Es la posicion que se le da para dibujar el plano
    '''
    posx = pos[0]
    posy = pos[1]
    ventana.fill([0,0,0])
    pygame.draw.line(ventana,[255,255,0],[0,posy],[ANCHO,posy])
    pygame.draw.line(ventana,[255,255,0],[posx,0],[posx,ALTO])


def triangulo(ventana,pos):
    ls=[]
    ls.append(pos)
    contador = 0
    while contador < 2:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ls.append(event.pos)
                contador+=1
    pygame.draw.line(ventana,AMARILLO,ls[0],ls[1])
    pygame.draw.line(ventana,AMARILLO,ls[1],ls[2])
    pygame.draw.line(ventana,AMARILLO,ls[2],ls[0])

def trianguloPosicion(ventana,pos,ls):
    #list(pos)
    p1 = pos
    p2 = [pos[0],(pos[1] + 100)]
    p3 = [pos[0]+100,pos[1]+50]

    pygame.draw.line(ventana,AMARILLO,pos,[ pos[0],(pos[1] + 100) ])
    pygame.draw.line(ventana,AMARILLO,[ pos[0],(pos[1] + 100) ],[pos[0]+100,pos[1]+50])
    pygame.draw.line(ventana,AMARILLO,[pos[0]+100,pos[1]+50],pos)
    pygame.display.flip()
    ls = [p1,p2,p3]
    return ls



#con esta funcion se busca que unamos los triangulos para que se vea tridimensional
def unionTriangulo(ventana,pos,ls):
    p1 = pos
    p2 = [pos[0],(pos[1] + 100)]
    p3 = [pos[0]+100,pos[1]+50]

    pygame.draw.line(ventana,AMARILLO,pos,[ pos[0],(pos[1] + 100) ])
    pygame.draw.line(ventana,AMARILLO,[ pos[0],(pos[1] + 100) ],[pos[0]+100,pos[1]+50])
    pygame.draw.line(ventana,AMARILLO,[pos[0]+100,pos[1]+50],pos)

    pygame.draw.line(ventana,AMARILLO,p1,ls[0])
    pygame.draw.line(ventana,AMARILLO,p2,ls[1])
    pygame.draw.line(ventana,AMARILLO,p3,ls[2])
    pygame.display.flip()
    ls = [p1,p2,p3]
    return ls




def caracol(ventana,pos):
    pygame.draw.line(ventana,AMARILLO,pos)
