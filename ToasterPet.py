import pygame
import math
import sys
import random

import GameLib

pygame.init()

INFO = pygame.display.Info()



class ToasterPet():

    """+1 Toasting Power!!!"""

    def __init__(self, renderSurface, player, position = pygame.Vector2):

        self.renderSurface = renderSurface
        self.idleSprite = GameLib.scaleSurfaceBy(pygame.image.load("Assets/TOASTER/Toaster.png"),5)
        self.runSpriteSheet = GameLib.scaleSurfaceBy(pygame.image.load("Assets/TOASTER/ToasterRun.png").convert_alpha(),5)
        self.slicedRunSheet = GameLib.stripFromSheet(self.runSpriteSheet,[0,0],[16*5,16*5],1,4)
        self.currentSprite = self.idleSprite

        self.player = player

        self.position = position# - GameLib.getCenterOffset(self.sprite)
        self.targetPosition = position
        self.rotation = 0

        self.smoothing = 30

        self.internalAnimTimer = 0
        self.animPeriod = 7
        self.animNum = 0

        self.safeRadius = 256
        self.isMoving = False
        self.startPos = pygame.Vector2(0,0)
        self.lerpValue = 0
        self.maxLerpValue = 0.2
        self.lerpDistance = 0

        self.campos = pygame.Vector2(0,0)

        self.displaySprite = pygame.surface.Surface(pygame.Vector2(16*5,16*5)).convert_alpha()

    def update(self):
        if self.position.distance_to(self.player.worldPosition) >= self.safeRadius * 1.25 and not self.isMoving:
            self.isMoving = True
            self.targetPosition = self.player.worldPosition
            self.startPos = self.position
            self.lerpDistance = self.position.distance_to(self.targetPosition)
            self.lerpValue = 0
        if self.position.distance_to(self.player.worldPosition) <= self.safeRadius * 0.5 and self.isMoving:
            self.isMoving = False
            self.lerpValue = 0
        if self.isMoving:
            difference = (self.targetPosition - self.position)/self.smoothing
            self.position += pygame.Vector2(max(min(difference.x,5),-5),max(min(difference.y,5),-5))
            self.lerpValue += 1
        self.internalAnimTimer += 1
        if self.internalAnimTimer % self.animPeriod == 0:
            self.animNum += 1
            if self.animNum >= 4:
                self.animNum = 0
        if self.isMoving:
            self.currentSprite = self.slicedRunSheet[self.animNum]
        else:
            self.currentSprite = self.idleSprite

    def render(self,campos):
        self.displaySprite.fill(pygame.color.Color(0,0,0,0))
        self.displaySprite.blit(self.currentSprite,pygame.Vector2(0,0))
        #GameLib.drawLabelBox(self.displaySprite,pygame.color.Color(0,255,0),"IsMoving: " + str(self.isMoving),15)
        #pygame.draw.circle(self.renderSurface,pygame.color.Color(0,0,255),self.position - campos,self.safeRadius,1)
        #pygame.draw.circle(self.renderSurface,pygame.color.Color(0,0,255),self.player.worldPosition - campos,self.safeRadius,1)
        
        self.renderSurface.blit(self.displaySprite, (self.position - campos) - GameLib.getCenterOffset(self.displaySprite))