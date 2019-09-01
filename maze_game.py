"""
This is a maze game developed in the framework of OpenClassrooms education program as Python Developper

Purpose of the game: the hero must exit the maze. In order to to so, he has to collect 3 items;
a needle,
a PVC tube,
a flask of ether.
The 3 items are randomly scattered in the maze.
And then inject the warden the drug
If he fails, he dies.


Classes :
Hero,
Warden,
Items,
Walls,

Methods:

Attributes:

This program is based on Pygame.
"""
import pygame
import Items

pygame.init()

# Set up a window for the maze. Length and height are 15 characters, sprite size is 40
maze_window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("OpenClassrooms - MacGyver Maze Game")
pygame.display.update()


#Set up a maze based on a txt file named maze_level_1
class Maze():
    def draw_maze(maze_level):
        maze = open(maze_level, "r")
        f = maze.readlines()
        maze_window.fill((0, 0, 0))
        i = 0
        for j in range(len(f)):
            for i in range(len(f[j])):
                if f[j][i] == "X":
                    pygame.draw.rect(maze_window, (255, 0, 0), [(i * 40), (j*40), 40, 40])
                    pygame.display.flip()

warden  = Items.Warden()

#Creates an instance to open a file with the maze
maze = Maze.draw_maze(maze_level="maze_level_1")

# Keeps the window oppn until intentionally closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



