# IMPORT LIBRARIES
import pygame
import math

# IMPORT CUSTOM SCRIPTS

import assets
import GameLib
import player


pygame.init()
# DEFINE GLOBAL VARIABLES

BG_COLOR = (50,50,50)
WINDOW_CAPTION = "Window"
PYGAME_INFO = pygame.display.Info()
SCREEN_SIZE = pygame.Vector2(PYGAME_INFO.current_w,PYGAME_INFO.current_h)
RENDERABLE_OBJECTS = []
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
    "Light" : pygame.surface.Surface(SCREEN_SIZE)
}

# INIT OBJECTS

MAIN_CAMERA = GameLib.Camera()
Player = player.player()

# DEFINE CLASSES

# DEFINE FUNCTIONS

def update_():
    pass

def render_():
    window.fill(BG_COLOR)
    pygame.display.set_caption(WINDOW_CAPTION)
    for object in RENDERABLE_OBJECTS:
        object.render_(MAIN_CAMERA.position)

# MAKE WINDOW

window = pygame.display.set_mode((SCREEN_SIZE.x,SCREEN_SIZE.y-64),pygame.RESIZABLE)
pygame.display.flip()
running = True
render_()

# INITIALIZE APP

# MAINLOOP

while running:
    # PER FRAME EVENTS

    update_()
    render_()

    # KEYBINDS & SHIT
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            break
            
    
    pygame.display.flip()
