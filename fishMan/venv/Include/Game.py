import pygame
import sys
import math
import random
from Chapter import ChapterOne
from Menu import Menu

pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Fish Man')

crashed = False

clock = pygame.time.Clock()
chapter= ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')
menu=Menu(gameDisplay.get_rect())

isLeft=False
end=False

score_font = pygame.font.Font(None, 38)
startTime = pygame.time.get_ticks()





def text_objects(text,font):
    textsurface=font.render(text,True,pygame.Color("Black"))
    return textsurface,textsurface.get_rect()

def message(text):
    text_message=pygame.font.Font(None,80)
    textsurf,textrect=text_objects(text,text_message)
    textrect.center=((800/2),(600/2))
    gameDisplay.blit(textsurf,textrect)
    pygame.display.update()
    pygame.time.wait(2)
    #Game()

def crash():
    message("GAME OVER")

def main():
    crashed=False
    isLeft=False
    end=False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    chapter.pgenerateTargetTimer.pause(True)
                    crashed = menu.runMenu(gameDisplay)
                    chapter.pgenerateTargetTimer.pause(False)
                if event.key == pygame.K_UP:
                    chapter.FishMan.my = -1
                if event.key == pygame.K_DOWN:
                    chapter.FishMan.my = 1
                if event.key == pygame.K_LEFT:
                    isLeft = True
                    chapter.FishMan.mx = -1
                if event.key == pygame.K_RIGHT:
                    chapter.FishMan.mx = 1
                    isLeft = False
                if event.key == pygame.K_SPACE:
                    if isLeft == False:
                        chapter.FishMan.fire(gameDisplay)
                    else:
                        chapter.FishMan.fireLeft(gameDisplay)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    chapter.FishMan.my = 0
                if event.key == pygame.K_DOWN:
                    chapter.FishMan.my = 0
                if event.key == pygame.K_LEFT:
                    isLeft = True
                    chapter.FishMan.mx = 0
                if event.key == pygame.K_RIGHT:
                    chapter.FishMan.mx = 0
            elif event == chapter.finishEvent:
                # print(event)
                chapter.finish((800, 600))
                crash()
                end = True

            elif event == chapter.FishMan.exposedEvent:
                print(event)
        if not end:
            chapter.draw(gameDisplay, isLeft)
            gameTime = pygame.time.get_ticks() - startTime
            chapter.drawGameTime(gameTime, gameDisplay)

        pygame.display.update()
        clock.tick(60)



main()
pygame.quit()
quit()

