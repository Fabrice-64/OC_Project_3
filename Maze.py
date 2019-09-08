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


class Maze:
    def __init__(self):
        # Creates lists containing the objects of each wall sprite, the coordinates of the corridor sprites
        # Including a list containing the objects to be collected by the hero
        self.walls = []
        self.corridors = []
        self.objects_to_collect = []

    def draw_maze(self, maze_window, maze_level):
        # Explores line by line the file containing the maze iot extract the different items (walls, characters, etc)
        maze = open(maze_level, "r")
        f = maze.readlines()
        maze_window.fill((0, 0, 0))
        i = 0
        for j in range(len(f)):
            for i in range(len(f[j])):
                # Definition of the 2 variables for the x and y of maze items. Value 40 is for the sprite size
                x = i * 40
                y = j * 40
                # Exploration of the file to get the different items of the maze : wall, hero, warden, corridors
                if f[j][i] == "X":
                    # Draws the walls of the maze
                    wall = Items.Wall(x, y)
                    maze_window.blit(wall.add_picture, (x, y))
                    self.walls.append(wall)
                elif f[j][i] == "W":
                    warden = Items.Warden(x, y)
                    maze_window.blit(warden.add_picture, (x, y))
                elif f[j][i] == "M":
                    macgyver = Items.MacGyver(x, y)
                    maze_window.blit(macgyver.add_picture, (x, y))
                else:
                    if x < 600:
                        self.corridors.append((x, y))

    def display_objects(self, maze_window):
        # Randomly displays the objects in the maze corridors
        # Chosen variables intend to lay objects far enough from warden
        number_items = len(Items.collected_objects_pictures)
        low = 5
        high = len(self.corridors) // (number_items + 2)
        # Scatters the objects on the corridors of the maze by slicing the list of corridor coordinates
        # and randomly laying an object in this very slice
        for i in range(len(Items.collected_objects_pictures)):
            # Displays the objects in the maze and stores them in a class list
            location = randrange(low, high)
            print(low, " ", high, " ", location, " ", number_items)
            collected_object = Items.Collected(self.corridors[location][0], self.corridors[location][1])
            low += high
            high += high
            self.objects_to_collect.append(collected_object)
            print(self.objects_to_collect)
            maze_window.blit(collected_object.add_picture, (self.corridors[location][0], self.corridors[location][1]))

        pygame.display.flip()
        return maze_window
