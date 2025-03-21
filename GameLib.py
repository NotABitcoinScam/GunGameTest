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
            
    def update(self):
        
        self.updateKeydowns()


def scaleSurfaceBy(surface = pygame.surface.Surface, scale = float):

    return pygame.transform.scale(surface,pygame.Vector2(surface.get_width()*scale,surface.get_height()*scale))

def getCenterOffset(surface = pygame.surface.Surface):

    return pygame.Vector2(surface.get_width()/2, surface.get_height()/2)

def createOutline(inputSurface = pygame.surface.Surface, pixelSize = int, color = pygame.color.Color):

    dimensions = pygame.Vector2(inputSurface.get_width(),inputSurface.get_height())

    newsurface = pygame.surface.Surface(dimensions + pygame.Vector2(2*pixelSize,2*pixelSize))

    maskSurface = pygame.mask.from_surface(inputSurface)
    maskSurface = maskSurface.to_surface(inputSurface,setcolor=color)

    newsurface.blit(maskSurface,pygame.Vector2(0,0))
    newsurface.blit(maskSurface,pygame.Vector2(pixelSize*2,0))
    newsurface.blit(maskSurface,pygame.Vector2(0,pixelSize*2))
    newsurface.blit(maskSurface,pygame.Vector2(pixelSize*2,pixelSize*2))

    newsurface.blit(inputSurface,pygame.Vector2(pixelSize,pixelSize))

    return newsurface
