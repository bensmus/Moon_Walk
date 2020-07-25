"""
Goal: pull individual sprites from sprite sheets.
Taken from: http://programarcadegames.com/python_examples/en/sprite_sheets/
"""
import pygame
import sys
#pylint: disable=no-member
pygame.init()

size = 640, 480
white = 255, 255, 255
green = 0, 255, 0
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class SheetImg:
    def __init__(self, filepath, left, top, width, height, output_scale):
        self.sprite_sheet = pygame.image.load(filepath).convert()

        # Create a new blank image
        self.img = pygame.Surface((width, height)).convert()
        
        # Copy the sprite from the large sheet onto the smaller image
        self.img.blit(self.sprite_sheet, (0, 0), (left, top, width, height))
        
        # Remove the black from the image:
        self.img.set_colorkey(black)
        
        # Scale up the image (Want each pixel to take up ~20 pixels)
        self.img = pygame.transform.scale(self.img, (width*output_scale, height*output_scale))


stand = SheetImg('astronaut_spritesheet.png', 0, 0, 16, 31, 10)
move = SheetImg('astronaut_spritesheet.png', 0, 32, 16, 31, 10)
screen.set_alpha(0)
print(screen.get_alpha())  # get_at is glitchy. 

# alpha 0 surfaces are displayed as black
# alpha is used for mixing the images

screen.blit(stand.img, (0, 0)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
       
    pygame.display.flip()