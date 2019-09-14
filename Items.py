# Set up classes for OC Project3 : build a maze game
import pygame
import Maze

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
        def picture(self):
            # Generates the picture for each and every item described in the subclasses
            self.image = pygame.image.load(self.pic).convert()
            self.image = pygame.transform.scale(self.image, (40, 40))
            return self.image


class Warden(Items):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = warden_picture


class Wall(Items):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.pic = wall_picture


class Collected(Items):
    id_counter = 0
    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = collected_objects_pictures[Collected.id_counter]
        Collected.id_counter +=1


class MacGyver(Items):
    number_collected_items = 0

    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = macgyver_picture

    def move(self, walls, window):
        # Due to the size of the sprites, needs to be 40 - Issue to be solved iot to be able to change the speed
        speed = 40
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.move_down(walls, window, speed)
                if event.key == pygame.K_UP:
                    self.move_up(walls, window, speed)
                if event.key == pygame.K_LEFT:
                    self.move_left(walls, window, speed)
                if event.key == pygame.K_RIGHT:
                    self.move_right(walls, window, speed)

    # For each type of movement for McGyver, one function is defined. One additional function has
    # been set up iot draw a black square at the former coordinates of McGyver's picture
    def move_down(self, walls, window, speed):
        if (self.x, self.y + 40) not in walls:
            self.black_square(window)
            self.y += speed
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def move_up(self, walls, window, speed):
        if self.y == 0:
            window.blit(self.picture, (self.x, self.y))
        else:
            if (self.x, self.y - 40) not in walls:
                self.black_square(window)
                self.y -= speed
                window.blit(self.picture, (self.x, self.y))
            else:
                window.blit(self.picture, (self.x, self.y))

    def move_left(self, walls, window, speed):
        if (self.x-40, self.y) not in walls:
            self.black_square(window)
            self.x -= speed
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def move_right(self, walls, window, speed):
        if (self.x+40, self.y) not in walls:
            self.black_square(window)
            self.x += speed
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def black_square(self, window):
        pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, 40, 40))

    # Collecting an item when McGyver steps on it
    def collecting_item(self, window, objects_to_collect):
        for object in objects_to_collect:
            if abs(self.x - object.x) < 20 and abs(self.y - object.y) < 20:
                self.number_collected_items += 1
                pygame.draw.rect(window, (0, 0, 0), (object.x, object.y, 40, 40))
                window.blit(self.picture, (self.x, self.y))
                object.x = 1000
                object.y = 1000
                print(object.x, object.y, self.number_collected_items)