import sys
import math
import pygame

class FishMan():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.imageOrder=0
        width=screen.get_width()
        height=screen.get_height()
        self.rectange=[100,int(height)-100,int(width/5),int(height/5)]
        self.fishManImages = [pygame.transform.scale(pygame.image.load("images/png/FishMan/fishman1.png")), (self.rectangle[2], self.rectangle[3]), pygame.transform.scale(pygame.image.load("images/png/FishMan/fishman2.png"), (self.rectangle[2], self.rectangle[3]))]
        self.imageOrder=0


        self.bullets = []
        self.exposed = False
        self.exposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='ManExposedEvent')



    def draw(self,screen,mx,my):
        self.imageOrder=self.imageOrder%2+1
        self.image=pygame.image.load("images/png/FishMan/fishman"+str(self.imageOrder)+".png")
        self.rectange[0]=self.rectange[0]+mx*2
        self.rectange[1]=self.rectange[1]+my*2
        self.image= pygame.transform.scale(self.image, (self.rectange[2],self.rectange[3]))


        screen.blit(self.image, self.rectange)