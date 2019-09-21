"""
    This is a maze game developed in the framework of OpenClassrooms education
    program as Python Developper.

    Purpose of the game: the hero must exit the maze. In order to to so, he has to collect 3 items;
    a needle,
    a PVC tube,
    a flask of ether.
    The 3 items are randomly scattered in the maze.
And then the hero inject the warden the drug
    If he fails, he dies.

    The game is organized as follows:
        1. Set up of a window containing a maze, with its walls, corridors, the items to be collected by the hero
            and a warden.
        2.Inside a game loop, three phases:
            Phase 1: the hero moves,
            Phase 2: it checks whether an item can be collected,
            Phase 3: it checks how far the hero is from the warden, therefore if the game is to be ended.

    Classes :
    Items, which includes:
        MacGyver,
        Warden,
        Walls,
        Collected
    Maze, which aims at drawing the maze

    Methods in main:
        Main doesn't contain any method. They are all to be found either in Maze or Items modules

    Attributes in main:
        Main doesn't contain any attributes. They are all to be found either in Maze, or Items, or Config modules

    This program is based on Python 3.7.4 and Pygame 1.9.3
"""
import pygame
import Items
from Maze import Maze

pygame.init()

# Creates an instance to open a file containing the maze and build it up subsequently
maze = Maze()
maze.draw_maze(maze_level="maze_level_1")
maze.display_objects()

# Updates the maze_window
pygame.display.flip()

# Keeps the window open until intentionally closed
running = True
while running:
    # This loop goes through the 3 main phases of this game: movement, collect of the objects, exit the maze
    maze.macgyver.move(maze.walls, maze.window)
    maze.macgyver.collecting_item(
        maze.window, maze.objects_to_collect, maze.my_font)
    maze.macgyver.meeting_warden(
        maze.warden, maze.window, maze.my_font_end_game)
    pygame.display.flip()
