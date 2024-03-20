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
LAYER_NAME_BACKGROUND_TOP = "Background_top"
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

        # Variable to hold our texture for our player
        self.player_texture = arcade.load_texture(f"{MAIN_PATH}/Assets/Character/Sprites/Idle/Idle1.png")

        # Separate variable that holds the player sprite
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128


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

       
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING)

        # Initiate New Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)       

        # Add Player Spritelist before "Foreground" layer. This will make the foreground

        # be drawn after the player, making it appear to be in front of the Player.
        # Setting before using scene.add_sprite allows us to define where the SpriteList
        # will be in the draw order. If we just use add_sprite, it will be appended to the
        # end of the order.

        self.scene.add_sprite_list_after("Player", LAYER_NAME_FOREGROUND)

        # Set up the player, specifically placing it at these coordinates.
        image_source = f"{MAIN_PATH}/Assets/Character/Sprites/Walk/ToWalk/ToWalk1.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X

        self.player_sprite.center_y = PLAYER_START_Y

        self.scene.add_sprite("Player", self.player_sprite)

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:

            arcade.set_background_color(self.tile_map.background_color)


        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=GRAVITY,
            ladders=self.scene[LAYER_NAME_LADDER],
            walls=self.scene[LAYER_NAME_PLATFORM],
        )

    def on_draw(self):
        """Renders the screen by drawing the game elements. Clears the screen with 'self.clear()' """

        self.clear()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 4)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered, 0.2)

    def update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # Update animations
        self.scene.update_animation(
            delta_time, [LAYER_NAME_POTION, LAYER_NAME_BACKGROUND]
        )

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_POTION]
        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:

            # Figure out how many points this coin is worth
            if "Points" not in coin.properties:
                print("Warning, collected a coin without a Points property.")
            else:
                points = int(coin.properties["Points"])
                self.score += points

            # Remove the coin
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)



        # Did the player fall off the map?

        if self.player_sprite.center_y < -100:

            self.player_sprite.center_x = PLAYER_START_X

            self.player_sprite.center_y = PLAYER_START_Y



            arcade.play_sound(self.game_over)



        # Did the player touch something they should not?

        if arcade.check_for_collision_with_list(

            self.player_sprite, self.scene[LAYER_NAME_DO_NOT_TOUCH]

        ):

            self.player_sprite.change_x = 0

            self.player_sprite.change_y = 0

            self.player_sprite.center_x = PLAYER_START_X

            self.player_sprite.center_y = PLAYER_START_Y



            arcade.play_sound(self.game_over)



        # See if the user got to the end of the level

        if self.player_sprite.center_x >= self.end_of_map:

            # Advance to the next level
            self.level += 1

            # Make sure to keep the score from this level when setting up the next level
            self.reset_score = False

            # Load the next level
            self.setup()

        # Position the camera
        self.center_camera_to_player()

def main():
    """Main function for the program"""
    window = MyGame()
    window.setup()
    arcade.run()

"""The program checks to see if the program is running from the main file, and if it is then it starts the program. """

if __name__ == "__main__":
    main()