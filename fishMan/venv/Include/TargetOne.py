import pygame
import sys
import math
import random


class TargetOne():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx = 1
        self.mxleft = -1
        self.my = 0
        self.speed=0
        self.life = 100
        self.screen = screen
        width = screen.get_width()
        height = screen.get_height()
        self.y = random.randint(10, height - int(height / 5))
        self.rectangle = pygame.rect.Rect(width + int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 20),
                                          int(height / 10))

        #self.swimImageOrder = 0

        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/Fish/purpleFish.png"),
                                                     (self.rectangle[2], self.rectangle[3])))
        self.leftswimImage=(pygame.transform.scale(pygame.image.load("images/png/Fish/purpleFishRight.png"),
                                                         (self.rectangle[2], self.rectangle[3])))

        self.explosionImageOrder = False
        self.leftExplosionImages = []

        self.explosionImages=(pygame.transform.scale(pygame.image.load("images/png/Fish/purpleFish.png"),
                                                           (self.rectangle[2] * 4, self.rectangle[2] * 4)))

        self.exposed = False

    def draw(self, screen,speed):
        self.speed = speed
        if self.explosionImageOrder == False:
            self.rectangle[0] = self.rectangle[0] - self.mx * self.speed
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.swimImage,
                        [self.rectangle[0] - int(self.swimImage.get_width() / 2),
                         self.rectangle[1] - int(self.swimImage.get_height() / 2)])
        else:
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * self.speed
            if self.explosionImageOrder == True:
                return True
            screen.blit(self.explosionImages,
                        [self.rectangle[0] - int(self.explosionImages.get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages.get_height() / 2)])
            if self.explosionImageOrder == True:
                self.explosionImageOrder = False
        return False

    def hit(self):
        self.life = self.life - 50
        if self.life <= 0:
            self.expose()

    def expose(self):
        self.life = 0
        self.exposed = True
        if self.explosionImageOrder==False:
            self.explosionImageOrder = True


class TargetOneFromLeft(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)

        self.mx = -1
        width = TargetOne.screen.get_width()
        height = TargetOne.screen.get_height()
        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/Fish/purpleFishRight.png"),
                                                     (self.rectangle[2], self.rectangle[3])))
        self.rectangle = pygame.rect.Rect(0 - int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 20),
                                          int(height / 10))

        self.ExplosionImages=(pygame.transform.scale(pygame.image.load("images/png/Fish/purpleFishRight.png"),
                                                           (self.rectangle[2] * 4, self.rectangle[2] * 4)))


class TargetTwoFromLeft(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)

        self.mx = -1
        width = TargetOne.screen.get_width()
        height = TargetOne.screen.get_height()
        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/Fish/babyShark.png"),
                                                     (self.rectangle[2], self.rectangle[3])))
        self.rectangle = pygame.rect.Rect(0 - int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 20),
                                          int(height / 10))

        self.ExplosionImages=(pygame.transform.scale(pygame.image.load("images/png/Fish/babyShark.png"),
                                                           (self.rectangle[2] * 4, self.rectangle[2] * 4)))

class TargetThreeFromLeft(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)
        self.mx = -1
        width = TargetOne.screen.get_width()
        height = TargetOne.screen.get_height()
        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/Fish/seaHorseFromLeft.png"),
                                                     (self.rectangle[2], self.rectangle[3])))
        self.rectangle = pygame.rect.Rect(0 - int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 20),
                                          int(height / 10))

        self.ExplosionImages=(pygame.transform.scale(pygame.image.load("images/png/Fish/seaHorseFromLeft.png"),
                                                           (self.rectangle[2] * 4, self.rectangle[2] * 4)))


class TargetTwo(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)
        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/Fish/yellowFish.png"),(self.rectangle[2], self.rectangle[3])))


        self.ExplosionImages=(pygame.transform.scale(pygame.image.load("images/png/Fish/yellowFish.png"),
                                                           (self.rectangle[2] * 4, self.rectangle[2] * 4)))


class TargetThree(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)
        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/Fish/seaHorse.png"),(self.rectangle[2], self.rectangle[3])))


        self.ExplosionImages=(pygame.transform.scale(pygame.image.load("images/png/Fish/seaHorse.png"),
                                                           (self.rectangle[2] * 4, self.rectangle[2] * 4)))


class Buble(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)

        self.mx = -1
        self.my = 1
        width = TargetOne.screen.get_width()
        height = TargetOne.screen.get_height()
        self.swimImage=(pygame.transform.scale(pygame.image.load("images/png/Buble/buble.png"),
                                                     (self.rectangle[2], self.rectangle[3])))
        self.x = random.randint(0, width)

        self.rectangle = pygame.rect.Rect(self.x, -15, int(width / 20),
                                          int(height / 10))


    def draw(self, screen):
        if self.explosionImageOrder == False:
            # self.swimImageOrder=(self.swimImageOrder+1)%10
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            self.rectangle[1] = self.rectangle[1] + self.my * 2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.swimImage,
                        [self.rectangle[0] - int(self.swimImage.get_width() / 2),
                         self.rectangle[1] - int(self.swimImage.get_height() / 2)])
        else:
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 2
            if self.explosionImageOrder == True:
                return True
            screen.blit(self.explosionImages,
                        [self.rectangle[0] - int(self.explosionImages.get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages.get_height() / 2)])
            if self.explosionImageOrder == True:
                self.explosionImageOrder = False
        return False






