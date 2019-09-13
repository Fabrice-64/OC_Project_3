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
import Items
from Maze import Maze

pygame.init()

# Creates an instance to open a file containing the maze and build it up subsequently
maze = Maze()
maze.draw_maze(maze_level="maze_level_1")
maze.display_objects()


# Updates the maze_window
pygame.display.flip()

print("Coordonnées initiales : ({}, {})".format(maze.macgyver.x, maze.macgyver.y))
# Keeps the window open until intentionally closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                print((maze.macgyver.x, maze.macgyver.y))
                if (maze.macgyver.x, maze.macgyver.y + 40) not in maze.walls:
                    pygame.draw.rect(maze.window, (0, 0, 0), (maze.macgyver.x, maze.macgyver.y, 40, 40))
                    maze.macgyver.y += 40
                    maze.window.blit(maze.macgyver.picture, (maze.macgyver.x, maze.macgyver.y))
                else:
                    maze.window.blit(maze.macgyver.picture, (maze.macgyver.x, maze.macgyver.y))



        pygame.display.flip()

        if event.type == pygame.QUIT:
            running = False



