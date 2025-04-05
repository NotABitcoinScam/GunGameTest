import pygame
import math

import GameLib

pygame.init()

INFO = pygame.display.Info()




class limb:

    def __init__(self, player, renderSurf = pygame.surface.Surface, sprite = pygame.surface.Surface, targetPos = pygame.Vector2):
        
        self.DEBUG = False
        #self.player = player
        self.renderSurf = renderSurf
        self.smoothing = 10
        self.targetPos = targetPos
        self.ogPos = targetPos
        self.position = targetPos
        self.sprite = sprite
        self.isStepping = False
        self.isAbleToStep = True
        self.idealTarget = self.targetPos

    def step(self,idealTarget):
        self.isStepping = True
        self.targetPos = idealTarget

    def update(self):

        difference = (self.targetPos - self.position)/self.smoothing
        self.position += pygame.Vector2(difference)

    def render_(self):

        self.renderSurf.blit(self.sprite, self.position - GameLib.getCenterOffset(self.sprite))
        if self.DEBUG:
            if self.isStepping:
                pygame.draw.circle(self.renderSurf,pygame.color.Color(255,0,0),self.targetPos,5)
                pygame.draw.line(self.renderSurf,pygame.color.Color(255,0,0),self.targetPos,self.targetPos)
            else:
                pygame.draw.circle(self.renderSurf,pygame.color.Color(0,255,0),self.targetPos,5)
                pygame.draw.line(self.renderSurf,pygame.color.Color(0,255,0),self.targetPos,self.targetPos)
            pygame.draw.circle(self.renderSurf, pygame.color.Color(0,0,255), self.targetPos,2.5)


