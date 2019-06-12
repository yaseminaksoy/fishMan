import pygame
import sys
import math
import random

class Bullet():
    def __init__(self,FishMan):
        self.x=0
        self.y=0
        self.mx=0
        self.my=0

        self.rectangle=pygame.rect.Rect(FishMan.rectangle[0] + int(FishMan.rectangle[2]/25*8), FishMan.rectangle[1] +  int(FishMan.rectangle[3]/25*8), int(FishMan.rectangle[2] / 5), int(FishMan.rectangle[3] / 5))
        self.imageOrder=0
        self.images=[pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (1).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (2).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (3).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (4).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (5).png"),(self.rectangle[2],self.rectangle[3]))]
    def draw(self,screen):
        self.imageOrder=(self.imageOrder+1)%5
        self.rectangle[0]=self.rectangle[0]+self.mx*5
        self.rectangle[1]=self.rectangle[1]+self.my*5
        screen.blit(self.images[self.imageOrder], self.rectangle)
