import pygame
pygame.init()



class Camera():
    
    def __init__(self, position = pygame.Vector2(0,0)):

        self.position = position
        self.moveWithArrows = False
    
    def updateKeydowns(self):

        if self.moveWithArrows:

            downKeys = pygame.key.get_pressed()

            # SET A MOVEMENT ANGLE FOR CALCULATING WHERE TO GO
            if downKeys[pygame.K_LEFT]:
                self.movingAngle = -90
            if downKeys[pygame.K_RIGHT]:
                self.movingAngle = 90
            if downKeys[pygame.K_UP]:
                self.movingAngle = 0
                if downKeys[pygame.K_LEFT]:
                    self.movingAngle = -45
                if downKeys[pygame.K_RIGHT]:
                    self.movingAngle = 45
                if downKeys[pygame.K_LEFT] and downKeys[pygame.K_RIGHT]:
                    self.movingAngle = 0
            if downKeys[pygame.K_DOWN]:
                self.movingAngle = 180
                if downKeys[pygame.K_LEFT]:
                    self.movingAngle = -135
                if downKeys[pygame.K_RIGHT]:
                    self.movingAngle = 135
                if downKeys[pygame.K_LEFT] and downKeys[pygame.K_RIGHT]:
                    self.movingAngle = 180
    def update(self):
        
        self.updateKeydowns()


def scaleSurfaceBy(surface = pygame.surface.Surface, scale = float):

    return pygame.transform.scale(surface,pygame.Vector2(surface.get_width()*scale,surface.get_height()*scale))

def getCenterOffset(surface = pygame.surface.Surface):

    return pygame.Vector2(surface.get_width()/2, surface.get_height()/2)