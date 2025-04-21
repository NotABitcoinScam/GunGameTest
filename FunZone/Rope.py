import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window")



ropePointA = pygame.Vector2(100, 300)
ropePointB = pygame.Vector2(700, 300)

ropePointNum = 8
ropeLength = 600
ropePoints = []
segmentError = 50
segmentLength = ropeLength / ropePointNum + segmentError

for i in range(ropePointNum):
    ropePoints.append(pygame.Vector2(ropePointA.x + (ropeLength / ropePointNum) * i, ropePointA.y))




# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    for i in range(ropePointNum - 1):
        pygame.draw.circle(screen, pygame.color.Color(0,0,0), ropePoints[i], 5)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()