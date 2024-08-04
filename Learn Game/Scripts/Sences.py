
import pygame

from pygame.locals import *
import sys
import ctypes
import time
import Draw as D
import ImportTile as IP
screenx = 1000
screeny = 720
 
screen = pygame.display.set_mode((screenx,screeny))

Button1 = D.slot((0,0,0),(255,0,0),50,50,3,100,570)
ay = D.slot((0,0,0),(200,200,200),100,50,3,500,360)
b = D.CreateButton(Button1,screen)

s1 = True
s2 = False
def bta():
    print("opoppopoopopopoppo")   






def sc1(): #Screen 1
    


    
    
             
    b.Click(bta)
    b.draw()
    ay.draw(screen)
    

    


def sc2(): #Screen 2

    pygame.draw.rect(screen,(0,0,0),hcn1)
    screen.blit(Dirt, (100,100))