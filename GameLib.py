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

    maskSurface = pygame.mask.from_surface(inputSurface)

    dimensions = pygame.Vector2(maskSurface.get_rect().x,maskSurface.get_rect().y)

    newsurface = pygame.surface.Surface(dimensions + pygame.Vector2(2*pixelSize,2*pixelSize))

    maskSurface = maskSurface.to_surface(newsurface,setcolor=color)

    newsurface.blit(maskSurface,pygame.Vector2(0,0))
    newsurface.blit(maskSurface,pygame.Vector2(pixelSize*2,0))
    newsurface.blit(maskSurface,pygame.Vector2(0,pixelSize*2))
    newsurface.blit(maskSurface,pygame.Vector2(pixelSize*2,pixelSize*2))

    newsurface.blit(inputSurface,pygame.Vector2(pixelSize,pixelSize))

    return newsurface
