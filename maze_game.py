"""
This is a maze game developed in the framework of OpenClassrooms education program as Python Developper

Purpose of the game: the hero must exit the maze. In order to to so, he has to collect 3 items;
a needle,
a PVC tube,
a flask of ether.
The 3 items are randomly scattered in the maze.
And then the hero inject the warden the drug
If he fails, he dies.


Classes :
Items, which includes:
    MacGyver,
    Warden,
    Walls,
    Collected
Maze, which aims at drawing the maze

Methods:

Attributes:

This program is based on Python 3.7.4 and Pygame 1.9.3
"""
import pygame
from Maze import Maze

pygame.init()

# Set up a window for the maze. Length and height are 15 characters, sprite size is 40
maze_window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("OpenClassrooms - MacGyver Maze Game")
pygame.display.update()



# Creates an instance to open a file containing the maze and builds it up subsequently
built_maze = Maze()
built_maze.draw_maze(maze_window, maze_level="maze_level_1")
built_maze.display_objects(maze_window)

print((built_maze.walls[10].x, built_maze.walls[10].y))
# Updates the maze_window
pygame.display.flip()

# Keeps the window open until intentionally closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



