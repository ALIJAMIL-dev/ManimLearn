from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)


        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.rotate(PI / 4)

        self.play(Create(circle))

        self.play()

        self.play(Transform(circle, square))

        self.play(FadeIn(square))

class TextMe(Scene):
    def construct(self):
        
        text = Text("Fuck you, I am a text!")
        self.play(Write(text))