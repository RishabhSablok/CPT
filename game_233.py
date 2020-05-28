import arcade


WIDTH = 640
HEIGHT = 480

player_x = WIDTH/2
player_y = 20
ball_X = WIDTH/2
ball_y = HEIGHT/2
delta_x = 3.5
delta_y = 2.5
points = 0

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False
asds = True

def on_update(delta_time):
    global up_pressed, player_y, down_pressed, right_pressed, left_pressed, player_x , player_y, ball_X, ball_y, delta_x, delta_y, asds, points
    arcade.set_background_color(arcade.color.BLACK)
    ball_X += delta_x
    ball_y += delta_y
    if ball_X > WIDTH - 10 or ball_X < 10 and asds:
        delta_x *= -1
    if ball_y > HEIGHT - 10 and asds:
        delta_y *= -1
    elif ball_y < 10 or (player_x -15 < ball_X < player_x +30 and player_y -15 < ball_y < player_y +15) and asds:
        delta_y = 0
        delta_x = 0
        asds = False
    """    
    if (ball_y - player_y < 40) and (player_x-32 < ball_X < player_x + 32):
        asds = True"""
    
    if (player_x - 32 < ball_X < player_x + 32 and ball_y < player_y + 22) and asds:
        delta_y *= -1.09
        delta_x *= 1.05
    if player_x - 32 < ball_X < player_x + 32 and player_y - 22 < ball_y < player_y + 22 and asds:
        points += 1
    if up_pressed and player_y < HEIGHT-30 and False:
        player_y += 7.5
    if down_pressed and player_y > 30 and False:
        player_y = player_y - 7.5
    if right_pressed and player_x < WIDTH-30 and asds:
        player_x += 7.5
    if left_pressed and player_x > 30 and asds:
        player_x = player_x - 7.5



def on_draw():
    global player_x, player_y
    arcade.start_render()
    arcade.draw_rectangle_filled(player_x, player_y, 60, 30, arcade.color.BLUE)
    if not asds:
        arcade.draw_text("YOU LOST", WIDTH//2, HEIGHT//2, arcade.color.RED, 20, align="center")
        arcade.draw_text("You have " + str(points) + " points", 0, 440, arcade.color.WHITE, 20)

    else:
        arcade.draw_circle_filled(ball_X, ball_y, 10, arcade.color.RED)
        arcade.draw_text("You have " + str(points) + " points", 0, 440, arcade.color.WHITE, 20)
        


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.W or key == arcade.key.UP:
        up_pressed = True
    if key == arcade.key.S or key == arcade.key.DOWN:
        down_pressed = True
    if key == arcade.key.A or arcade.key.LEFT == key:
        left_pressed = True
    if key == arcade.key.D or arcade.key.RIGHT == key:
        right_pressed = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.W or key == arcade.key.UP:
        up_pressed = False
    if key == arcade.key.S or arcade.key.DOWN == key:
        down_pressed = False
    if key == arcade.key.A or arcade.key.LEFT == key:
        left_pressed = False
    if key == arcade.key.D or arcade.key.RIGHT == key:
        right_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game", resizable=False)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)
    
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
