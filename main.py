"""
Fait par Zhuo Han
Groupe 407

Dessin d'un voiture Dodge Challenger
"""


import arcade


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Full Screen Example"


class MyGame(arcade.Window):
    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "big screen")
        self.background_color = arcade.color.WHITE

    def draw_car(self):
        # CABIN
        windshield = ((415, 470), (885, 470), (825, 570), (475, 570))
        arcade.draw_polygon_filled(windshield, arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw_line(415, 460, 475, 570, arcade.color.MAROON, 10)
        arcade.draw_line(885, 460, 825, 570, arcade.color.MAROON, 10)
        arcade.draw_line(470, 570, 830, 570, arcade.color.MAROON, 5)

        # WHEELS AND MUD GUARDS
        arcade.draw.draw_lrbt_rectangle_filled(395, 475, 200, 370, arcade.color.BLACK)
        arcade.draw.draw_lrbt_rectangle_filled(825, 905, 200, 370, arcade.color.BLACK)
        arcade.draw.draw_lrbt_rectangle_filled(405, 895, 230, 300, arcade.color.CHARLESTON_GREEN)
        # CHASSIS
        arcade.draw_triangle_filled(400, 440, 410, 440, 410, 470, arcade.color.MAROON)
        arcade.draw_triangle_filled(900, 440, 890, 440, 890, 470, arcade.color.MAROON)
        arcade.draw.draw_lrbt_rectangle_filled(410, 890, 440, 470, arcade.color.MAROON)
        arcade.draw.draw_lrbt_rectangle_filled(400, 900, 300, 440, arcade.color.MAROON)
        arcade.draw.draw_lrbt_rectangle_filled(430, 870, 240, 300, arcade.color.MAROON)
        arcade.draw_triangle_filled(430, 300, 400, 300, 430, 240, arcade.color.MAROON)
        arcade.draw_triangle_filled(870, 300, 900, 300, 870, 240, arcade.color.MAROON)
        # VENT
        arcade.draw.draw_arc_filled(650, 470, 250, 50, arcade.color.MAROON, 0,
                                    180)
        arcade.draw.draw_arc_filled(650, 470, 200, 40, arcade.color.BLACK, 0,
                                    180)
        # GRILLS AND LIGHTS
        arcade.draw.draw_lrbt_rectangle_filled(410, 890, 370, 420, arcade.color.BLACK)
        arcade.draw.draw_lrbt_rectangle_filled(415, 520, 375, 415,
                                               arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw.draw_lrbt_rectangle_filled(780, 885, 375, 415,
                                               arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw.draw_lrbt_rectangle_filled(440, 860, 250, 290, arcade.color.BLACK)
        arcade.draw_circle_filled(445, 395, 17, arcade.color.GOLD)
        arcade.draw_circle_filled(490, 395, 14, arcade.color.GOLD)
        arcade.draw_circle_filled(445, 395, 12, arcade.color.LIGHT_GRAY)
        arcade.draw_circle_filled(490, 395, 9, arcade.color.LIGHT_GRAY)

        arcade.draw_circle_filled(855, 395, 17, arcade.color.GOLD)
        arcade.draw_circle_filled(810, 395, 14, arcade.color.GOLD)
        arcade.draw_circle_filled(855, 395, 12, arcade.color.LIGHT_GRAY)
        arcade.draw_circle_filled(810, 395, 9, arcade.color.LIGHT_GRAY)
        # MIRRORS
        arcade.draw_line(415, 460, 390, 480, arcade.color.MAROON, 7)
        arcade.draw_line(885, 460, 910, 480, arcade.color.MAROON, 7)
        arcade.draw_ellipse_filled(395, 480, 40, 25, arcade.color.MAROON)
        arcade.draw_ellipse_filled(905, 480, 40, 25, arcade.color.MAROON)
        # NUMBER PLATE
        arcade.draw_lrbt_rectangle_outline(600, 710, 300, 340, arcade.color.ULTRAMARINE,
                                           6)
        arcade.draw_lrbt_rectangle_filled(600, 710, 300, 340, arcade.color.LIGHT_GRAY)
        arcade.draw_text('HS   54C', 610, 310, arcade.color.RED, 20, 13, align='center')
        arcade.draw_point(647, 319, arcade.color.RED, 8)

    def on_draw(self):
        self.clear()

        self.draw_car()


def main():
    game = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
