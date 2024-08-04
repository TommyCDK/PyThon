import pygame

from pygame.locals import *
import sys
import ctypes
import time
import Draw as D
import ImportTile as IP
import Sences

pygame.init()

#Screen Settings
screenx = 1000
screeny = 720
 
screen = pygame.display.set_mode((screenx,screeny))

run = True


#Import Images And Create Rect
hcn = Rect((0,450),(50,50))

hcn1 = Rect((200,200),(50,50))

Dirt = pygame.image.load("Tiles\Dirt.png")

Dirt = pygame.transform.smoothscale(Dirt,(50,50))

Grass = pygame.image.load("Tiles\Grass.png")

Grass = pygame.transform.smoothscale(Grass,(50,50))

Sand = pygame.image.load("Tiles\Sand.png")

Sand = pygame.transform.smoothscale(Sand,(50,50))

Water = pygame.image.load("Tiles\Water.png")

Water = pygame.transform.smoothscale(Water,(50,50))


fc = False

def fcc(): #FullScreen Toggle

    if fc == True:

        ctypes.windll.user32.SetProcessDPIAware()

        true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

        pygame.display.set_mode(true_res,pygame.FULLSCREEN)

    else:

        screen = pygame.display.set_mode((1000,720))

s1 = True
s2 = False

     
                    
def RunModule():

    if s1 == True:
        Sences.sc1()
    if s2 == True:
        Sences.sc2()
          


    



screen.fill("white")
while run:
    mx,my = pygame.mouse.get_pos()
    mr = Rect((mx,my),(10,10))
    screen.fill("white")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if s2 == True:
                    s2 = False
                    print("d")
                else: 
                    s2 = True
                print("s")
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                if fc == True:
                    fc = False
                else:
                    fc = True
    RunModule()




    


    pygame.display.flip()

quit()