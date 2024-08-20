

import pygame
import os
#Import Images And Create Rect

class ImportImages():
    def __init__(self, ID, Path, ScaleX, ScaleY):
        self.ID = str(ID)
        self.Path = Path
        self.ScaleX = ScaleX
        self.ScaleY = ScaleY
        
    def Install(self):
        self.Name = self.ID
        self.ID = pygame.image.load(self.Path)
        self.ID = pygame.transform.smoothscale(self.ID,(self.ScaleX, self.ScaleY))
    
    def Draw(self, Surface, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.Surface = Surface
        Surface.blit(self.ID, (self.PosX, self.PosY))

dirt = ImportImages("dirt","Tiles\Dirt.png",50,50)
dirt.Install()

grass = ImportImages("grass","Tiles\Grass.png",50,50)
grass.Install()

sand = ImportImages("sand","Tiles\Sand.png",50,50)
sand.Install()

water = ImportImages("water","Tiles\Water.png",50,50)
water.Install()

ExitIMG = ImportImages("ExitIMG", "Tiles\Exit.png",150,50)
ExitIMG.Install()

StartIMG = ImportImages("StartIMG", "Tiles\Start.png",150,50)
StartIMG.Install()

MenuIMG = ImportImages("MenuIMG", "Tiles\Menu.png",150,50)
MenuIMG.Install()