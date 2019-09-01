# Set up classes for OC Project3 : build a maze game
import pygame
class Items:
    print("YES")


class Warden(Items):
    def __init__(self):
        self.image = pygame.image.load('ressource/Gardien.png').convert()

class Wall(Items):
    pass

class Collected(Items):
    pass

class MacGyver(Items):
    def __init__(self):
        self.image = pygame.image.load('ressource/MacGyver.png').convert()
