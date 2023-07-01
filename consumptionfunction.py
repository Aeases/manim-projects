from manim import *

Skip_Prev = False

class ConsumptionFunction(Scene):
    def construct(self):
        self.next_section(skip_animations=Skip_Prev)
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
        x_axislabel = ax.get_x_axis_label(r'Y_d').shift(DOWN/2.5)
        y_axislabel = ax.get_y_axis_label(r'AE')
        #ConsumptionCurve = ax.plot(lambda x: func(x)).set_color(ORANGE)
        ConsumptionCurve = always_redraw(lambda: ax.plot(lambda x: func(x)).set_color(ORANGE))
#        ConsumptionCurve.add_updater(
#            lambda m: m.become(
#                ax.plot(
#                    lambda x: func(x)
#                )
#            )
#        )
        
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
        self.play(TransformMatchingShapes(VGroup(DecimalA, DecimalB), ConsumptionDecimal), Unwrite(VGroup(MarginalPropC, AutonSpending)))
        self.play(b.animate(run_time=2, rate_func=there_and_back).set_value(0.80))
        self.play(Unwrite(ConsumptionCurve), 
                  Uncreate(VGroup(a_label)), 
                  ReplacementTransform(ConsumptionDecimal.clear_updaters(), ConsumptionFormula.to_edge(UP, buff=0.5).scale(1.5)), rate_functions=rate_functions.bezier)
        self.next_section(skip_animations=Skip_Prev)
        #ConsumptionFormulae = MathTex('C_f=', 'a_c', '+', 'b', 'Y_d').to_edge(UP, buff=0.5).move_to(ConsumptionFormula).scale(1.25)
        #Cons_Auton_Brace = Brace(mobject=ConsumptionFormulae[1], direction=DOWN, color=YELLOW)
        #Cons_Auton_Text = Text("Autonomous \n Consumption", font_size=24, color=YELLOW).next_to(Cons_Auton_Brace, DOWN)
        #b.set_value(30)
        #a.set_value(0.8)

        Formulae = {
            "Consumption": ["{{C}} = {{a_c}}", "55-60%", YELLOW, 60],
            "Investment": ["{{I}} = {{a_I}}", "16-23%", TEAL, 13],
            "Government": ["{{G}} = {{a_g}}", "23%", PURPLE, 23],
        }
        animations = []
        Prev_Formulae = VGroup(
            ConsumptionFormula
        )
        for idx, Formula in enumerate(Formulae.values()):
            PreviousFormula = Prev_Formulae[idx]
            IsFirstOne = PreviousFormula == ConsumptionFormula
            tex = MathTex(Formula[0]).next_to(PreviousFormula, DOWN)
            if (IsFirstOne):
                tex.move_to(ConsumptionFormula)
                print("fuck")

            
            color = Formula[2]
            tex.scale(1.5)
            tex[2].set_color(color)

            tex_Brace = Brace(mobject=tex[2], direction=DOWN, color=color)
            tex_Text = Text(f"Autonomous {list(Formulae.keys())[idx]} Expenditure", font_size=24, color=color).next_to(tex_Brace, DOWN)
            plotteddata = ax.plot(lambda x: Formula[3]+(x*0)).set_color(color)
            if IsFirstOne:

                animations.append(
                    
                    LaggedStart(
                    #FadeOut(ConsumptionFormula, run_time=0),
                    TransformMatchingShapes(ConsumptionFormula, tex),
                    #tex.animate().set_opacity(100)
                    lag_ratio=0
                ))
                
            else: animations.append(
                LaggedStart(
                    TransformFromCopy(PreviousFormula, tex),
                    LaggedStart(
                    PreviousFormula.animate().to_edge(LEFT + RIGHT, buff=0),
                    PreviousFormula.animate().scale(0.75)
                    ),

                    lag_ratio=0.2
                ))
                
            animations.append(LaggedStart(
                FadeIn(tex_Brace),
                tex[2].animate().set_color(color),
                Write(tex_Text),
                Create(plotteddata),
                lag_ratio=0.1
            ))
            animations.append(LaggedStart(
                FadeOut(tex_Brace),
                FadeOut(tex_Text),
                Unwrite(plotteddata),
            ))
                

            #self.remove(ConsumptionDecimal, ConsumptionFormula)

            print(f"I am {Formula[0]}, I believe in: {PreviousFormula}")
            Prev_Formulae.add(tex)
        
        
        animations.append(
            Prev_Formulae[-1].animate().scale(0.75)
        )
        for animation in animations:
            self.wait(stop_condition=(self.play(animation, lag_ratio=0.5)))
        
        Prev_Formulae.remove(ConsumptionFormula)
        self.next_section()
        ConstantCurves = []
        for Formula in Formulae.values():
            ConstantCurves.append(ax.plot(lambda x: Formula[3]+(x*0)).set_color(Formula[2]))
        
        AEComp_PREEquals=VGroup()
        AEComp_AFTERequals = VGroup()
        AEComp_equals = VGroup()
        AEComp_PREequalsTarget = VGroup()

        for Formula in Prev_Formulae:
            AEComp_PREEquals.add(Formula[0:1])
            AEComp_PREequalsTarget.add(Formula[0])
            AEComp_AFTERequals.add(Formula[2])
            AEComp_equals.add(Formula[1])
        
        Aggregate_Formula = MathTex(r"{{AE}} = ( {{a_I}}+{{a_g}}+{{X-M}}+{{a_c}} ) \times {{b}}{{Y_d}}")
        Aggregate_Formula.set_color_by_tex("a_I", TEAL).set_color_by_tex("a_c", YELLOW).set_color_by_tex("a_g", PURPLE)
        Aggregate_Formula.to_edge(UP, buff=0.5)
        Aggregate_Formula.set_opacity_by_tex("+", 0.5).set_opacity_by_tex("-", 0.5).set_opacity_by_tex("X-M", 0.75)
        self.play(
        LaggedStart(
            LaggedStart(
                Create(ConstantCurves[0]),
                Create(ConstantCurves[1]),
                Create(ConstantCurves[2]),
                lag_ratio=0.2,
            ),
            LaggedStart(
                AEComp_PREEquals[0].animate.next_to(ConstantCurves[0]).set_color(YELLOW),
                AEComp_PREEquals[1].animate().next_to(ConstantCurves[1]).set_color(TEAL),
                AEComp_PREEquals[2].animate().next_to(ConstantCurves[2]).set_color(PURPLE),
                lag_ratio=0.2,
            ),
            LaggedStart(
                #ReplacementTransform(, Aggregate_Formula), 
                FadeOut(AEComp_equals),
                TransformMatchingShapes(VGroup(AEComp_AFTERequals, x_axislabel.copy()), Aggregate_Formula, path_arc=np.sin(5**2)),
                lag_ratio=0.4,
                run_time=2
            ),
            lag_ratio=0.45
        ))
#        self.play(
#                        LaggedStart(
#                Transform(AEComp_PREEquals[0], AEComp_PREequalsTarget[0]),
#                Transform(AEComp_PREEquals[1], AEComp_PREequalsTarget[1]),
#                Transform(AEComp_PREEquals[2], AEComp_PREequalsTarget[2]),
#                lag_ratio=0.2,
#            ),
#        )


        self.wait(1)
            
