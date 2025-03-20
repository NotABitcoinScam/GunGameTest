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

# INIT OBJECTS

MAIN_CAMERA = GameLib.Camera()

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
