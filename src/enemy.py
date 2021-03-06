import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        """"Initializes the sprite functionality and loads the image of the enemy. Also sets attributes for the enemy"""
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
        """"Makes the enemy move a random amount"""
        #print("'Update me,' says " + self.name)
        move_x = random.randrange(-1, 2)
        move_y = random.randrange(-1, 2)
        self.rect.x += move_x
        self.rect.y += move_y
