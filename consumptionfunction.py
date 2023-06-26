from manim import *

class ConsumptionFunction(Scene):
    def construct(self):
        a = ValueTracker(30)
        b = ValueTracker(0.8)
        def func(x):
            return a.get_value() + b.get_value()*x
        ax = Axes(
            axis_config={
                "include_numbers": False,
                "include_ticks": False,
            },
            tips=False,
            x_range=[0, 100, 10],
            y_range=[0, 100, 10]
        )
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
        
        ConsumptionFormula = MathTex(r'C_f={{a}}+{{b}}{{Y_d}}')
        self.play(Write(ConsumptionFormula))
        self.play(Create(VGroup(ax, a_label)))
        DecimalA = DecimalNumber(a.get_value()).to_corner(corner=DOWN + RIGHT).shift(LEFT*2, UP*2)
        DecimalB = DecimalNumber(b.get_value()).next_to(DecimalA, DOWN)
        MarginalPropC = MathTex("{{b}}=").next_to(DecimalB, LEFT)
        AutonSpending = MathTex("{{a}}=").next_to(DecimalA, LEFT) 
        self.play(
            TransformMatchingTex(ConsumptionFormula, VGroup(MarginalPropC, AutonSpending, x_axislabel), Write(y_axislabel)),
            LaggedStart(*[Write(DecimalA), Write(DecimalB)], lag_ratio=0.5)
            )
        DecimalB.add_updater(lambda s: s.set_value(b.get_value()))
        DecimalA.add_updater(lambda s: s.set_value(a.get_value()))
        self.play(Create(ConsumptionCurve))
        self.play(b.animate().set_value(0.2))
        self.play(a.animate().set_value(17))
        self.play(a.animate().set_value(50))
        ConsumptionDecimal = VGroup(MathTex("C_f="), DecimalA.copy(), MathTex("+"), DecimalB.copy(), MathTex(r"\times Y_d")).arrange()
        self.add(ConsumptionDecimal)
        ConsumptionComponofDecimal = VGroup(DecimalA, DecimalB)
        self.play(
                    DecimalA.animate().scale(0.001),
                    DecimalB.animate().scale(0.001)
                )
        self.wait(5)
        #self.play(ConsumptionCurve(lambda x: 20 + 0.8*x))

