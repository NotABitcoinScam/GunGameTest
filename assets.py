import pygame
pygame.init()


def grabTestPlayer():
    return pygame.image.load('Assets/Characters/TestCharacter.png').convert_alpha()

def grabTestGun():
    return pygame.image.load('Assets/Guns/TestGun.png').convert_alpha()