import pygame
import sys
import math
import random
from  threading import Timer
from TargetOne import *
from FishMan import FishMan
from Bullet import Bullet
from pTimer import  pTimer





pygame.font.init()
score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
score_msg = score_font.render("Hp:", 1, pygame.Color("Purple"))
score_msg_size = score_font.size("Hp")
score_msg2 = score_font.render("Score:", 1, pygame.Color("Purple"))
score_msg_size2 = score_font.size("Score")


red=(255, 10, 10)
black=(0,0,0)


class ChapterOne():
    def __init__(self,screen):
        self.name="Let's Start"
        self.FishMan= FishMan(screen)
        self.targets=[]
        self.backGroundImage=pygame.transform.scale(pygame.image.load("images/png/seabackground.png"),(screen.get_width(), screen.get_height()))
        self.backGroundImageX=0
        self.backGroundImageY=0
        self.screen= screen



        self.pgenerateTargetTimer=pTimer(2,self.generateTarget,screen)
        self.hpLowerTimer = pTimer(3,self.FishMan.decrease,screen)


        self.finishEvent=pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')

    def start(self,screen):

        self.pgenerateTargetTimer.start()
        self.hpLowerTimer.start()
    def finish(self,screen):
        self.pgenerateTargetTimer.stop()
        self.hpLowerTimer.stop()
        pygame.event.post(self.finishEvent)

    

    def generateTarget(self,arguments):
        rnumber = random.randint(0,2)

        if rnumber == 0 :
            rnumber2 = random.randint(0, 2)
            if rnumber2==0:
                newTarget= TargetOneFromLeft(TargetOne(arguments[0]))
            elif rnumber2==1:
                newTarget= TargetTwoFromLeft(TargetOne(arguments[0]))
            else:
                newTarget= TargetThreeFromLeft(TargetOne(arguments[0]))


        elif rnumber ==1:
            rnumber3 = random.randint(0, 2)
            print('number=',rnumber3)
            if rnumber3==0:
                newTarget = TargetOne(arguments[0])
            elif rnumber3==1:
                newTarget = TargetTwo(TargetOne(arguments[0]))
            else:
                newTarget = TargetThree(TargetOne(arguments[0]))

        else :

            newTarget= Buble(TargetOne(arguments[0]))
        for t in self.targets:
            if t.y == newTarget.y and type(newTarget) != Buble:
                self.generateTarget(self,arguments)
        self.targets.append(newTarget)


    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage,(self.backGroundImageX,0))
        self.backGroundImageX=self.backGroundImageX-1
        screen.blit(self.backGroundImage,(screen.get_width()+self.backGroundImageX,0))

        if screen.get_width() == -self.backGroundImageX:
            self.backGroundImageX=0

    def drawHp(self,screen,hp):
        score_numb = score_numb_font.render(str(hp), 1, pygame.Color("red"))
        screen.blit(score_msg, (screen.get_width() - score_msg_size[0] - 60, 10))
        screen.blit(score_numb, (screen.get_width() - 45, 14))

    def drawScore(self,screen,score):
        score_numb = score_numb_font.render(str(score), 1, pygame.Color("red"))
        screen.blit(score_msg2, (screen.get_width() - score_msg_size2[0]-700, 10))
        screen.blit(score_numb, (screen.get_width() - 690, 14))

    def drawGameTime(self,gameTime,screen):
        color=black
        game_time = score_numb_font.render("Time:", 1, pygame.Color("purple"))
        if gameTime/1000>50:
            color=black

        game_time_counter = score_font.render(str(gameTime / 1000), 1, pygame.Color("red"))
        screen.blit(game_time, (screen.get_width() - score_msg_size2[0]-500, 10))
        screen.blit(game_time_counter, (screen.get_width() - 510, 14))

    def drawFishMan(self,screen):
        self.FishMan.draw(screen)

    def drawFishManLeft(self,screen):
        self.FishMan.turnLeft(screen)
        self.FishMan.turnLeft(screen)

    def drawTargets(self,screen):
        speed = 0
        for target in self.targets:
            if type(target )!= Buble :
                if type(target)==TargetOne or type(target)==TargetOneFromLeft:
                    speed=2
                elif type(target)==TargetTwo:
                    speed=3
                elif type(target)==TargetThree:
                    speed=5
                elif type(target)==TargetTwoFromLeft:
                    speed=4
                exposed=target.draw(screen,speed)

                if exposed:
                    if type(target)==TargetThree or type(target)==TargetThreeFromLeft:
                        self.FishMan.score += 10
                    elif type(target)==TargetTwo or type(target)==TargetTwoFromLeft:
                        self.FishMan.score += 5
                    else:
                        self.FishMan.score += 3

                    self.targets.remove(target)
                    if self.FishMan.exposed:
                        pygame.event.post(self.FishMan.exposedEvent)
                        self.finish(screen)

                else:
                    if target.rectangle.colliderect(self.FishMan.rectangle):
                        if not target.exposed:
                            target.expose()
                            self.FishMan.expose()

                    else:
                        for bullet in self.FishMan.bullets:
                            if target.rectangle.colliderect(bullet.rectangle):
                                target.hit()
                                self.FishMan.bullets.remove(bullet)
            else :
                exposed = target.draw(screen)
                if exposed:
                    self.targets.remove(target)
                else:
                    if target.rectangle.colliderect(self.FishMan.rectangle):
                        if not target.exposed:
                            self.FishMan.hp+=20
                            target.expose()


            
    def draw(self,screen,isLeft):
        self.drawBackGround(screen)
        if isLeft==False:
            self.drawFishMan(screen)
        else:
            self.drawFishManLeft(screen)
        self.drawTargets(screen)
        if self.FishMan.hp <= 0:
            pygame.event.post(self.finishEvent)
        self.drawHp(screen,self.FishMan.hp)
        self.drawScore(screen,self.FishMan.score)

