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
        self.headSheet = pygame.image.load("Assets/Characters/TestCharacter2/TestCharacter2Head-Sheet.png").convert_alpha()
        self.slicedHeadSheet = GameLib.stripFromSheet(self.headSheet,[0,0],[16,16],1,4)
        self.headSprites = {
            "Up" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[1],5),
            "Down" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[3],5),
            "Left" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[0],5),
            "Right" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[2],5)
        }
        self.currentHeadSprite = self.headSprites["Down"]
        self.halfSpriteSize = pygame.Vector2(128,128)
        self.sprite = pygame.surface.Surface((self.halfSpriteSize.x*2,self.halfSpriteSize.y*2)).convert_alpha()
        

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



        world_to_cam = self.worldPosition - camPos
        mousePosOffset = GameLib.getMouseVector2() - world_to_cam

        angle = math.atan2(mousePosOffset[1], mousePosOffset[0])
        
        if -math.pi/4 <= angle <= math.pi/4:
            self.currentHeadSprite = self.headSprites['Right']
        elif math.pi/4 < angle <= 3*math.pi/4:
            self.currentHeadSprite = self.headSprites['Down']
        elif 3*math.pi/4 < angle or angle <= -3*math.pi/4:
            self.currentHeadSprite = self.headSprites['Left']
        else: # -3*math.pi/4 < angle < -math.pi/4
            self.currentHeadSprite = self.headSprites['Up']
        angle = -self.moveVector.x



        
        self.sprite.fill(pygame.color.Color(0,0,0,0))

        self.sprite.blit(pygame.transform.rotate(self.currentHeadSprite,angle),self.halfSpriteSize - GameLib.getCenterOffset(self.currentHeadSprite))
        
        self.renderedLayer.blit(self.sprite, (self.worldPosition - camPos) - GameLib.getCenterOffset(self.sprite))

    def update(self):
        
        self.updateKeydowns()
        self.updateMovement()

if __name__ == '__main__':
    import main
        
