""" Main file """

import arcade

""" Game window """

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Advanced Combat"


""" The class 'Mygame' is the main application """

class MyGame(arcade.Window):

    """ Set's up the game window, with the dimensions above height, width and title by calling the class 'MyGame' """
    def __init__(self):

        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)
