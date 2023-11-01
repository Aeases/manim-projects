import scipy.stats as stat
from manim import *
text_color = "#CECDC3"

class TableScene(MovingCameraScene):
  def construct(self):
    
    promTable = MathTable(
      table=[
        [r'', r'\text{Country A}', r'\text{Country B}'],
        [r'\text{Computers}', r'30', r'40'],
        [r'\text{Coal}', r'20', r'50']
      ]
    )
    promTable.set_color("#CECAC3")
    promTable.get_vertical_lines().set_stroke(color="#CECDC3", width=4)
    sq = Square()
    header = [Text("Inputs Table", font="Inter", color=text_color, weight=SEMIBOLD).to_edge(UP), Text("Opportunity Cost Table", font="Inter", color=text_color, weight=SEMIBOLD).to_edge(UP)]
    self.add(promTable, header[0])
    endCol = lambda x, y: promTable.get_cell((x,y))
    ColA = promTable.get_columns()[1]
    ColB = promTable.get_columns()[2]
    Col0 = promTable.get_columns()[0]
    self.camera.frame.save_state()
    ColB.save_state()
    self.play(LaggedStart(
      FadeOut(ColB, shift=RIGHT),
      self.camera.frame.animate().scale(0.7).move_to((endCol(2,2).get_left() + endCol(2,2).get_top() / 2)),
      lag_ratio=0.075
      ))
    #TexEquation = MathTex(r'\frac{', r'30', r'}{', r'20', r'}')
    #TexEquation.next_to(endCol(2,2))
    tempText = [MathTex("or").set_color(text_color), MathTex(r'\div')]
    tempEquation = [MathTex(r"\frac{30}{20}"), MathTex(r"\frac{3}{2}"), MathTex(r"\frac{3}{2}=1.5"), MathTex(r"\frac{30}{20}=1.5"), MathTex(r"30 \div 20"), MathTex(r"1.5")]
    ColumnA = VGroup(ColA[1], ColA[2])
    ColumnA.save_state()
    #self.camera.frame.save
    self.play(
        Create(tempText[0]),
        VGroup(ColA[1],tempText[0], ColA[2]).animate().arrange_submobjects(),
      )
    self.play(
              ReplacementTransform(tempText[0], tempText[1]),
    )
    self.wait(1)
    self.play(
      TransformMatchingShapes(VGroup(ColA[1], tempText[1], ColA[2]), tempEquation[0]),
      lag_ratio=0.4
    )
    self.wait(1)
    self.play(
      ReplacementTransform(tempEquation[0], tempEquation[1])
    )
    self.wait(1)
    self.play(
      TransformMatchingShapes(tempEquation[1], tempEquation[2])
    )
    self.play(
      ReplacementTransform(tempEquation[2], tempEquation[3])
    )
    self.play(Indicate(endCol(2,2), rate_func=there_and_back_with_pause, scale_factor=0.9))
    self.play(TransformMatchingShapes(tempEquation[3], ColumnA.restore()))

    ColumnA.save_state()
    
    l = MathTex(r"\frac{30}{20}")
    self.play(TransformMatchingShapes(VGroup(ColA[1], ColA[2]), l))
    self.play(TransformMatchingShapes(l, tempEquation[4]))
    self.play(FadeTransformPieces(tempEquation[4], tempEquation[5]))
    self.play(Flash(tempEquation[5], flash_radius=0.45), Indicate(endCol(2,2), rate_func=there_and_back, scale_factor=0.9))
    ColB.restore()
    
    self.play(Uncreate(VGroup(tempEquation[5], endCol(2,2))), self.camera.frame.animate().restore(), Write(ColB), Indicate(endCol(2,2), color=text_color, rate_func=exponential_decay, scale_factor=1))
    ColumnA.animate.restore()
    self.play(Write(ColumnA))
    self.wait(5)

    ColAEquations = [MathTex(r"\frac{30}{20}"), MathTex(r"1.5")]
    ColBEquations = [MathTex(r"\frac{40}{50}"), MathTex(r"0.8")]
    ColBEquations[0].move_to(ColB[1])
    ColBEquations[0].move_to(ColB[1])
    self.play(
      TransformMatchingShapes(VGroup(ColA[1], ColA[2]), ColAEquations[0]),
      TransformMatchingShapes(VGroup(ColB[1], ColB[2]), ColBEquations[0])
    )
    self.play(ReplacementTransform(ColAEquations[0], ColAEquations[1]), ShowPassingFlash(endCol(2,2), time_width=0.3))
    self.play(ReplacementTransform(ColBEquations[0], ColBEquations[1]), ShowPassingFlash(endCol(2,3), time_width=0.7, color=ORANGE))

    self.play(Unwrite(header[0]))
    self.play(Write(header[1], rate_func=rate_functions.slow_into))
    self.wait(2)
    # promTable.get_horizontal_lines()[0].animate().put_start_and_end_on(end=endCol(2,2).get_top() + endCol(2,2).get_right(), start=(endCol(2,1).get_left() + endCol(2,2).get_top()))
    
