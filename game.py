import arcade

class Game_Window(arcade.Window):
    def __init__(self, height, width, title):
        super().__init__(height, width, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.WHITE)
    
    def on_draw(self):
        arcade.start_render()

Game_Window(500, 500, "Start")
arcade.run()