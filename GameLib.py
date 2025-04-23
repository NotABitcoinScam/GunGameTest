import pygame
import math
import random
pygame.init()

INFO = pygame.display.Info()

pygame.font.init()



class tilemapManager():

    def __init__(self):
        self.dirtTiles = stripFromSheet(scaleSurfaceBy(pygame.image.load("Assets/Tiles/DirtTiles_1-3.png").convert(),5), (0,0), (16*5,16*5), 1, 3)
        self.dimensions = pygame.Vector2(36,24)
        self.dirtTilemap = self.generateRandomDirtmap()

        self.tilemapImage = pygame.surface.Surface((36*5*16,24*5*16)).convert()
        self.tilemapImage.fill((0,0,0,0))

        self.drawDirtmap(self.dirtTiles,self.dirtTilemap,self.tilemapImage,pygame.Vector2(0,0))

    # TILEMAP DIMENSIONS
    # [240,135]
    # [48,27]

    def generateRandomDirtmap(self):
        # ADD RANDOM ROTATION TO TILE DATA FOR MORE VARIATION
        tilemap = []
        for y in range(0,int(self.dimensions.y)):
            row = []
            for x in range(0,int(self.dimensions.x)):
                row.append([random.randint(0,2),pygame.Vector2(x*5*16,y*5*16)])
            tilemap.append(row)
        return tilemap
    
    def generateRandomGrassmap(self):
        # ADD RANDOM ROTATION TO TILE DATA FOR MORE VARIATION
        tilemap = []
        for y in range(0,int(self.dimensions.y)):
            row = []
            for x in range(0,int(self.dimensions.x)):
                row.append([random.randint(0,1),pygame.Vector2(x*5*16,y*5*16)])
            tilemap.append(row)
        return tilemap
    
    def renderTilemap(self,camera,surface = pygame.surface.Surface):
        #cameraRect = pygame.Rect(camera.position.x,camera.position.y,surface.get_width(),surface.get_height())
        surface.blit(self.tilemapImage,-camera.position)
        
    
    def drawDirtmap(self,tileset,tilemap,surface,offset):
        for y in range(0,int(self.dimensions.y)):
            for x in range(0,int(self.dimensions.x)):
                tile = tilemap[y][x][0]
                position = tilemap[y][x][1] - offset
                if tile == 0:
                    surface.blit(tileset[0],position)
                elif tile == 1:
                    surface.blit(tileset[1],position)
                elif tile == 2:
                    surface.blit(tileset[2],position)


    def drawGrassmap(self,tileset,tilemap,surface,offset):
        pass
                

    def sliceTilemap_15(tilemap_path, tile_scale, mode = 'both'):
    
        tileDictionary = {}
        tileArray = []

        tilemapImage = pygame.image.load(tilemap_path).convert_alpha()
        tilemapImage = scaleSurfaceBy(tilemapImage, tile_scale)

        slicedTiles = stripFromSheet(tilemapImage, (0,0), (tile_scale,tile_scale), 4, 4, 'grid')
        tileArray = slicedTiles

        tileDictionary = {
            'TopRightOuter' : tileArray[0][0],
            'MidLeftEdge' : tileArray[0][1],
            'BottomLeftInner' : tileArray[0][2],
            'MidTopEdge' : tileArray[0][3],

            'DiagonalDown' : tileArray[1][0],
            'BottomRightInner' : tileArray[1][1],
            'Center' : tileArray[1][2],
            'TopLeftInner' : tileArray[1][3],

            'BottomLeftOuter' : tileArray[2][0],
            'MidBottomEdge' : tileArray[2][1],
            'TopRightInner' : tileArray[2][2],
            'MidRightEdge' : tileArray[2][3],

            'BLANK_N/A' : tileArray[3][0],
            'TopLeftOuter' : tileArray[3][1],
            'DiagonalUp' : tileArray[3][2],
            'BottomRightOuter' : tileArray[3][3]
        }

        if mode == 'Array':
            return tileArray
        elif mode == 'Dictionary':
            return tileDictionary
        elif mode == 'both':
            return tileArray, tileDictionary
        

    
        



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

    maskSurface = pygame.mask.from_surface(inputSurface.copy())

    dimensions = pygame.Vector2(maskSurface.get_size()[0] + (2*pixelSize), maskSurface.get_size()[1] + (2*pixelSize))

    newsurface = pygame.surface.Surface(dimensions).convert_alpha()
    newsurface.fill((0,0,0,0))

    if color == pygame.color.Color(0,0,0):
        color = pygame.color.Color(1,1,1)
    maskSurface = maskSurface.to_surface(newsurface.copy(),setcolor=color, unsetcolor=(0,0,0,0))
    maskSurface.set_colorkey((0,0,0))
    
    newsurface.blit(maskSurface,pygame.Vector2(0,pixelSize)) # Left
    newsurface.blit(maskSurface,pygame.Vector2(pixelSize*2,pixelSize)) # Right
    newsurface.blit(maskSurface,pygame.Vector2(pixelSize,0)) # Up
    newsurface.blit(maskSurface,pygame.Vector2(pixelSize,pixelSize*2)) # Down
    
    newsurface.blit(inputSurface,pygame.Vector2(pixelSize,pixelSize))

    return newsurface


def stripFromSheet(sheet, start, size, columns, rows=1, mode = 'list'):
    """
    Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows.
    """
    if mode == 'list':
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                frames.append(sheet.subsurface(pygame.Rect(location, size)))
    elif mode == 'grid':
        frames = []
        for j in range(rows):
            row = []
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                row.append(sheet.subsurface(pygame.Rect(location, size)))
            frames.append(row)
    
    return frames

def getMouseVector2():

    return pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

def rotateAtCenter(surface, angle):
         rotated_image = pygame.transform.rotate(surface, angle)
         new_rect = getCenterOffset(rotated_image)
         return rotated_image, new_rect

def drawLabelBox(surface = pygame.surface.Surface, color = pygame.color.Color, text = str, size = int):
    pygame.draw.rect(surface,color,surface.get_rect(),2)
    font = pygame.font.SysFont(pygame.font.get_default_font(),size)
    textSurface = font.render(text,False,color)
    surface.blit(textSurface,pygame.Vector2(2,2))

#def vectorDistance(inp1,inp2):
#    return pygame.Vector2(math.sqrt(inp1.x**2 - inp2.x**2),math.sqrt(inp1.y**2 - inp2.y**2))

def getHalfScreenVector2():
    return pygame.Vector2(INFO.current_w/2,INFO.current_h/2)

def getScreenVector2():
    return pygame.Vector2(INFO.current_w,INFO.current_h)

def alignPixelsToGrid(surface, pixelSize):
    newsurface = surface.copy()
    newsurface = pygame.transform.scale(newsurface,pygame.Vector2(surface.get_width()/pixelSize,surface.get_height()/pixelSize))
    newsurface = pygame.transform.scale(newsurface,pygame.Vector2(surface.get_width(),surface.get_height()))
    return newsurface


def replaceColor(surface, currentColor, newColor):

    new_surface = surface.copy()
    pixel_array = pygame.PixelArray(new_surface)
    pixel_array.replace(currentColor, newColor)
    del pixel_array
    
    return new_surface





if __name__ == '__main__':
    try:
        import main
    except ModuleNotFoundError:
        raise Exception("No associated main.py file found")