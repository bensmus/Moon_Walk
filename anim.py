"""
Goal: pull individual sprites from sprite sheets.
Taken from: http://programarcadegames.com/python_examples/en/sprite_sheets/
"""
import pygame
import sys
#pylint: disable=no-member
pygame.init()

size = 1920, 1080
white = 255, 255, 255
moongray = 137, 137, 137
green = 0, 255, 0
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class SurfId(pygame.Surface):
    ''' Give the surface a unique identifier for debugging '''

    def __init__(self, dimensions, id):
        self.id = id

        # super returns temporary object of the parent class
        super().__init__(dimensions)
    

def get_imgs(filepath, img_height, img_width, output_scale):
    ''' get a list of images from a vertical spritesheet '''

    spritesheet = pygame.image.load(filepath)

    # expecting a vertical spritesheet
    max_height = spritesheet.get_height()
    
    # integer division 
    img_count = max_height // img_height

    imgs = []
    for i in range(img_count):

        # moving down the spritesheet as we go through the loop
        top = i * img_height

        img = SurfId((img_height, img_width), i)  # using i as the id

        # draws the spritesheet onto the image starting from (0, 0)
        img.blit(spritesheet, (0, 0))

        # makes black alpha zero
        img.set_colorkey(black)

        # scale
        img = pygame.transform.scale(img, (img_width*output_scale, img_height*output_scale))

        imgs.append(img)
    
    return imgs


# imgs = get_imgs('astronaut_spritesheet.png', 32 , 32, 10)

class Player:
    # keep track of what sprite image we are currently on
    counter = 0
    def __init__(self, filepath, img_height, img_width, output_scale):
        self.imgs = get_imgs(filepath, img_height, img_width, output_scale)
        self.update()
    
    def update(self):
        self.img = self.imgs[self.counter % len(self.imgs)]
        # print(self.counter) works


time = 0
update_time = 1000
astro = Player('astronaut_spritesheet.png', 32, 32, 10)

while True:
    dt = clock.tick(60)
    time += dt

    screen.fill(moongray)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if time > update_time:
        update_time += 1000
        astro.counter += 1
        astro.update()

    print(astro.img)
    screen.blit(astro.img, (0, 0))
    pygame.display.flip()
    