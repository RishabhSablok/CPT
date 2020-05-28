import arcade, random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Game"
SCALING = 2.0
class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLUE)
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = arcade.draw_rectangle_filled(400, 300, 100, 100, arcade.color.RED)

Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()