"""
    This module intends to contain all elements needed in the program.

    Classes :
        This module doesn't contain any class

    Methods:
        This module doesn't contain any method

    Attributes:
        wall_picture:       gets access to the file containing a picture of a wall,
        macgyver_picture:   gets access to the file containing a picture of the hero,
        warden_picture:     gets access to the file containing a picture of the warden,
        objects_to_be_collected: gathers as a list the objects to be collected by the hero.
        All these files are located in a folder named 'ressource'

        Following constants are used throughout the script:
        SPRITE_SIZE:        as the maze is to be configured in 40x40 px sprites, its value as been 
                            set to 40, is used in Items and Maze modules
        CORRIDORS_COLOR:    is used in both modules Items and maze_game: the first to darken the corridors 
                            once an image has been moved, the latter to draw the maze.
        SCORE_BACKGROUND:   is used to draw a background to the score display, iot make it more visible,
                            in both modules Maze and Items.
        SCORE_COLOR:        is used to type the score in both modules Items and Maze


"""
maze_level = "maze_level_1"
wall_picture = 'ressource/wall.gif'
macgyver_picture = 'ressource/MacGyver.png'
warden_picture = 'ressource/Gardien.png'
objects_to_be_collected_pictures = [
    'ressource/seringue.png', 'ressource/ether.png', 'ressource/aiguille.png']

SPRITE_SIZE = 40
CORRIDORS_COLOR = (0, 0, 0)
SCORE_BACKGROUND = (255, 255, 255)
SCORE_COLOR = (125, 250, 125)
