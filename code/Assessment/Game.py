""" Main file """

import arcade
import os

""" Game window """

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Advanced Combat"
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))

#The scaling and size difference of the sprites and map tile sizes.
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
SPRITE_PIXEL_SIZE = 64
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# Player starting position
PLAYER_START_X = 128
PLAYER_START_Y = 450

# Layer Names from our TileMap
LAYER_NAME_PLATFORM = "Platform"
LAYER_NAME_POTION = "Potion"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_FOREGROUND_TOP = "Foreground_top"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_DO_NOT_TOUCH = "Do_not_touch"
LAYER_NAME_LADDER = "Ladder"

""" The class 'Mygame' is the main application """

class MyGame(arcade.Window):

    #Set's up the game window, by calling the class 'MyGame'.
    def __init__(self):
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        #List for player and walls
        self.wall_list = None
        self.player_list = None

        #Right edge of the map
        self.end_of_map = 0

        # Level
        self.level = 1

        arcade.set_background_color(arcade.csscolor.BLACK)


    def setup(self):
        """Sets up the game, loads and creates game resources and objects."""
        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Map name

        map_name = f"{MAIN_PATH}/map1_level_{self.level}.tmx"



        # Layer Specific Options for the Tilemap

        layer_options = {

            LAYER_NAME_PLATFORM: {

                "use_spatial_hash": True,

            },

            LAYER_NAME_POTION: {

                "use_spatial_hash": True,

            },

            LAYER_NAME_LADDER: {
                "use_spatial_hash": True,
            },

            LAYER_NAME_DO_NOT_TOUCH: {

                "use_spatial_hash": True,
            },
        }

        pass       


    def on_draw(self):
        """Renders the screen by drawing the game elements. Clears the screen with 'self.clear()' """

        self.clear()


def main():
    """Main function for the program"""
    window = MyGame()
    window.setup()
    arcade.run()

"""The program checks to see if the program is running from the main file, and if it is then it starts the program. """

if __name__ == "__main__":
    main()