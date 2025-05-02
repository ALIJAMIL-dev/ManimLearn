from manim import *

class WithVim(Scene):
    def construct(self):
        WVim = Text("This file is created and coded using vim in W11 Terminal(Vim for Windows)").scale(3)

        self.play(Create(WVim))
        self.wait(3)


