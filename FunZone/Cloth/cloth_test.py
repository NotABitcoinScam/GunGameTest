#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

import cloth

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('cloth?')
screen = pygame.display.set_mode((500, 500),0,32)

rag_data = cloth.load_rags('C:/Users/ariwi/Documents/Python/GunGameTest/FunZone/Cloth/rags')

#my_cloth = cloth.ClothObj(rag_data['vine']) 
my_cloth = cloth.ImageClothObj(pygame.image.load('C:/Users/ariwi/Documents/Python/GunGameTest/FunZone/Cloth/ClothTest.png').convert_alpha(), 15)

render_mode = 1

timer = 0

# Loop ------------------------------------------------------- #
while True:

    timer +=1

    # Background --------------------------------------------- #
    screen.fill((150,150,150))

    # Cloth -------------------------------------------------- #
    mx, my = pygame.mouse.get_pos()

    # move
    my_cloth.move_grounded([mx, my])

    # process
    my_cloth.update()
    my_cloth.update_sticks()

    # render
    if render_mode and not pygame.mouse.get_pressed()[1]:
        my_cloth.render_texture(screen, (255, 255, 255))
    else:
        my_cloth.render_sticks(screen)

    if mainClock.get_fps() <= 5 and timer >= 60:
        print('---------------------------------------------------------------')
        print('AUTO TERMINATION - FPS too low')
        print('---------------------------------------------------------------')
        pygame.quit()
        sys.exit()

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_r:
                if render_mode:
                    render_mode = 0
                else:
                    render_mode = 1

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
    pygame.display.set_caption('Cloth Sim - FPS: + ' + str(mainClock.get_fps()))
