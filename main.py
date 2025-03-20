# IMPORT LIBRARIES
import pygame
import math


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

MAIN_CAMERA = GameLib.Camera()
Player = player.player(RENDER_LAYERS["Player"])
Player.worldPosition = pygame.Vector2(500,500)

RENDERABLE_OBJECTS.append(Player)

# DEFINE CLASSES

# DEFINE FUNCTIONS

def update_():
    Player.update()

def render_():
    window.fill(BG_COLOR)
    pygame.display.set_caption(WINDOW_CAPTION)
    for layer in RENDER_LAYERS.values():
        window.blit(layer,pygame.Vector2(0,0))
    for object in RENDERABLE_OBJECTS:
        object.render_(MAIN_CAMERA.position)

def drawGizmos():
    pygame.draw.circle(RENDER_LAYERS["Debug"],pygame.color.Color(255,255,255),pygame.mouse.get_pos(),5)

render_()

# INITIALIZE APP

# MAINLOOP

while running:
    # PER FRAME EVENTS

    update_()

    # KEYBINDS & SHIT
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            break
            
    render_()
    pygame.display.flip()
