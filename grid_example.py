import arcade

row_num = 15
column_num = 15

width = 30
height = 30

margin = 5

screen_width = (width + margin) * column_num + margin
screen_height = (height + margin) * row_num + margin
screen_title = "Grid"


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.grid = []
        for row in range(row_num):
            self.grid.append([])
            for column in range(column_num):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        for row in range(row_num):
            for column in range(column_num):
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                x = (margin + width) * column + margin + width // 2
                y = (margin + height) * row + margin + height // 2

                arcade.draw_rectangle_filled(x, y, width, height, color)

    def on_mouse_press(self, x, y, button, modifiers):

        column = int(x // (width + margin))
        row = int(y // (height + margin))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        if row < row_num and column < column_num:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


Game(screen_width, screen_height, screen_title)
arcade.run()