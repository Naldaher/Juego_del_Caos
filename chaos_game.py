# JUEGO DEL CAOS: el juego del caos es un proceso donde se realizan un
# numero x de iteraciones para generar un fractal, DEPENDIENDO DE LA
# CONFIGURACION INICIAL. Específicamente esta configurado para generar
# un fractal basado en un polígono regular de n lados

import pygame
import random
import math
import colorsys 

# colorsys se utiliza para convertir colores del espacio
# HSV (tono, saturación, valor) a RGB (red, blue, green), permitiendo
# asignar un color distinto a cada vértice del polígono

from pygame.locals import *

idx = [0, 0, 0] # almaceno los tres ultimos vertices seleccionados

def mark_pixel(surface, pos, pcol): # mark_pixel determina el color del pixel actual en el juego del caos
    # pos = tupla (x,y) de la posición
    col = surface.get_at(pos)
    surface.set_at(pos, (min(col[0] + pcol[0]/10, 255),
                         min(col[1] + pcol[1]/10, 255),
                         min(col[2] + pcol[2]/10, 255)))
    # definimos un nuevo color mezclando gradualmente el anterior (por eso dividimos entre 10)
    # y nos aseguramos que no exceda los 255 (max de RGB) -> por eso usamos la funcion min
    # establezco el nuevo color en la posicion actual con .set_at

def random_point_index(p):
    if len(p) <= 3:
        return random.randint(0, len(p) - 1) # si hay menos de 3 vértices, el siguiente será uno random y ya

    global idx
    idx[2] = idx[1] # actualizo los vértices
    idx[1] = idx[0]
    dst1 = abs(idx[1] - idx[2]) # distancia

    while True:
        idx[0] = random.randint(0, len(p) - 1)
        dst = abs(idx[0] - idx[1])
        if dst1 == 0 and (dst == 1 or dst == len(p) - 1):
            continue
        else:
            break

    return idx[0]

# si los dos vértices anteriores fueron iguales (dst1 == 0)
# el nuevo vértice no debe ser un vecino directo del vértice (por eso 'continue')
# los vértices directos se identifican cuando la distancia es 1 o N-1

def init_polygon(width, height, n):
    delta_angle = 360/n
    r = width/2 - 10
    p = []

    for i in range(0, n):
        angle = (180 + i*delta_angle) * math.pi / 180 # calculo el ángulo del polinomio
        color = colorsys.hsv_to_rgb((i*delta_angle)/360, 0.8, 1)
        p.append(((width/2 + r*math.sin(angle),
                   height/2 + r*math.cos(angle)),
                  (int(color[0]*255), int(color[1]*255), int(color[2]*255)))) # esta tupla tiene 5 elementos: 2 de la posicion calculada con trigonometria, y 3 para el RGB

    return p

def main(width, height, n, r):
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Juego del Caos')

    p = init_polygon(width, height, n)

    x, y = (400, 300)
    step = 0
    while True:
        step = step + 1
        point_idx = random_point_index(p)

        pos = p[point_idx][0]
        color = p[point_idx][1]
        # Formula para el calculo de la nuevo x (o y): nuevo_x = x + (pos[0] - x)*r
        x += (pos[0] - x) * r
        y += (pos[1] - y) * r

        mark_pixel(surface, (int(x), int(y)), color)

        if step % 1000 == 0:
            pygame.display.update() # actualiza la pantalla, q sino peta

        for event in pygame.event.get():
            if event.type == QUIT: # para poder cerrar el programa sin crash, porque el programa es un bucle infinito
                pygame.image.save(surface, 'chaosspiel.jpg')
                pygame.quit()
                return

if __name__ == "__main__":
    n=5; main(800, 800, n,  0.45)