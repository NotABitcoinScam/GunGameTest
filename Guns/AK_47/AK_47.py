import pygame
import math
import sys

import GameLib

pygame.init()

INFO = pygame.display.Info()


class AK_47():
    
    def __init__(self, renderSurface, player, position = pygame.Vector2):

        self.renderSurface = renderSurface

        self.sprite = GameLib.scaleSurfaceBy(pygame.image.load('Guns/AK_47/AK_47.png').subsurface(pygame.rect.Rect(0,6,16,6)).convert_alpha(),5)
        self.projectileSprite = pygame.image.load('Guns/AK_47/AK_47_Projectile.png').subsurface(pygame.rect.Rect(0,0,5,3)).convert_alpha()

        self.player = player

        self.position = position# - GameLib.getCenterOffset(self.sprite)
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
        self.rotation = -math.degrees(self.rotation)
        if GameLib.getMouseVector2().x < INFO.current_w/2:
            self.rotation -= 180
            preRotatedSprite = pygame.transform.flip(self.sprite,True,False)
        else:
            preRotatedSprite = self.sprite

        rotatedSprite = GameLib.rotateAtCenter(preRotatedSprite, self.rotation)

        #pygame.draw.rect(rotatedSprite[0],pygame.color.Color(0,255,0),rotatedSprite[0].get_rect(),2)
        GameLib.drawLabelBox(rotatedSprite[0],pygame.color.Color(0,225,0),'AK-47', 20)

        self.renderSurface.blit(rotatedSprite[0], self.position - rotatedSprite[1] + pygame.Vector2(128,128) - pygame.Vector2(rotatedSprite[0].get_rect().x/2,rotatedSprite[0].get_rect().y/2))

        

    def shoot(self):

        pass