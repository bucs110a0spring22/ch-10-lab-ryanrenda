import pygame
import random
#model
class Ball(pygame.sprite.Sprite):
	

    def __init__(self, name, x, y, img_file):
        """"Initializes the sprite functionality and loads the image of the ball and changes its size. Also sets attributes for the ball"""
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))



      
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name 
        self.speed = 5

    def update(self):
        """"Makes the ball move back and forth on the screen"""
        if self.rect.x < 500:
          self.rect.x += 1
        if self.rect.x >= 500:
          self.rect.x = 0

