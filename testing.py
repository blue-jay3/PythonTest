import matplotlib.pyplot as plt
import numpy as np
import pygame 
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((700,400))
DISPLAYSURF.fill((255,255,255))

FPS = pygame.time.Clock()
FPS.tick(60)

color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))

run = True
on = False

while run:
    
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_SPACE]:
        if on == False:
            pygame.draw.rect(DISPLAYSURF, (255,0,0), object1)
            on = True
        if on == True:
            on = False
        
    pygame.display.update()

pygame.quit()