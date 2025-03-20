import pygame
import math

import assets
import GameLib

pygame.init()

class player:

    def __init__(self, renderedLayer = pygame.surface.Surface):

        self.worldPosition = pygame.Vector2(0,0)
        self.currentSpeed = 0
        self.facingAngle = 0
        self.movingAngle = 0
        self.moveVector = pygame.Vector2(0,0)
        self.renderedLayer = renderedLayer
        self.sprite = assets.grabTestPlayer()
        self.sprite = GameLib.scaleSurfaceBy(self.sprite,5)
        

        self.stats = {
            'Speed' : 5
        }
    
    def onPygameEventCall(self, event):

        pass

    def updateKeydowns(self):

        downKeys = pygame.key.get_pressed()

        # SET A MOVEMENT ANGLE FOR CALCULATING WHERE TO GO

        if downKeys[pygame.K_w] == True or downKeys[pygame.K_s] == True or downKeys[pygame.K_a] == True or downKeys[pygame.K_d] == True:
            self.currentSpeed = self.stats['Speed']
        else:
            self.currentSpeed = 0
        
        self.moveVector = pygame.Vector2(0,0)

        if downKeys[pygame.K_w]:
            self.moveVector += pygame.Vector2(0,-self.stats['Speed'])
        if downKeys[pygame.K_s]:
            self.moveVector += pygame.Vector2(0,self.stats['Speed'])
        if downKeys[pygame.K_a]:
            self.moveVector += pygame.Vector2(-self.stats['Speed'], 0)
        if downKeys[pygame.K_d]:
            self.moveVector += pygame.Vector2(self.stats['Speed'], 0)
        
        

    def updateMovement(self):
        self.worldPosition += self.moveVector

    def render_(self,camPos):

        self.renderedLayer.blit(self.sprite, (self.worldPosition - camPos) - GameLib.getCenterOffset(self.sprite))

    def update(self):
        
        self.updateKeydowns()
        self.updateMovement()
        
