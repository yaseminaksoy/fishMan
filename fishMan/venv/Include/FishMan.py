import pygame
import sys
import math
import random
from Bullet import Bullet
class FishMan():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.hp=100
        self.mx=0
        self.my=0
        width=screen.get_width()
        height=screen.get_height()
        #self.rectangle = [100, int(height) - 100, int(width / 5), int(height / 5)]
        self.rectangle = pygame.rect.Rect(250, float(height/1.5), int(width / 5), int(height / 5))
        #self.rectangle=pygame.rect.Rect(10,int(height/2)-int(height/5/2),int(width/5),int(height/5))

        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/FishMan/fishman.png"), (self.rectangle[2], self.rectangle[3])))
        self.leftswimImage=(pygame.transform.scale(pygame.image.load("images/png/FishMan/fishmanLeft.png"), (self.rectangle[2], self.rectangle[3])))
        self.shootImageOrder=False
        self.shootImages=(pygame.transform.scale(pygame.image.load("images/png/FishMan/fishman.png"),(self.rectangle[2],self.rectangle[3])))
        self.leftShootImages = (pygame.transform.scale(pygame.image.load("images/png/FishMan/fishmanLeft.png"),
                                                   (self.rectangle[2], self.rectangle[3])))



        self.exposedImages=[pygame.transform.scale(pygame.image.load("images/png/FishMan/fishman.png"), (self.rectangle[2], self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/FishMan/fishmanLeft.png"), (self.rectangle[2], self.rectangle[3]))]

        self.score=0

        self.bullets=[]
        self.exposed=False
        self.exposedEvent=pygame.event.Event(pygame.USEREVENT, attr1='FishManExposedEvent')


    def draw(self,screen):
        if self.exposed:
            screen.blit(self.exposedImages[0], self.rectangle)
            return True
        self.rectangle[0]=self.rectangle[0]+self.mx*5
        self.rectangle[1]=self.rectangle[1]+self.my*5
        self.rectangle.clamp_ip(screen.get_rect())
        if self.shootImageOrder==True:
            screen.blit(self.swimImage, self.rectangle)
        else:
            screen.blit(self.shootImages, self.rectangle)
            self.shootImageOrder=True


        for bullet in self.bullets:
            bullet.draw(screen)
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet)

    def fire(self,screen):

        nbullet=Bullet(self)
        nbullet.mx=1
        self.bullets.append(nbullet)
        self.shootImageOrder=0

    def fireLeft(self, screen):
        nbullet = Bullet(self)
        nbullet.mx = -1
        self.bullets.append(nbullet)
        self.shootImageOrder = 0

    def expose(self):
        self.exposed=True

    def turnLeft(self, screen):
        if self.exposed:
            screen.blit(self.exposedImages[1], self.rectangle)
            return True
        self.rectangle[0] = self.rectangle[0] + self.mx * 2
        self.rectangle[1] = self.rectangle[1] + self.my * 2
        self.rectangle.clamp_ip(screen.get_rect())  # FishMan objesini ekran karesi içinde tutar
        if self.shootImageOrder == True:
            screen.blit(self.leftswimImage, self.rectangle)
        else:
            screen.blit(self.leftShootImages, self.rectangle)
            self.shootImageOrder = True

        for bullet in self.bullets:
            bullet.draw(screen)
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet)

    def decrease(self,screen):
        self.hp -=10

