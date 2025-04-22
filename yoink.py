from manim import *

class Yoink(Scene):
    def construct(self):
        yoink_text = Text("Yoink").scale(5)

        yoink_text.set_color_by_gradient(RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)
        self.play(Write(yoink_text))   

        siuu = Text("Siuu").scale(5).next_to(yoink_text, DOWN, buff=0.5)
        siuu.set_color_by_gradient(RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)
        self.play(Write(siuu))


class FuckYou(Scene):
    def construct(self):
        Fuck_You = Text("Fuck You Apple").scale(2)

        Fuck_You.set_color_by_gradient(RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)
        self.play(Write(Fuck_You))

class SoStupid(Scene):
    def construct(self):
        URStupid = Text("You're So Stupid!")
        URStupid.set_color(YELLOW_A)

        self.play(Write(URStupid))

class Logo(Scene):
    def construct(self):
        suck= ImageMobject("download.png")

        suck.scale(1.2)

        suck.to_edge(RIGHT, buff=1)

        self.add(suck)