"""
Platformer Game
"""
import arcade

# Game window
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Platformer"

# Sprite scaling
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Movement speed of player; ppf
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.9
PLAYER_JUMP_SPEED = 20


class MyGame(arcade.Window):
    """
    Main application class.
    """
    
    def __init__(self):

        # accesses the class and setups the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # The scene
        self.scene = None

        # The player sprite
        self.player_sprite = None

        # The physics engine
        self.physics_engine = None


        # The camera

        self.camera = None


        arcade.set_background_color(arcade.csscolor.SILVER)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""


        # Sets up the camera

        self.camera = arcade.Camera(self.width, self.height)


        # Sets up the scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # Sets up player at the coordinates below
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 96
        self.scene.add_sprite("Player", self.player_sprite)

        

        # Create the ground and creates the wall sprite at a certain length horizontally
        for x in range(0, 2500, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # Puts crates at certain coordinates
        coordinate_list = [[512, 96], [256, 96], [768, 96], [996, 288], [], [], []]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"]
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()


        # Activate our Camera

        self.camera.use()


        # Draw our Scene
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0




    def center_camera_to_player(self):

        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)

        screen_center_y = self.player_sprite.center_y - (

            self.camera.viewport_height / 2

        )



        # Don't let camera travel past 0

        if screen_center_x < 0:

            screen_center_x = 0

        if screen_center_y < 0:

            screen_center_y = 0

        player_centered = screen_center_x, screen_center_y




        self.camera.move_to(player_centered)


    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()


        # Position the camera

        self.center_camera_to_player()



def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()