from manim import *

class plsHelp(Scene):
    def construct(self):
        myT = Text("I'm a beginner pls Help!")
        ci = Circle().scale(10)
        sq = Square().scale(3.7)
        ci.surround(myT)

        self.add(ci, myT)
        self.play(Transform(ci, sq))
        self.wait(2)