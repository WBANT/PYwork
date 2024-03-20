""" Main file """

import arcade

""" Game window """

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Advanced Combat"


""" The class 'Mygame' is the main application """

class MyGame(arcade.Window):

    """ Set's up the game window, by calling the class 'MyGame' """
    def __init__(self):

        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.BLACK)


    def setup(self):
        """Sets up the game, loads and creates game resources and objects."""

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