class WalkingTurret():

    def __init__(self,renderedLayer, player, position = pygame.Vector2):

        self.renderSurface = renderedLayer
        

        self.headSheet = pygame.image.load("Assets/WalkingTurret/WalkingTurretBody.png").convert_alpha()
        self.slicedHeadSheet = GameLib.stripFromSheet(self.headSheet,[0,0],[16,16],1,2)
        self.headSprites = {
            "Idle" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[0],5),
            "Beep" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[1],5),
        }
        self.currentHeadSprite = self.headSprites["Idle"]


        self.legSheet = pygame.image.load("Assets/WalkingTurret/WalkingTurretLegs.png").convert_alpha()
        self.slicedLegSheet = GameLib.stripFromSheet(self.legSheet,[0,0],[16,16],1,2)
        self.legSprites = {
            "Front" : GameLib.scaleSurfaceBy(self.slicedLegSheet[0],5),
            "Back" : GameLib.scaleSurfaceBy(self.slicedLegSheet[1],5),
        }
        #self.currentLegSprite = self.legSprites["Idle"]
        

        self.player = player

        self.position = position
        self.lastPosition = position
        self.targetPosition = position
        self.rotation = 0

        self.smoothing = 30

        self.internalAnimTimer = 0
        self.animPeriod = 10
        self.animNum = 0
        self.currentLeg = 1

        self.safeRadius = 512
        self.stepDistanceMult = 10
        self.isMoving = False
        self.startPos = pygame.Vector2(0,0)
        self.moveVector = pygame.Vector2(0,0)

        self.legOffset = 32

        self.campos = pygame.Vector2(0,0)

        self.displaySprite = pygame.surface.Surface(pygame.Vector2(256,256)).convert_alpha()
        self.xLegPosMult = 0.75
        self.yLegPosMult = 0.33333

        self.speed = 3

        self.offsets=[
            pygame.Vector2(-self.legOffset*self.xLegPosMult,-self.legOffset*self.yLegPosMult) + pygame.Vector2(0,self.legOffset*0.75),
            pygame.Vector2(self.legOffset*self.xLegPosMult,-self.legOffset*self.yLegPosMult) + pygame.Vector2(0,self.legOffset*0.75),
            pygame.Vector2(-self.legOffset*self.xLegPosMult,self.legOffset*self.yLegPosMult) + pygame.Vector2(0,self.legOffset*0.75),
            pygame.Vector2(self.legOffset*self.xLegPosMult,self.legOffset*self.yLegPosMult) + pygame.Vector2(0,self.legOffset*0.75)
        ]

        self.legs = {
            'BackLeft': limb(self,self.displaySprite,self.legSprites['Back'],GameLib.getCenterOffset(self.displaySprite) + self.offsets[0]),
            'BackRight': limb(self,self.displaySprite,self.legSprites['Back'],GameLib.getCenterOffset(self.displaySprite) + self.offsets[1]),
            'FrontLeft': limb(self,self.displaySprite,self.legSprites['Front'],GameLib.getCenterOffset(self.displaySprite) + self.offsets[2]),
            'FrontRight': limb(self,self.displaySprite,self.legSprites['Front'],GameLib.getCenterOffset(self.displaySprite) + self.offsets[3]),
        }

    def update(self):

        self.targetPosition = self.player.worldPosition

        if self.position.distance_to(self.targetPosition) >= self.safeRadius * 1.25 and not self.isMoving:
            self.isMoving = True
            self.targetPosition = self.player.worldPosition
            self.startPos = self.position
            self.lerpDistance = self.position.distance_to(self.targetPosition)
            self.lerpValue = 0
        if self.position.distance_to(self.targetPosition) <= self.safeRadius * 0.5 and self.isMoving:
            self.isMoving = False
            self.lerpValue = 0


        difference = (self.targetPosition - self.position)/self.smoothing
        self.moveVector = pygame.Vector2(max(min(difference.x,self.speed),-self.speed),max(min(difference.y,self.speed),-self.speed))

        if not self.isMoving:
            self.moveVector = pygame.Vector2(0,0)

        if self.isMoving:
            self.position += self.moveVector
            self.legs['FrontRight'].targetPos -= self.moveVector
            self.legs['FrontLeft'].targetPos -= self.moveVector
            self.legs['BackRight'].targetPos -= self.moveVector
            self.legs['BackLeft'].targetPos -= self.moveVector

        #self.legs -= self.campos

        self.legs['BackLeft'].update()
        self.legs['BackRight'].update()
        self.legs['FrontLeft'].update()
        self.legs['FrontRight'].update()


        self.internalAnimTimer += 1

        #pygame.draw.circle(self.renderSurface, pygame.color.Color(255,0,0), self.position - self.campos, 5)
        #self.legs['FrontRight'].step(GameLib.getHalfScreenVector2() - GameLib.getCenterOffset(self.displaySprite))

        if self.internalAnimTimer % 60 in [0,1,2,3,4,5,6,7,8,9]:
            self.currentHeadSprite = self.headSprites['Beep']
        else:
            self.currentHeadSprite = self.headSprites['Idle']

        if self.internalAnimTimer % self.animPeriod == 0:

            #print('Test')
            
            if self.currentLeg == 1:
                self.currentLeg = 2
                self.legs['FrontRight'].step(GameLib.getCenterOffset(self.displaySprite) + self.offsets[2] + self.moveVector * self.stepDistanceMult)
                #print('1')
            elif self.currentLeg == 2:
                self.currentLeg = 3
                self.legs['FrontLeft'].step(GameLib.getCenterOffset(self.displaySprite) + self.offsets[3] + self.moveVector * self.stepDistanceMult)
                #print('2')
            elif self.currentLeg == 3:
                self.currentLeg = 4
                self.legs['BackRight'].step(GameLib.getCenterOffset(self.displaySprite) + self.offsets[0] + self.moveVector * self.stepDistanceMult)
                #print('3')
            elif self.currentLeg == 4:
                self.currentLeg = 1
                self.legs['BackLeft'].step(GameLib.getCenterOffset(self.displaySprite) + self.offsets[1] + self.moveVector * self.stepDistanceMult)
                #print('4')
            #print('---------------------------')



        self.lastPosition = self.position

    def render_(self, campos):

        self.campos = campos
        world_to_cam = self.position
        targetOffset = self.targetPosition - world_to_cam

        angle = math.degrees(math.atan2(targetOffset[1], targetOffset[0]))
        if targetOffset.x < 0:
            self.rotation -= 180
            preRotatedSprite = pygame.transform.flip(self.currentHeadSprite,False,True)
        else:
            preRotatedSprite = self.currentHeadSprite

        rotatedSprite = GameLib.rotateAtCenter(preRotatedSprite, -angle)

        headBobHeight = (math.sqrt(math.sqrt(max(abs(math.sin(self.internalAnimTimer / 30))- 0.25,0.25))) * 10) - 24
        
        self.displaySprite.fill(pygame.color.Color(0,0,0,0))

        avgLegPos = (self.legs['FrontLeft'].position + self.legs['FrontRight'].position + self.legs['BackLeft'].position + self.legs['BackRight'].position)/4

        #self.displaySprite.blit(rotatedSprite[0], rotatedSprite[1] + pygame.Vector2(128,128) - pygame.Vector2(rotatedSprite[0].get_rect().x/2,rotatedSprite[0].get_rect().y/2))

        self.legs['BackLeft'].render_()
        self.legs['BackRight'].render_()

        self.displaySprite.blit(rotatedSprite[0],avgLegPos - rotatedSprite[1] + pygame.Vector2(0,headBobHeight - self.legOffset*0.75))

        self.legs['FrontLeft'].render_()
        self.legs['FrontRight'].render_()

        #GameLib.drawLabelBox(self.displaySprite,pygame.color.Color(0,255,0),'Walking_Turret',32)

        self.renderSurface.blit(self.displaySprite, (self.position - campos) - GameLib.getCenterOffset(self.displaySprite))
