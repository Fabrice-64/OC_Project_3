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
Items, which includes:
    MacGyver,
    Warden,
    Walls,
    Collected

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

# Initializes both main characters of the maze
macgyver = Items.MacGyver()
warden = Items.Warden()


#Set up a maze based on a txt file named maze_level_1
class Maze():
    # Explores line by line the file containing the maze iot extract the different items (walls, characters, etc)
    def draw_maze(maze_level):
        maze = open(maze_level, "r")
        f = maze.readlines()
        maze_window.fill((0, 0, 0))
        i = 0
        for j in range(len(f)):
            for i in range(len(f[j])):
                # Definition of the 2 variables for the x and y of maze items. Value 40 is for the sprite size
                x = i * 40
                y = j * 40
                # Exploration of the file to get the different items of the maze
                if f[j][i] == "X":
                    # Draws the walls of the maze
                    pygame.draw.rect(maze_window, (255, 0, 0), [x, y, 40, 40])
                elif f[j][i] == "W":
                    maze_window.blit(warden.add_picture(), (x, y))
                elif f[j][i] == "M":
                    maze_window.blit(macgyver.add_picture(), (x, y))
                pygame.display.flip()
        return maze_window


#Creates an instance to open a file with the maze
maze = Maze.draw_maze(maze_level="maze_level_1")

# Updates the maze_window
pygame.display.flip()

# Keeps the window oppn until intentionally closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



