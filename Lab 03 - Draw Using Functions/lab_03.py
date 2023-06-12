# TIGER IN THE WILD DRAWING

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_ground():
    arcade.draw_lrtb_rectangle_filled(
        0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_BROWN)


def draw_tree():
    # Second Tree
    arcade.draw_rectangle_filled(750, 220, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(750, 260, 60, 80, arcade.csscolor.DARK_GREEN)

    arcade.draw_rectangle_filled(650, 250, 20, 150, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(650, 300, 60, 100, arcade.csscolor.DARK_GREEN)

    arcade.draw_rectangle_filled(550, 220, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(550, 260, 60, 80, arcade.csscolor.DARK_GREEN)


def draw_tiger(x, y):
    """DRAW A TIGER"""

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # BODY
    arcade.draw_rectangle_filled(x, y, 100, 50, arcade.color.ORANGE)
    # HEAD
    arcade.draw_rectangle_filled(
        x + 40, y + 30, 50, 50, arcade.color.ORANGE_PEEL)

    # FEET
    arcade.draw_rectangle_filled(x + 50, y - 20, 40, 20, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(x - 50, y - 20, 40, 20, arcade.color.ASH_GREY)

    # EYES
    arcade.draw_rectangle_filled(x + 50, y + 40, 10, 10, arcade.color.BLACK)


def on_draw(delta_time):
    arcade.start_render()
    draw_ground()
    draw_tree()
    draw_tiger(on_draw.tiger, 220)

    if on_draw.tiger == 800:
        on_draw.tiger = 0
    else:
        on_draw.tiger += 1

    print(on_draw.tiger)


on_draw.tiger = 100


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tiger in the Wild!")

    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.schedule(on_draw, 1/60)

    arcade.run()


# Call the main function to get the program started.
main()
