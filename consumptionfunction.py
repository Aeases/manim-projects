from manim import *

Skip_Prev = True

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
        
        ConsumptionFormula = MathTex(r'C_f={{a}}+{{b}}{{Y_d}}').scale(1.5)
        self.play(Write(ConsumptionFormula))
        self.play(
                LaggedStart(
                    Create(VGroup(ax, a_label)),
                    ConsumptionFormula.animate().to_edge(UP, buff=0.5),
                    lag_ratio=0.6
                )
                  )
        a_brace = Brace(ConsumptionFormula[1], DOWN).set_color(YELLOW)
        b_brace = Brace(ConsumptionFormula[3], DOWN).set_color(RED)
        DecimalA = DecimalNumber(a.get_value()).next_to(a_brace, DOWN).set_color(YELLOW)
        DecimalB = DecimalNumber(b.get_value()).next_to(b_brace, DOWN).set_color(RED)
        self.play(
            LaggedStart(
                LaggedStart(
                    ConsumptionFormula[1].animate().set_color(YELLOW),
                    Create(a_brace),
                    Write(DecimalA),
                    lag_ratio=0.24
                ),
            
                LaggedStart(
                    ConsumptionFormula[3].animate().set_color(RED),
                    Create(b_brace),
                    Write(DecimalB),
                    lag_ratio=0.14
                ),
            )
        )
        #MarginalPropC = MathTex("{{b}}=").next_to(DecimalB, LEFT)
        #AutonSpending = MathTex("{{a}}=").next_to(DecimalA, LEFT) 
        #self.play(
        #    TransformMatchingTex(ConsumptionFormula, VGroup(MarginalPropC, AutonSpending, x_axislabel), Write(y_axislabel)),
        #    LaggedStart(*[Write(DecimalA), Write(DecimalB)], lag_ratio=0.5)
        #    )
        DecimalB.add_updater(lambda s: s.set_value(b.get_value()))
        DecimalA.add_updater(lambda s: s.set_value(a.get_value()))
        self.play(Create(ConsumptionCurve))
        self.play(b.animate().set_value(0.2))
        self.play(a.animate().set_value(17))
        self.play(a.animate().set_value(50))

        ConsumptionDecimal = VGroup(MathTex("C_f="), DecimalA.copy(), MathTex("+"), DecimalB.copy(), MathTex(r"\times Y_d")).arrange()
        ConsumptionDecimal.to_edge(UP, buff=0.5).scale(1.35)
        self.play(
            LaggedStart(
                Unwrite(a_brace),
                Unwrite(b_brace),
                LaggedStart(
                    Uncreate(ConsumptionFormula[3]),
                    Uncreate(ConsumptionFormula[1]),
                    TransformMatchingShapes(VGroup(DecimalA, DecimalB, ConsumptionFormula), ConsumptionDecimal)
                )
            )
            )
        self.play(b.animate(run_time=2, rate_func=there_and_back).set_value(0.80))
        self.play(Unwrite(ConsumptionCurve), 
                    Uncreate(VGroup(a_label)), 
                    ReplacementTransform(ConsumptionDecimal.clear_updaters(), ConsumptionFormula.to_edge(UP, buff=0.5)), 
                    rate_functions=rate_functions.bezier,
                  )
        self.play(Unwrite(VGroup(ConsumptionFormula[2], ConsumptionFormula[3], ConsumptionFormula[4])),
)
        self.next_section(skip_animations=Skip_Prev)
        #ConsumptionFormulae = MathTex('C_f=', 'a_c', '+', 'b', 'Y_d').to_edge(UP, buff=0.5).move_to(ConsumptionFormula).scale(1.25)
        #Cons_Auton_Brace = Brace(mobject=ConsumptionFormulae[1], direction=DOWN, color=YELLOW)
        #Cons_Auton_Text = Text("Autonomous \n Consumption", font_size=24, color=YELLOW).next_to(Cons_Auton_Brace, DOWN)
        #b.set_value(30)
        #a.set_value(0.8)

        Formulae = {
            "Consumption": ["{{C}} = {{a_c}}", "55-60%", YELLOW, 44],
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
        self.next_section(skip_animations=Skip_Prev)
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
        
        Aggregate_Formula = VGroup(
            MathTex(r"{{AE}} = ( {{a_I}}+{{a_g}}+{{X-M}}+{{a_c}} ) \times {{b}}{{Y_d}}"),
            MathTex(r"{{AE}} = ( {{a_{I+g} }}+{{X-M}}+{{a_c}} ) \times {{b}}{{Y_d}}"),

                                    )
        for Formula in Aggregate_Formula:
            Formula.set_color_by_tex("a_I", TEAL).set_color_by_tex("a_c", YELLOW).set_color_by_tex("a_g", PURPLE)
            Formula.to_edge(UP, buff=0.5)
            Formula.set_opacity_by_tex("+", 0.5).set_opacity_by_tex("-", 0.5).set_opacity_by_tex("X-M", 0.75)
            Formula.set_color_by_tex("a_{I+g}", BLUE_C).set_opacity_by_tex("a_{I+g", 1)
        self.play(
        LaggedStart(
            LaggedStart(
                Create(ConstantCurves[0]),
                Create(ConstantCurves[1]),
                Create(ConstantCurves[2]),
                lag_ratio=0.2,
            ),
            LaggedStart(
                AEComp_PREEquals[0].animate().next_to(ConstantCurves[0]).set_color(YELLOW),
                AEComp_PREEquals[1].animate().next_to(ConstantCurves[1]).set_color(TEAL),
                AEComp_PREEquals[2].animate().next_to(ConstantCurves[2]).set_color(PURPLE),
                lag_ratio=0.2,
            ),
            LaggedStart(
                #ReplacementTransform(, Aggregate_Formula), 
                FadeOut(AEComp_equals),
                TransformMatchingShapes(VGroup(AEComp_AFTERequals, x_axislabel.copy()), Aggregate_Formula[0], path_arc=np.sin(5**2)),
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
        self.next_section()
        #self.play(Aggregate_Formula.animate().shift(Aggregate_Formula.get_center()-Aggregate_Formula.get_part_by_tex("b").get_center()))
        Investment_TickL = ax.y_axis.get_tick(Formulae.get("Investment")[3]).set_color(TEAL)
        Investment_NumL = DecimalNumber(
                number=Formulae.get("Investment")[3],
                num_decimal_places=0
            ).next_to(ax.y_axis.n2p(Formulae.get("Investment")[3]), LEFT)
        Investment_NumL.set_color(TEAL)
        
        Government_TickL = ax.y_axis.get_tick(Formulae.get("Government")[3]).set_color(PURPLE)
        Government_NumL = DecimalNumber(
                number=Formulae.get("Government")[3],
                num_decimal_places=0
            ).next_to(ax.y_axis.n2p(Formulae.get("Government")[3]), LEFT)
        Government_NumL.set_color(PURPLE)   

        Consumption_TickL = ax.y_axis.get_tick(Formulae.get("Consumption")[3]).set_color(YELLOW)
        Consumption_NumL = DecimalNumber(
                number=Formulae.get("Consumption")[3],
                num_decimal_places=0
            ).next_to(ax.y_axis.n2p(Formulae.get("Consumption")[3]), LEFT)
        Consumption_NumL.set_color(YELLOW)    
        
        
        self.play(
            LaggedStart(
                Write(Investment_NumL),
                Create(Investment_TickL),
                Write(Government_TickL),
                Create(Government_NumL),
                Write(Consumption_NumL),
                Create(Consumption_TickL),
                lag_ratio=0.05
            )
        )
        self.play(
            TransformMatchingShapes(Aggregate_Formula[0], Aggregate_Formula[1]),
            Circumscribe(Aggregate_Formula[1].get_part_by_tex("a_{I+g}"), ),
                
            run_time=2
            )
        
        auton_i_g = MathTex("G+I").set_color(BLUE_D).next_to(ConstantCurves[2]).shift(LEFT/2+DOWN/2+UP/3-UP/4)
        self.play(
            AnimationGroup(
                Circumscribe(VGroup(Investment_NumL, Government_NumL)),
                AnimationGroup(
                    ReplacementTransform(VGroup(AEComp_PREEquals[1], AEComp_PREEquals[2]), auton_i_g),
                    ReplacementTransform(ConstantCurves[1], ConstantCurves[2]),
                ),
                AnimationGroup(
                    ReplacementTransform(Investment_NumL, Government_NumL),
                    ReplacementTransform(ConstantCurves[1], ConstantCurves[2]),
                ),
            run_time=2.2
            ),
            AnimationGroup(
                    Government_NumL.animate().set_color(BLUE_D),
                    ConstantCurves[2].animate().set_color(BLUE_D)
                ),
            lag_ratio=1.8
        )
        auton_inv_gov = ValueTracker(Formulae.get("Government")[3])
        row = Government_NumL.copy()
        Government_NumL.add_updater(lambda m:
            m.become(Government_NumL.set_value(auton_inv_gov.get_value()).next_to(ax.y_axis.n2p(auton_inv_gov.get_value()), LEFT))
            )
        
        ConstantCurves[2].add_updater(lambda m:
            m.become(
                ax.plot(lambda x: auton_inv_gov.get_value()+(x*0)).set_color(BLUE_D)
            )
        )

        auton_i_g.add_updater(lambda m: #could probably do this with always_redraw on the original as well
            m.next_to(ConstantCurves[2]).shift(LEFT/2+DOWN/2+UP/3-UP/4)
        )
        thisisleavinginlike2secs = MathTex("23+13=36")
        self.play(
            Succession(
                AnimationGroup(
                    auton_inv_gov.animate(rate_func=rush_into).set_value(36),
                    lag_ratio=0.3
                )
            ),
            Succession(
                Write(thisisleavinginlike2secs),
                FadeOut(thisisleavinginlike2secs)
            )


        )
        self.play(
                    Government_NumL.animate().set_color(BLUE_D),
                    Aggregate_Formula[1].animate().set_color_by_tex("a_{I+g}", BLUE_D),
                    lag_ratio=0.3
      )
        self.wait(6)
        
        



        
