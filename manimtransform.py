from manim import *

yvaluesarray = [183.08, 181.11, 181.71, 198.04, 201.72, 191.76, 196.48, 221.59, 214.67, 216.62, 211.25, 225.74]
yvalue2 = [1,2,3,4,5,6,7,8]

class Transform(Scene):
    def construct(self):
        ax = Axes(
            axis_config={
                "include_numbers": True
            },
            tips=True,
            x_range=[1, 12],
            y_range=[180, 220, 5]
        )
        curve = ax.plot_line_graph(
        x_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        y_values=yvaluesarray
        )
        
        dotGroup = VGroup()
        for n, dp in enumerate(yvaluesarray):
            dot = Dot()
            dot.move_to(ax.c2p(n+1, dp))
            dotGroup.add(dot)

        self.play(Write(ax))
        self.play(Write(curve), run_time=3)
        self.add(dotGroup)
        self.play(dotGroup.animate.arrange(), run_time=3)
        self.wait(1)
        self.play(dotGroup.animate.arrange_in_grid(), FadeOut(curve))
        self.wait(1)
        square = Square()
        self.play(ReplacementTransform(dotGroup, square))
        self.play(square.animate.rotate(PI*3))
        circle = Circle()
        self.play(ReplacementTransform(square, circle))

class Transform1(Scene):
    def construct(self):
        ax = Axes(
            axis_config={
                "include_numbers": True
            },
            tips=True,
            x_range=[1, 12],
            y_range=[180, 220, 5]
        )
        curve = ax.plot_line_graph(
        x_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        y_values=yvaluesarray
        )
        
        dotGroup = VGroup()
        for n, dp in enumerate(yvaluesarray):
            dot = Dot()
            dot.move_to(ax.c2p(n+1, dp))
            dotGroup.add(dot)

        self.play(Write(ax))
        self.play(Write(curve), run_time=3)
        self.add(dotGroup)
        self.play(dotGroup.animate.arrange(), run_time=3)
        self.wait(1)
        self.play(dotGroup.animate.arrange_in_grid(), FadeOut(curve))
        self.wait(1)
        square = Square()
        self.play(ReplacementTransform(dotGroup, square))
        self.play(square.animate.rotate(PI*3))
        circle = Circle()
        self.play(ReplacementTransform(square, circle))


