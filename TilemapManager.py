import pygame
import GameLib

pygame.init()



dirtTiles = GameLib.stripFromSheet(pygame.image.load("Assets/Tiles/DirtTiles_1-3.png").convert(), (0,0), (16,16), 1, 3)
dirtTilemap = GameLib.tilemapManager.generateRandomDirtmap()

print(dirtTilemap)