import pygame
pygame.init()



class Camera():
    
    def __init__(self, position = pygame.Vector2(0,0)):

        self.position = position
        self.moveWithArrows = False
    
    def updateKeydowns(self):

        if self.moveWithArrows:
            
            camspeed = 5

            downKeys = pygame.key.get_pressed()

            # SET A MOVEMENT ANGLE FOR CALCULATING WHERE TO GO

            if downKeys[pygame.K_UP] == True or downKeys[pygame.K_DOWN] == True or downKeys[pygame.K_LEFT] == True or downKeys[pygame.K_RIGHT] == True:
                self.currentSpeed = camspeed
            else:
                self.currentSpeed = 0
            
            self.moveVector = pygame.Vector2(0,0)

            if downKeys[pygame.K_UP]:
                self.moveVector += pygame.Vector2(0,-self.currentSpeed)
            if downKeys[pygame.K_DOWN]:
                self.moveVector += pygame.Vector2(0,self.currentSpeed)
            if downKeys[pygame.K_LEFT]:
                self.moveVector += pygame.Vector2(-self.currentSpeed, 0)
            if downKeys[pygame.K_RIGHT]:
                self.moveVector += pygame.Vector2(self.currentSpeed, 0)

            self.position += self.moveVector
            
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

def stripFromSheet(sheet, start, size, columns, rows=1):
    """
    Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows.
    """
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pygame.Rect(location, size)))
    return frames

def getMouseVector2():

    return pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

def rotateAtCenter(surface, angle):
         rotated_image = pygame.transform.rotate(surface, angle)
         new_rect = getCenterOffset(rotated_image)
         return rotated_image, new_rect


if __name__ == '__main__':
    try:
        import main
    except ModuleNotFoundError:
        raise Exception("No associated main.py file found")