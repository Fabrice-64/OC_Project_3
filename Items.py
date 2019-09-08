# Set up classes for OC Project3 : build a maze game
import pygame

# Pictures used in the maze are all listed here below
warden_picture = 'ressource/Gardien.png'
macgyver_picture = 'ressource/MacGyver.png'
wall_picture = 'ressource/wall.gif'
collected_objects_pictures = ['ressource/seringue.png', 'ressource/ether.png', 'ressource/aiguille.png']


class Items:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        @property
        def add_picture(self):
            # Generates the picture for each and every item described in the subclasses
            self.image = pygame.image.load(self.picture).convert()
            self.image = pygame.transform.scale(self.image, (40, 40))
            return self.image


class Warden(Items):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.picture = warden_picture


class Wall(Items):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.picture = wall_picture


class Collected(Items):
    id_counter = 0
    def __init__(self, x, y):
        super().__init__(x, y)
        self.picture = collected_objects_pictures[Collected.id_counter]
        Collected.id_counter +=1



class MacGyver(Items):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.picture = macgyver_picture

