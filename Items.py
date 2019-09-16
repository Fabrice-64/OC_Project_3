"""
The purpose of this class is to set up the different items displayed in the maze.
It deals as well with all the game play, including the movements, scores, and final result.

Methods are exclusively used in McGyver class, as the sole active item of the game.
"""
import pygame

import Config

SPEED = 40


class Items:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Warden(Items):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = Config.warden_picture


class Wall(Items):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = Config.wall_picture


class ToCollect(Items):
    id_counter = 0

    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = Config.objects_to_be_collected_pictures[ToCollect.id_counter]
        ToCollect.id_counter += 1


class MacGyver(Items):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.pic = Config.macgyver_picture
        self.number_collected_items = 0

    def move(self, walls, window):
        # Due to the size of the sprites, needs to be 40 - Issue to be solved iot to be able to change the speed
        speed = Config.SPRITE_SIZE
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.move_down(walls, window)
                if event.key == pygame.K_UP:
                    self.move_up(walls, window)
                if event.key == pygame.K_LEFT:
                    self.move_left(walls, window)
                if event.key == pygame.K_RIGHT:
                    self.move_right(walls, window)
            if event.type == pygame.QUIT:
                exit()

    # For each type of movement for McGyver, one function is defined.
    # One additional function has been set up iot draw a black square at the former coordinates of McGyver's picture
    def move_down(self, walls, window):
        if (self.x, self.y + Config.SPRITE_SIZE) not in walls:
            self.black_square(window, self.x, self.y)
            self.y += SPEED
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def move_up(self, walls, window):
        if self.y == 0:
            window.blit(self.picture, (self.x, self.y))
        else:
            if (self.x, self.y - Config.SPRITE_SIZE) not in walls:
                self.black_square(window, self.x, self.y)
                self.y -= SPEED
                window.blit(self.picture, (self.x, self.y))
            else:
                window.blit(self.picture, (self.x, self.y))

    def move_left(self, walls, window):
        if (self.x - Config.SPRITE_SIZE, self.y) not in walls:
            self.black_square(window, self.x, self.y)
            self.x -= SPEED
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def move_right(self, walls, window):
        if (self.x + Config.SPRITE_SIZE, self.y) not in walls:
            self.black_square(window, self.x, self.y)
            self.x += SPEED
            window.blit(self.picture, (self.x, self.y))
        else:
            window.blit(self.picture, (self.x, self.y))

    def black_square(self, window, x, y):
        # Draws a black square along with any change in the displayed characters or items
        pygame.draw.rect(window, Config.CORRIDORS_COLOR,
                         (x, y, Config.SPRITE_SIZE, Config.SPRITE_SIZE))

    def collecting_item(self, window, objects_to_collect, my_font):
        # Collecting an item when McGyver steps on it and updates the score top-right of the screen
        for object in objects_to_collect:
            if abs(self.x - object.x) <= Config.SPRITE_SIZE and abs(self.y - object.y) <= Config.SPRITE_SIZE:
                self.number_collected_items += 1
                # Reinitialize the background after picking the object
                pygame.draw.rect(window, Config.CORRIDORS_COLOR, (object.x, object.y, Config.SPRITE_SIZE,
                                                                  Config.SPRITE_SIZE))
                object.x = object.y = 1000
            # Updates the score on the screen
            add_score = str(self.number_collected_items)
            text = add_score
            pygame.draw.rect(window, Config.SCORE_BACKGROUND, (530, 5, 30, 30))
            text_window = my_font.render(text, True, Config.SCORE_COLOR)
            window.blit(text_window, (540, 5))

    def meeting_warden(self, warden, window, my_font_end_game):
        # This is to set the behavior of both McGyver and the warden when they meet eachother
        if abs(self.x - warden.x) <= Config.SPRITE_SIZE and abs(self.y - warden.y) <= Config.SPRITE_SIZE:
            if self.number_collected_items == 3:
                # Removing the warden and victory for McGyver if he has collected the 3 items.
                self.black_square(window, warden.x, warden.y)
                warden.x = warden.y = 1000
                window.blit(warden.picture, (warden.x, warden.y))
                text = "Gagné !"
                text_window = my_font_end_game.render(
                    text, True, (125, 250, 125))
                window.blit(text_window, (200, 200))
            else:
                # Putting McGyver into custody if he didn't collect the three items.
                self.black_square(window, self.x, self.y)
                self.x = 80
                self.y = 480
                window.blit(self.picture, (self.x, self.y))
                text = "Perdu !"
                text_window = my_font_end_game.render(text, True, (200, 0, 0))
                window.blit(text_window, (200, 200))
