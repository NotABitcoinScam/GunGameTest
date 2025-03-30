# IMPORT LIBRARIES
import pygame
import math
import sys


pygame.init()
# DEFINE GLOBAL VARIABLES

BG_COLOR = (50,50,50)
WINDOW_CAPTION = "Window"
PYGAME_INFO = pygame.display.Info()
SCREEN_SIZE = pygame.Vector2(PYGAME_INFO.current_w,PYGAME_INFO.current_h)
RENDERABLE_OBJECTS = []
PIXEL_SIZE = 5
RENDER_LAYERS = {
    "Floor" : pygame.surface.Surface(SCREEN_SIZE),
    "Blood" : pygame.surface.Surface(SCREEN_SIZE),
    "Debris" : pygame.surface.Surface(SCREEN_SIZE),
    "Props" : pygame.surface.Surface(SCREEN_SIZE),
    "Walls" : pygame.surface.Surface(SCREEN_SIZE),
    "EnemyOutline" : pygame.surface.Surface(SCREEN_SIZE),
    "Enemies" : pygame.surface.Surface(SCREEN_SIZE),
    "PlayerOutline" : pygame.surface.Surface(SCREEN_SIZE),
    "Player" : pygame.surface.Surface(SCREEN_SIZE),
    "MainOutline" : pygame.surface.Surface(SCREEN_SIZE),
    "Main" : pygame.surface.Surface(SCREEN_SIZE),
    "Particles" : pygame.surface.Surface(SCREEN_SIZE),
    "Light" : pygame.surface.Surface(SCREEN_SIZE),
    "Debug" : pygame.surface.Surface(SCREEN_SIZE)
}



# IMPORT CUSTOM SCRIPTS

import assets
import GameLib
import player

# MAKE WINDOW

window = pygame.display.set_mode((SCREEN_SIZE.x,SCREEN_SIZE.y-64),pygame.RESIZABLE)
pygame.display.flip()
running = True

# INIT OBJECTS

MainSurf = pygame.surface.Surface(SCREEN_SIZE)
MAIN_CAMERA = GameLib.Camera()
#MAIN_CAMERA.moveWithArrows = True
Player = player.player(MainSurf)
Player.worldPosition = pygame.Vector2(500,500)

RENDERABLE_OBJECTS.append(Player)

# DEBUG CRAP



testgunasset = assets.grabTestGun()
testgunasset = GameLib.scaleSurfaceBy(testgunasset,PIXEL_SIZE)
testgunwithoutline = GameLib.createOutline(testgunasset,PIXEL_SIZE,pygame.color.Color(255,255,255))



# DEFINE CLASSES

# DEFINE FUNCTIONS

def update_(): 
    Player.update() 

def render_():
    global MainSurf

    drawGizmos()


    # CAMERA SMOOTH =D
    smoothing = 20
    difference = (Player.worldPosition - MAIN_CAMERA.position)/smoothing
    MAIN_CAMERA.position += pygame.Vector2(difference)


    

    window.fill(BG_COLOR)
    pygame.display.set_caption(WINDOW_CAPTION)
    '''for key in RENDER_LAYERS.keys():
        window.blit(RENDER_LAYERS[key],pygame.Vector2(0,0))'''
    MAIN_CAMERA.update()
    for object in RENDERABLE_OBJECTS:
        object.render_(MAIN_CAMERA.position - SCREEN_SIZE/2)

    '''tempsurf = MainSurf
    tempsurf = GameLib.scaleSurfaceBy(MainSurf,1/PIXEL_SIZE)
    MainSurf = GameLib.scaleSurfaceBy(tempsurf,PIXEL_SIZE)'''
    
    window.blit(MainSurf,pygame.Vector2(0,0))

def drawGizmos():

    #MainSurf.blit(testgunasset,pygame.Vector2(500,500))
    #MainSurf.blit(testgunwithoutline,pygame.Vector2(600,500))

    pygame.draw.circle(MainSurf,pygame.color.Color(0,0,255),pygame.Vector2(0,0) - MAIN_CAMERA.position,15)

    pygame.draw.circle(MainSurf,pygame.color.Color(255,255,255),pygame.mouse.get_pos(),5)

    pygame.draw.line(MainSurf,pygame.color.Color(0,0,255),Player.worldPosition - MAIN_CAMERA.position, (Player.worldPosition - MAIN_CAMERA.position) + pygame.Vector2(math.cos(Player.movingAngle) * 50, math.sin(Player.movingAngle) * 50))

render_()

# INITIALIZE APP

# MAINLOOP

clock = pygame.time.Clock()

while running:
    # PER FRAME EVENTS

    update_()

    # KEYBINDS & SHIT
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            sys.exit()
            break

    WINDOW_CAPTION = 'Window - FPS: ' + str(round(clock.get_fps(),2))
            
    render_()
    pygame.display.flip()

    MainSurf.fill(BG_COLOR)

    #for key in RENDER_LAYERS.keys():
        #RENDER_LAYERS[key].fill(pygame.color.Color(0,0,0,0))

    clock.tick(60)
