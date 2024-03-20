""" Main file """

import arcade
import os

""" Game window """

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Advanced Combat"
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))

#The scaling and size difference of the sprites and map tile sizes.
TILE_SCALING = 1
SPRITE_PIXEL_SIZE = 64
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Layer Names from our TileMap
LAYER_NAME_PLATFORM = "Platform"
LAYER_NAME_POTION = "Potion"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_BACKGROUND_TOP = "Background_top"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_DO_NOT_TOUCH = "Do_not_touch"
LAYER_NAME_LADDER = "Ladder"


""" The class 'Mygame' is the main application """


class MyGame(arcade.Window):

    #Set's up the game window, by calling the class 'MyGame'.
    def __init__(self):
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        #List for player and walls
        self.wall_list = None

        #Right edge of the map
        self.end_of_map = 0

        # Level
        self.level = 1


    def setup(self):
        """Sets up the game, loads and creates game resources and objects."""

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # MAIN_PATH PROBLEM
        """!!!"""
        map_name = f"{MAIN_PATH}\Maps\map_level_{self.level}.tmx"





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

        #DELETED , layer_options       
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING)

        # Initiate New Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)       

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:

            arcade.set_background_color(self.tile_map.background_color)


    def on_draw(self):
        """Renders the screen by drawing the game elements. Clears the screen with 'self.clear()' """

        self.clear()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()



    def update(self, delta_time):
        """Movement and game logic"""

        # Update animations
        self.scene.update_animation(
            delta_time, [LAYER_NAME_POTION, LAYER_NAME_BACKGROUND]
        )

        # Did the player fall off the map?


        # Did the player touch something they should not?

        # See if the user got to the end of the level

def main():
    """Main function for the program"""
    window = MyGame()
    window.setup()
    arcade.run()

"""The program checks to see if the program is running from the main file, and if it is then it starts the program. """

if __name__ == "__main__":
    main()