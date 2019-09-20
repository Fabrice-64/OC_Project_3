"""
    Sets up a maze based on a txt file named maze_level_1 and displays following items:
    a hero,
    a warden,
    the walls,
    the objects to be collected.
    The corridors are not conceived as objects, however, their coordinates are collected for further use

"""
import pygame
import Items
from random import randrange
import Config

MAZE_HEIGHT = MAZE_WIDTH = 600
SELECTED_FONT = "ressource/08634_ClarendonBT.ttf"


class Maze:
    def __init__(self):
        # Creates lists containing the objects of each wall sprite, the coordinates of the corridor sprites
        # Including a list containing the objects to be collected by the hero
        self.corridors = []
        self.walls = {}
        self.objects_to_collect = []
        # Set up a window for the maze. Length and height are 15 characters, sprite size is 40
        self.window = pygame.display.set_mode((MAZE_HEIGHT, MAZE_WIDTH))
        pygame.display.set_caption("OpenClassrooms - MacGyver Maze Game")
        self.my_font = pygame.font.Font(SELECTED_FONT, 24)
        self.my_font_end_game = pygame.font.Font(SELECTED_FONT, 48)
        self.text = "Score : "
        self.text_window = self.my_font.render(
            self.text, True, (125, 250, 125))

    def draw_maze(self, maze_level):
        # Explores line by line the file containing the maze iot extract the different items (walls, characters, etc)
        file = open(maze_level, "r")
        f = file.readlines()
        for j in range(len(f)):
            for i in range(len(f[j])):
                # Reminder: here are the 2 variables for the x and y of maze items. Value 40 is for the sprite size
                x = i * Config.SPRITE_SIZE
                y = j * Config.SPRITE_SIZE
                # Exploration of the file to get the different items of the maze : wall, hero, warden, corridors
                if f[j][i] == "X":
                    # Draws the walls of the maze and stores the parts of the wall in a maze
                    self.wall = Items.Wall(x, y)
                    self.wall.picture = self.draw_picture(self.wall.pic)
                    self.window.blit(self.wall.picture, (x, y))
                    self.walls[(x, y)] = self.wall
                elif f[j][i] == "W":
                    self.warden = Items.Warden(x, y)
                    self.warden.picture = self.draw_picture(self.warden.pic)
                    self.window.blit(self.warden.picture, (x, y))
                elif f[j][i] == "M":
                    self.macgyver = Items.MacGyver(x, y)
                    self.macgyver.picture = self.draw_picture(
                        self.macgyver.pic)
                    self.window.blit(self.macgyver.picture, (x, y))
                else:
                    if x < 600:
                        # Stores the empty spaces in a list, iot be used for displaying the items
                        self.corridors.append((x, y))
        # Draws the white box where the score will be displayed
        pygame.draw.rect(self.window, Config.SCORE_BACKGROUND,
                         (440, 5, 120, 30))
        self.window.blit(self.text_window, (450, 5))

    def display_objects(self):
        # Randomly displays the objects in the maze corridors
        # Chosen variables intend to lay objects far enough from warden
        number_items = len(Config.objects_to_be_collected_pictures)
        low = 1
        high = len(self.corridors) // (number_items + 2)
        # Scatters the objects on the corridors of the maze by slicing the list of corridor coordinates \
        # and randomly laying an object in this very slice
        for i in range(number_items):
            # Displays the objects in the maze and stores them in a class list
            location = randrange(low, high)
            # The coordinates of the corridors have been saved as tuples as (x,y)
            self.object_to_collect = Items.ToCollect(
                self.corridors[location][0], self.corridors[location][1])
            self.object_to_collect.picture = self.draw_picture(
                self.object_to_collect.pic)
            # Steps up to another slice of the list
            low += high
            high += high
            # Objects to collect are store in this list, iot be retrieved afterwards
            self.objects_to_collect.append(self.object_to_collect)
            self.window.blit(self.object_to_collect.picture,
                             (self.corridors[location][0], self.corridors[location][1]))
        return self.window

    def draw_picture(self, picture):
        # Generates the picture for each and every item described in the subclasses of module Items
        self.image = pygame.image.load(picture).convert()
        self.image = pygame.transform.scale(
            self.image, (Config.SPRITE_SIZE, Config.SPRITE_SIZE))
        return self.image
