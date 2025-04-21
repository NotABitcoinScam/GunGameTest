import pygame
import math

import Guns.AK_47
import Guns.AK_47.AK_47
import Guns.TestGun
import Guns.TestGun.TestGun
import assets
import GameLib
import Guns
import ToasterPet
import SmolKitty
import FunZone.Cloth.cloth

pygame.init()

INFO = pygame.display.Info()


class limb:

    def __init__(self, player, renderSurf = pygame.surface.Surface, sprite = pygame.surface.Surface, targetPos = pygame.Vector2):
        
        self.DEBUG = False
        self.player = player
        self.renderSurf = renderSurf
        self.smoothing = 3
        self.targetPos = targetPos
        self.ogPos = targetPos
        self.position = targetPos
        self.sprite = sprite
        self.isStepping = False
        self.isAbleToStep = True

    #TODO Finish the stepping

    def step(self, idealTarget):
        self.isStepping = True
        self.targetPos = idealTarget

    def update(self, idealTarget):

        difference = (self.targetPos - self.position)/self.smoothing
        self.position += pygame.Vector2(difference)

    def render_(self, idealTarget):

        self.renderSurf.blit(self.sprite, self.position - GameLib.getCenterOffset(self.sprite))
        if self.DEBUG:
            if self.isStepping:
                pygame.draw.circle(self.renderSurf,pygame.color.Color(255,0,0),self.targetPos,5)
                pygame.draw.line(self.renderSurf,pygame.color.Color(255,0,0),self.targetPos,idealTarget)
            else:
                pygame.draw.circle(self.renderSurf,pygame.color.Color(0,255,0),self.targetPos,5)
                pygame.draw.line(self.renderSurf,pygame.color.Color(0,255,0),self.targetPos,idealTarget)
            pygame.draw.circle(self.renderSurf, pygame.color.Color(0,0,255), idealTarget,2.5)



