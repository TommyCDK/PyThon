


import pygame
import sys
from pygame import *


class slot(): #Draw Square With OutLine

        def __init__(self, LineColor, BackgroundColor, ScaleX, ScaleY, LineWidth, PosX, PosY):

            self.LineColor =  LineColor
            self.LineWidth = LineWidth
            self.BackgroundColor = BackgroundColor
            self.ScaleX = ScaleX
            self.ScaleY = ScaleY
            self.PosX = PosX
            self.PosY  = PosY           
            LineWidth = int(LineWidth)
            RectName = Rect((PosX,PosY),(ScaleX,ScaleY))
        def draw(self, Surface):
            self.Surface = Surface
            pygame.draw.rect(Surface,self.BackgroundColor,Rect((self.PosX,self.PosY),(self.ScaleX,self.ScaleY)))
            pygame.draw.line(Surface,self.LineColor,(self.PosX,self.PosY),(self.PosX+self.ScaleX,self.PosY),self.LineWidth)
            pygame.draw.line(Surface,self.LineColor,(self.PosX,self.PosY),(self.PosX,self.PosY+self.ScaleY),self.LineWidth)
            pygame.draw.line(Surface,self.LineColor,(self.PosX+self.ScaleX,self.PosY),(self.PosX+self.ScaleX,self.PosY+self.ScaleY),self.LineWidth)
            pygame.draw.line(Surface,self.LineColor,(self.PosX,self.PosY+self.ScaleY),(self.PosX+self.ScaleX,self.PosY+self.ScaleY),self.LineWidth)

class CreateButton():
        
    def __init__(self, Rect, Surface): #Import Rect
        self.Rect = Rect 
        self.rectx = self.Rect.PosX
        self.recty = self.Rect.PosY
        self.rectscaleX = self.Rect.ScaleX
        self.rectscaleY = self.Rect.ScaleY
        LineWidth = self.Rect.LineWidth
        LineColor = self.Rect.LineColor 
        self.CheckClick = False 
        self.IsHover = False
        self.Surface = Surface
    def Click(self, Execute):  #Check Click
        self.Execute = Execute 
        self.but = Rect((self.rectx,self.recty),(self.rectscaleX,self.rectscaleY))
        if self.but.collidepoint(pygame.mouse.get_pos()) :
            if pygame.mouse.get_pressed()[0] and not self.CheckClick:
                self.CheckClick = True
                print(self.CheckClick)
                Execute()
            if not pygame.mouse.get_pressed()[0]:
                self.CheckClick = False





    def draw(self):
        self.Rect.draw(self.Surface)


def fcc(): #FullScreen Toggle

    if fc == True:

        ctypes.windll.user32.SetProcessDPIAware()

        true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

        pygame.display.set_mode(true_res,pygame.FULLSCREEN)

    else:

        screen = pygame.display.set_mode((1000,720))
