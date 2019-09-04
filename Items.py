# Set up classes for OC Project3 : build a maze game
import pygame
class Items:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_picture(self):
    # Generates the picture for each and every item described in the subclasses
        self.image = pygame.image.load(self.picture).convert()
        self.image = pygame.transform.scale(self.image, (40, 40))
        return self.image

class Warden(Items):
    def __init__(self):
        self.picture = 'ressource/Gardien.png'

class Wall(Items):
    pass

class Collected(Items):
    pass

class MacGyver(Items):
    def __init__(self):
        self.picture = 'ressource/MacGyver.png'

