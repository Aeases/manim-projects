from manim import *
import numpy as np

class Testfunc(Scene):
    def construct(self):
        a = ValueTracker(30)
        b = ValueTracker(0.8)
        I = ValueTracker(30)
        def func(x):
            return a.get_value() + b.get_value()*x
        ax = Axes(
            axis_config={
                "include_numbers": False,
                "include_ticks": False,
            },
            tips=False,
            x_range=[0, 300, 10],
            y_range=[0, 300, 10]
        ).scale(0.85)
        #a_label = ax.y_axis.add_labels({a.get_value(): Tex('a')})
        a_label_point = ax.y_axis.n2p(a.get_value())
        a_label = MathTex("a").next_to(
            a_label_point, LEFT
            ).add_updater(
                lambda s: s.next_to(ax.y_axis.n2p(a.get_value()), LEFT))
        x_axislabel = ax.get_x_axis_label(r'Y_d')
        y_axislabel = ax.get_y_axis_label(r'AE')
        ConsumptionCurve = ax.plot(lambda x: func(x))
        ConsumptionCurve.add_updater(
            lambda m: m.become(
                ax.plot(
                    lambda x: func(x)
                )
            )
        )
        DegreeLine = ax.plot(lambda x: x, color=GREEN).set_opacity(75)
        self.play(Write(VGroup(ax)))
        self.play(Create(VGroup(ConsumptionCurve, a_label, x_axislabel, y_axislabel, DegreeLine)))
        ShiftedConsumptionCurve = ax.plot(lambda x: func(x)+I.get_value(), color=TEAL)
        Brace = BraceBetweenPoints(ax.y_axis.n2p(a.get_value()), ax.y_axis.n2p(a.get_value() + I.get_value()), direction=LEFT, color=TEAL)
        tex_Text = MathTex("\Delta I", font_size=48, color=TEAL).next_to(Brace, LEFT)
       
        resultx = (0 - a.get_value()) / (b.get_value()-1)

        print(resultx)
        #y=(a*(d-c)/(a-b))+c.

        resulty = (b.get_value() * (0-a.get_value())/(b.get_value()-1)) + a.get_value()
        print(resulty)
        self.play(TransformFromCopy(ConsumptionCurve, ShiftedConsumptionCurve))
        rot = Dot(ax.c2p(resultx, resulty))
        self.play(Write(rot))
        self.play(Write(tex_Text), Create(Brace), FadeOut(a_label))
        self.wait(2)