class player:

    def __init__(self, renderedLayer = pygame.surface.Surface):

        self.currentCharacter = 'Ari'

        self.hasCape = True
        self.currentFoot = 'Right'
        self.internalAnimTimer = 0
        self.bodyHeadSeperation = 40
        self.footMult = 1.35
        self.stepDistanceMult = 10
        self.worldPosition = pygame.Vector2(0,0)
        self.currentSpeed = 0
        self.facingAngle = 0
        self.movingAngle = 0
        self.headSpriteAngle = 0
        self.moveVector = pygame.Vector2(0,0)
        self.renderedLayer = renderedLayer
        self.headSheet = pygame.image.load("Assets/Characters/" + self.currentCharacter + "/Head-Sheet.png").convert_alpha()
        self.slicedHeadSheet = GameLib.stripFromSheet(self.headSheet,[0,0],[16,16],1,4)
        self.headSprites = {
            "Up" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[1],5),
            "Down" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[3],5),
            "Left" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[0],5),
            "Right" : GameLib.scaleSurfaceBy(self.slicedHeadSheet[2],5)
        }
        self.currentHeadSprite = self.headSprites["Down"]


        self.bodySheet = pygame.image.load("Assets/Characters/" + self.currentCharacter + "/Body-Sheet.png").convert_alpha()
        self.slicedBodySheet = GameLib.stripFromSheet(self.bodySheet,[0,0],[16,16],1,4)
        self.bodySprites = {
            "Up" : GameLib.scaleSurfaceBy(self.slicedBodySheet[1],5),
            "Down" : GameLib.scaleSurfaceBy(self.slicedBodySheet[3],5),
            "Left" : GameLib.scaleSurfaceBy(self.slicedBodySheet[0],5),
            "Right" : GameLib.scaleSurfaceBy(self.slicedBodySheet[2],5)
        }
        self.currentBodySprite = self.headSprites["Down"]

        self.halfSpriteSize = pygame.Vector2(128,128)
        self.sprite = pygame.surface.Surface((self.halfSpriteSize.x*2,self.halfSpriteSize.y*2)).convert_alpha()
        
        self.limbSprite = pygame.image.load("Assets/Characters/" + self.currentCharacter + "/Limb.png").convert_alpha()
        self.limbSprite = GameLib.scaleSurfaceBy(self.limbSprite,5)
        self.leftFoot = limb(self,self.sprite,self.limbSprite,pygame.Vector2(-10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize)
        self.rightFoot = limb(self,self.sprite,self.limbSprite,pygame.Vector2(10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize)
        

        self.currentGun = Guns.AK_47.AK_47.AK_47(self.sprite,self,self.halfSpriteSize)
        self.currentPet = SmolKitty.SmolKittyPet(self.renderedLayer,self,self.worldPosition)


        self.stats = {
            'Speed' : 5
        }

        if self.hasCape:
            self.frontCape = FunZone.Cloth.cloth.ImageClothObj(pygame.image.load("Assets/Characters/" + self.currentCharacter + "/Cape.png").convert_alpha(), 5)

    
    def onPygameEventCall(self, event):

        pass

    def updateKeydowns(self):
        
        downKeys = pygame.key.get_pressed()

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
        self.leftFoot.targetPos -= self.moveVector
        self.rightFoot.targetPos -= self.moveVector
        self.leftFoot.update(pygame.Vector2(-10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize + self.moveVector * self.stepDistanceMult)
        self.rightFoot.update(pygame.Vector2(10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize + self.moveVector * self.stepDistanceMult)
        
        if self.internalAnimTimer % 10 == 0:
            if self.currentFoot == 'Left':
                self.currentFoot = 'Right'
                self.leftFoot.step(pygame.Vector2(-10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize + self.moveVector * self.stepDistanceMult)
            else:
                self.currentFoot = 'Left'
                self.rightFoot.step(pygame.Vector2(10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize + self.moveVector * self.stepDistanceMult)
        self.currentPet.update()

    def render_(self,camPos):

        world_to_cam = self.worldPosition - camPos
        mousePosOffset = GameLib.getMouseVector2() - world_to_cam


        angle = math.atan2(mousePosOffset[1], mousePosOffset[0])
        self.headSpriteAngle = -self.moveVector.x
        self.bodySpriteAngle = -self.moveVector.x
        mult = 2
        if -math.pi/4 <= angle <= math.pi/4:
            self.currentHeadSprite = self.headSprites['Right']
            self.currentBodySprite = self.bodySprites['Right']
            self.headSpriteAngle -= math.degrees(angle) / 2 / mult
        elif math.pi/4 < angle <= 3*math.pi/4:
            self.currentHeadSprite = self.headSprites['Down']
            self.currentBodySprite = self.bodySprites['Down']
        elif 3*math.pi/4 < angle or angle <= -3*math.pi/4:
            self.currentHeadSprite = self.headSprites['Left']
            self.currentBodySprite = self.bodySprites['Left']
            if math.degrees(angle) >= 0:
                self.headSpriteAngle -= ((math.degrees(angle) / 2) - 90)/mult
            else:
                self.headSpriteAngle += (abs(math.degrees(angle) / 2) - 90)/mult
        else: # -3*math.pi/4 < angle < -math.pi/4
            self.currentHeadSprite = self.headSprites['Up']
            self.currentBodySprite = self.bodySprites['Up']

        headBobHeight = math.sin(((1/45)*math.pi) * self.internalAnimTimer)*2
        
        self.sprite.fill(pygame.color.Color(0,0,0,0))

        if -3*math.pi/4 < angle < -math.pi/4:
            pass
            #self.currentGun.render_(camPos)

        self.leftFoot.render_(pygame.Vector2(-10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize + self.moveVector * self.stepDistanceMult)
        self.rightFoot.render_(pygame.Vector2(10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize + self.moveVector * self.stepDistanceMult)

        rotateAdjustedBodySprite = GameLib.rotateAtCenter(self.currentBodySprite, self.bodySpriteAngle)
        self.sprite.blit(rotateAdjustedBodySprite[0],self.halfSpriteSize - rotateAdjustedBodySprite[1] + pygame.Vector2(0,self.bodyHeadSeperation/2))

        rotateAdjustedHeadSprite = GameLib.rotateAtCenter(self.currentHeadSprite,self.headSpriteAngle)
        self.sprite.blit(rotateAdjustedHeadSprite[0],self.halfSpriteSize - rotateAdjustedHeadSprite[1] + pygame.Vector2(self.moveVector.x,headBobHeight) + pygame.Vector2(0,-self.bodyHeadSeperation/2))
    
        if not -3*math.pi/4 < angle < -math.pi/4:
            #self.currentGun.render_(camPos)
            self.frontCape.render_texture(self.renderedLayer,pygame.color.Color(0,0,0),[0,0])
        else:
            pass
            #self.frontCape.render_polygon(self.renderedLayer,pygame.color.Color(0,0,0))

        
        
        #pygame.Vector2(-10,self.bodyHeadSeperation * self.footMult) + self.halfSpriteSize + self.moveVector * self.stepDistanceMult
        
        if self.currentPet.position.y <= (self.worldPosition.y + (self.bodyHeadSeperation)):
            self.currentPet.render(camPos)

        GameLib.drawLabelBox(self.sprite,pygame.color.Color(0,255,0),'Player',20)

        self.renderedLayer.blit(self.sprite, (self.worldPosition - camPos) - GameLib.getCenterOffset(self.sprite))

        
        
        if self.currentPet.position.y > (self.worldPosition.y + (self.bodyHeadSeperation)):
            self.currentPet.render(camPos)

        self.frontCape.move_grounded([self.worldPosition.x - camPos.x - self.currentBodySprite.get_width()/4 + 2, self.worldPosition.y - camPos.y + 10])
        if -3*math.pi/4 < angle < -math.pi/4:
            self.frontCape.render_texture(self.renderedLayer,pygame.color.Color(0,0,0),[0,0])

    def update(self):
        
        

        movevecconst = 0.075
        self.frontCape.update(self.moveVector * -movevecconst)
        self.frontCape.update_sticks()
        self.updateKeydowns()
        self.updateMovement()
        self.internalAnimTimer += 1

if __name__ == '__main__':
    try:
        import main
    except ModuleNotFoundError:
        raise Exception("No associated main.py file found")