import pygame
import math
import sys

import GameLib
import player



class AK_47():
    
    def __init__(self, renderSurface = pygame.surface.Surface, player = player.player, position = pygame.Vector2):

        self.renderSurface = renderSurface

        self.sprite = pygame.image.load('AK-47.png').subsurface(pygame.rect.Rect(0,6,16,6)).convert_alpha()
        self.projectileSprite = pygame.image.load('AK-47_Projectile.png').subsurface(pygame.rect.Rect(0,0,5,3)).convert_alpha()

        self.player = player

        self.position = position
        self.targetPosition = position
        self.rotation = 0

        self.smoothing = 5


    def update(self):

        pass

    def render_(self, camPos):

        world_to_cam = self.player.worldPosition - camPos
        self.position = (self.targetPosition - self.position) / self.smoothing
        mousePosOffset = GameLib.getMouseVector2() - world_to_cam

        self.rotation = math.atan2(mousePosOffset[1], mousePosOffset[0])

        self.renderSurface.blit(GameLib.rotateAtCenter(self.sprite, self.rotation), self.position)

        

    def shoot(self):

        pass