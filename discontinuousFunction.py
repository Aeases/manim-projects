import scipy.stats as stat
from manim import *

class Thing(VMobject):
    def __init__(
        self, stroke_color=RED, fill_opacity=0.7, my_awesome_argument=42, **kwargs
    ):
        self.my_awesome_argument = my_awesome_argument
        super().__init__(stroke_color=stroke_color, fill_opacity=fill_opacity, **kwargs)

class TableScene(Scene):
  def construct(self):

    v = ValueTracker(4)

    ax2 = NumberPlane((-3, 3), (-4, 4))
    discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - v.get_value())
    correct = always_redraw(lambda: ax2.plot(
        discontinuous_function,
        discontinuities=[-2, 2],  # discontinuous points
        dt=0.1,  # left and right tolerance of discontinuity
        color=GREEN,
    ))
    self.play(Create(VGroup(ax2, correct)))
    self.wait()
    self.play(v.animate.set_value(6))