import arcade
import random


WIDTH = 640
HEIGHT = 480


class Sprite:
    def __init__(self, x: int, y: int, x_speed: int=0, y_speed: int=0):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 25, arcade.color.BLACK)
    
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x > WIDTH or self.x < 0 or self.y > HEIGHT or self.y < 0:
            self.x_speed = -self.x_speed
            self.y_speed = -self.y_speed


window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

sprites = []

for i in range(10):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    dx = random.randrange(-5, 5)
    dy = random.randrange(-5, 5)

    s = Sprite(x, y, dx, dy)
    sprites.append(s)

def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    for sprite in sprites:
        sprite.update()


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    for sprite in sprites:
        sprite.draw()


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y, button, modifiers)


if __name__ == '__main__':
    setup()