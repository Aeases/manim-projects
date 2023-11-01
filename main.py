from manim import *
def endstartInterp(startValue, endValue):
    values = [startValue]
    print(endValue)
    while endValue > values[-1]:
        new_value = values[-1] + 1
        values.append(new_value)
    return values

def generate_geo_func(initial, terms):
    value_list = [initial]
        
    while terms >1:
        nextvalue = 0.8*value_list[-1]+10
        value_list.append(nextvalue)
        terms -= 1
    return (value_list)

def SeqContinuer(self: Scene, TEX_Sequence, table: MathTable, Tn_Target, sen: MathTex):
    tex = TEX_Sequence
    Current_Tn_Target = Tn_Target
    previous_values = table.get_rows()[1]
    print(table.get_rows())

    for n, val in enumerate(table.get_rows()[1]):
        TermValue = str(val).split("'")[1]
        TermTableReference = table.get_rows()[0]
        TermTableValueReference = table.get_rows()[1]
        TermPreviousValue = int(str(table.get_rows()[1][n-1]).split("'")[1])
        Term = n+1
        Current_Sequence = MathTex("{{T}}_{", f"{Term-1}", "+1}", r"=", r"(2 \times", f"{TermPreviousValue})", r"-20").move_to(TEX_Sequence)
        print(Term)
        if n == 0:
            continue
        if n == 2:
            newGSWhere = MathTex(r"\text{where}").next_to(TEX_Sequence, RIGHT)
            sen.set_x(500)
            self.play(ReplacementTransform(newGSWhere, TEX_Sequence))            
        if n > 2:
            self.play(Write(TEX_Sequence))
        self.play(
            TransformMatchingTex(TEX_Sequence, Current_Sequence.shift(DOWN/2).align_to(TEX_Sequence, LEFT)),
            lag_ratio=0.25,
            run_time=1.5
        )
        self.play(
            ReplacementTransform(Current_Sequence, MathTex(f"{TermValue}").move_to(previous_values[n])),
        )

    return(table)




from manim import *
import numpy as np
class ExampleTest(Scene):
    def construct(self):
        GeoSequenece = MathTex(r"{{T}}_{ {{n}} + 1}", r"=", r"2", r"T_n", r"-20").shift(LEFT, UP*3)
        GSWhere = MathTex(r"\text{ where }", r"T_1", r"=", r"5").next_to(GeoSequenece, RIGHT)
        

        t0 = MathTable(
            [["T_{{1}}", "T_{{2}}", "T_{{3}}", "T_{{4}}"],
            [5, -10, -40, -100]],
            include_outer_lines=True,
            v_buff=0.5
            )
        t0Entries = t0.get_entries()
        Sentence = VGroup(GeoSequenece, GSWhere)
        SentenceTemp = VGroup(GeoSequenece, GSWhere[0], GSWhere[2])
        self.add(Sentence)


        
        self.play(
                    FadeTransformPieces(GSWhere[1], t0Entries[0]),
                    FadeOut(GSWhere[2]),
                    Wait(0.3),
                    FadeTransformPieces(GSWhere[3], t0Entries[4])
                )
        self.play(Write(t0.get_rows()[0].remove(t0Entries[0])), Write(t0.get_vertical_lines()))
        newt0 = SeqContinuer(self, GeoSequenece, t0, 2, GSWhere)

        
        
        ax = Axes(
            axis_config={
                "include_numbers": True
            },
            tips=True,
            x_range=[1, 10],
            y_range=[0, 100, 10]
        ).shift(RIGHT*2)
        curve = ax.plot_line_graph(
                x_values=endstartInterp(ax.x_range[0], ax.x_range[1]),
                y_values=generate_geo_func(10, ax.x_range[-2])
                
        ) # can use VGROUP to combine
        self.play(Transform(newt0, t0.shift(UP)))
        self.play(Write(ax))
        self.next_section()
        self.play(Write(ax))





    # for e in previous_values:
    #     f = str(e).split("'")
    #     print(f"The Value is: {f}")
    #     self.play(
    #         TransformMatchingTex(TEX_Sequence, MathTex(f"T_{'{'}{Current_Tn_Target - 1}+1{'}'}"))
    #     )
    #     Current_Tn_Target += 1
