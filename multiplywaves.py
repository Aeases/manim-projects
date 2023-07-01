from manim import *
import numpy as np


class multiplywaves(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-25, 25],
            y_range=[-10, 10, 2]
        )

        def func(x):
            return np.sin(x/2)





        plot = ax.plot(lambda x: np.sinc(x)/50 * np.sin(x*5))
        tex = VGroup(
            MathTex(r"\sin(x)"),
            MathTex(r"\sin(x^2)")
            )
        tex.scale(2)
        tex.to_edge(UP + RIGHT)
        self.add(ax)
        self.play(Write(plot))


        self.wait(5)