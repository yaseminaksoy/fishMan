import pygame
import sys
from FishMan import FishMan
pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False




clock = pygame.time.Clock()
backGroundImage=pygame.image.load("images/png/seabackground.png")
backGroundImage= pygame.transform.scale(backGroundImage, (gameDisplay.get_width(), gameDisplay.get_height()))

 #ekranı her framede tekrar çizdiriyoruz
gameFishMan=FishMan(gameDisplay)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.blit(backGroundImage,(0,0))
    gameFishMan.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()