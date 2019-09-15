# Set up classes for OC Project3 : build a maze game
import pygame

# Pictures used in the maze are all listed here below
warden_picture = 'ressource/Gardien.png'
macgyver_picture = 'ressource/MacGyver.png'
wall_picture = 'ressource/wall.gif'
collected_objects_pictures = ['ressource/seringue.png', 'ressource/ether.png', 'ressource/aiguille.png']

CORRIDORS_COLOR = (0,0,0)
SPRITE_SIZE = 40

class Items:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def picture(self):
        # Generates the picture for each and every item described in the subclasses
        self.image = pygame.image.load(self.pic).convert()
        self.image = pygame.transform.scale(self.image, (SPRITE_SIZE, SPRITE_SIZE))
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

    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = macgyver_picture
        self.number_collected_items = 0

    def move(self, walls, window):
        # Due to the size of the sprites, needs to be 40 - Issue to be solved iot to be able to change the speed
        speed = SPRITE_SIZE
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
            if event.type == pygame.QUIT:
                exit()

    # For each type of movement for McGyver, one function is defined.
    # One additional function has been set up iot draw a black square at the former coordinates of McGyver's picture
    def move_down(self, walls, window, speed):
        if (self.x, self.y + SPRITE_SIZE) not in walls:
            self.black_square(window, self.x, self.y)
            self.y += speed
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def move_up(self, walls, window, speed):
        if self.y == 0:
            window.blit(self.picture, (self.x, self.y))
        else:
            if (self.x, self.y - SPRITE_SIZE) not in walls:
                self.black_square(window, self.x, self.y)
                self.y -= speed
                window.blit(self.picture, (self.x, self.y))
            else:
                window.blit(self.picture, (self.x, self.y))

    def move_left(self, walls, window, speed):
        if (self.x - SPRITE_SIZE, self.y) not in walls:
            self.black_square(window, self.x, self.y)
            self.x -= speed
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def move_right(self, walls, window, speed):
        if (self.x + SPRITE_SIZE, self.y) not in walls:
            self.black_square(window, self.x, self.y)
            self.x += speed
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def black_square(self, window, x, y):
        pygame.draw.rect(window, CORRIDORS_COLOR, (x, y, SPRITE_SIZE, SPRITE_SIZE))

    def collecting_item(self, window, objects_to_collect, my_font):
        # Collecting an item when McGyver steps on it and updates the score top-right of the screen
        for object in objects_to_collect:
            if abs(self.x - object.x) <= SPRITE_SIZE and abs(self.y - object.y) <= SPRITE_SIZE:
                self.number_collected_items += 1
                # Reinitialize the background after picking the object
                pygame.draw.rect(window, CORRIDORS_COLOR, (object.x, object.y, SPRITE_SIZE, SPRITE_SIZE))
                object.x = object.y = 1000
                window.blit(self.picture, (object.x, object.y))
            # Updates the score on the screen
            add_score = str(self.number_collected_items)
            text = add_score
            pygame.draw.rect(window, (255, 255, 255), (530, 5, 30, 30))
            text_window = my_font.render(text, True, (125, 250, 125))
            window.blit(text_window, (540, 5))

    def meeting_warden(self, warden, window, my_font_end_game):
        if abs(self.x - warden.x) <= SPRITE_SIZE and abs(self.y - warden.y) <= SPRITE_SIZE:
            if self.number_collected_items == 3:
                self.black_square(window, warden.x, warden.y)
                warden.x = warden.y = 1000
                window.blit(warden.picture, (warden.x, warden.y))
                text = "Gagné !"
                text_window = my_font_end_game.render(text, True, (125, 250, 125))
                window.blit(text_window, (200, 200))

            else:
                self.black_square(window, self.x, self.y)
                self.x = 80
                self.y = 480
                window.blit(self.picture, (self.x, self.y))
                text = "Perdu !"
                text_window = my_font_end_game.render(text, True, (200, 0, 0))
                window.blit(text_window, (200, 200))
