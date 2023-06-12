import arcade

arcade.open_window(600, 600, "Drawing Example", resizable=False)

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()


arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.csscolor.GREEN)

# First Tree
arcade.draw_rectangle_filled(100, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 260, 30, arcade.csscolor.DARK_GREEN)

# Second Tree
arcade.draw_rectangle_filled(200, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 260, 60, 80, arcade.csscolor.DARK_GREEN)

# Third Tree
arcade.draw_rectangle_filled(300, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 230, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Fourth Tree
arcade.draw_rectangle_filled(400, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 300, 370, 220, 430,
                            220, arcade.csscolor.DARK_GREEN)

# Fifth Tree
arcade.draw_rectangle_filled(500, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 300),
                            (480, 260),
                            (470, 220),
                            (530, 220),
                            (520, 260)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Sun
arcade.draw_circle_filled(500, 500, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 500, 430, 500, arcade.color.YELLOW, 4)
arcade.draw_line(500, 500, 570, 500, arcade.color.YELLOW, 4)
arcade.draw_line(500, 500, 500, 430, arcade.color.YELLOW, 4)
arcade.draw_line(500, 500, 500, 570, arcade.color.YELLOW, 4)

# Diagonal rays
arcade.draw_line(500, 500, 550, 550, arcade.color.YELLOW, 8)
arcade.draw_line(500, 500, 450, 450, arcade.color.YELLOW, 8)
arcade.draw_line(500, 500, 450, 550, arcade.color.YELLOW, 8)
arcade.draw_line(500, 500, 550, 450, arcade.color.YELLOW, 8)

arcade.draw_text("Arbor Day - Plant a Tree!",
                 150, 130,
                 arcade.color.BLACK, 24)

arcade.finish_render()

arcade.run()
