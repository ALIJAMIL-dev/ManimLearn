from manim import *

class TheCircle(Scene):
    def construct(self):
        circle = Circle()  # Create a circle
        #circle.set_fill(RED, opacity=0.5)
        self.play(Create(circle)) 