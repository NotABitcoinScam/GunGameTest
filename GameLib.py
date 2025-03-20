import pygame
pygame.init()



class Camera():
    
    def __init__(self, position = pygame.Vector2(0,0)):

        self.position = position


def scaleSurfaceBy(surface = pygame.surface.Surface, scale = float):

    pygame.transform.scale(surface,pygame.Vector2(surface.get_width()*scale,surface.get_height()*scale))