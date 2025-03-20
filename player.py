import pygame
import math

import assets

pygame.init()

class player:

    def __init__(self, renderedLayer = pygame.surface.Surface):

        self.worldPosition = pygame.Vector2(0,0)
        self.facingAngle = 0
        self.movingAngle = 0
        self.renderedLayer = renderedLayer
        self.sprite = assets.grabTestPlayer()
        

        self.stats = {
            'Speed' : 5
        }
    
    def onEventCall(self, event):

        pass

    def updateKeydowns(self):

        downKeys = pygame.key.get_pressed()

        # SET A MOVEMENT ANGLE FOR CALCULATING WHERE TO GO
        if downKeys[pygame.K_a]:
            self.movingAngle = -90
        if downKeys[pygame.K_d]:
            self.movingAngle = 90
        if downKeys[pygame.K_w]:
            self.movingAngle = 0
            if downKeys[pygame.K_a]:
                self.movingAngle = -45
            if downKeys[pygame.K_d]:
                self.movingAngle = 45
            if downKeys[pygame.K_a] and downKeys[pygame.K_d]:
                self.movingAngle = 0
        if downKeys[pygame.K_s]:
            self.movingAngle = 0
            if downKeys[pygame.K_a]:
                self.movingAngle = -135
            if downKeys[pygame.K_d]:
                self.movingAngle = 135
            if downKeys[pygame.K_a] and downKeys[pygame.K_d]:
                self.movingAngle = 0

    def updateMovement(self):
        self.worldPosition += pygame.Vector2(self.stats["Speed"] * math.cos(self.movingAngle), self.stats["Speed"] * math.sin(self.movingAngle))

    def render_(self,camPos):

        self.renderedLayer.blit()
        
