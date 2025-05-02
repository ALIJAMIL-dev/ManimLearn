from manim import *

class Yoink(Scene):
    def construct(self):
        yoink_text = Text("Yoink").scale(5)

        yoink_text.set_color_by_gradient(RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)
        self.play(Write(yoink_text))   

        siuu = Text("Siuu").scale(5).next_to(yoink_text, DOWN, buff=0.5)
        siuu.set_color_by_gradient(RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)
        self.play(Write(siuu))