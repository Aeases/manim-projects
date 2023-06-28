from manim import *

class TimeSereis(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 11],
            y_range=[0, 300, 30]
        )

        plot = ax.plot_line_graph(
            x_values=[0,1,2,3,4,5,6,7,8,9,10,11],
            y_values=[157, 67, 55, 96, 163, 69, 57, 100, 175, 79, 61, 108]
        )
        plot_seasoned = ax.plot_line_graph(
            x_values=[2,3,4,5,6,7,8,9],
            y_values=[94.5, 95.5, 96, 96.75, 98.75, 101.5, 104.75]
        )
        UnText = Text("Unseasoned").to_edge(UP)
        SeasonText = Text("Seasoned").to_edge(UP)
        self.play(
            Create(ax),
            Write(plot),
            Write(UnText)
        )
        self.play(
            ReplacementTransform(plot, plot_seasoned),
            TransformMatchingShapes(UnText, SeasonText)
        )
        self.wait(5)
