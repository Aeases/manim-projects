import scipy.stats as stat
from manim import *
from helpers import *

from typing import TYPE_CHECKING
from typing import Sequence
U_SHAPED_DISTRIBUTION = [0.3, 0.15, 0.05, 0.05, 0.15, 0.3]

def normaler(mean, sigma, x):
  dist = stat.norm(mean, sigma).pdf(x)
  return dist


class NormalDistribution(Scene):
  def construct(self):
    sigma = ValueTracker(14)
    normal = stat.norm(60, sigma.get_value())
    ax = Axes(
      x_range=[0, 100, 3],
      y_range=[0, 1, 0.5],
      tips=False,
      axis_config={"include_numbers": True, },
      x_axis_config={
        "numbers_with_elongated_ticks": [60],
        "include_numbers": False,
        },
    )
    #plot = ax.plot(lambda x: normal.pdf(x) * 10**2 )
    #plot = ax.plot(lambda x: normaler(60, 14, x))
    classes = [[54.5, 19, RED_A], [64.2, 14, YELLOW_A], [63.2, 13.3, RED_D], [66, 13.6, GREEN_A]]
    #plot.add_updater(lambda m: m.become(ax.plot(lambda x: stat.norm(60, sigma.get_value()).pdf(x) * 10**2)))
    self.play(Write(ax))
    #self.play(Create(plot))
    distPlot = DistributionPlot(ax, 60, 14, colour=BLUE_C)
    self.play(AnimationGroup(Create(distPlot.getPlot())))
    xNumbers = ax.get_x_axis().get_number_mobject(60)
    self.play(Write(xNumbers))
    #focaiDot = Dot(distPlot.runFunction(25))
    #self.play(Write(focaiDot))
    
    #anims = AnimationGroup
   
    for i in classes:
       tmp = DistributionPlot(ax, i[0], i[1], i[2])
       self.play(LaggedStart(
         TransformFromCopy(distPlot.getPlot(), tmp.getPlot()),
         lag_ratio=0,
         run_time=1.35
       ))
    #print(distPlot.runFunction(1))
"""     for i in classes:
      tempPlot = DistributionPlot(ax, i[0], i[1], i[2])
      self.play(TransformFromCopy(distPlot.getPlot(), tempPlot.getPlot()))
      self.play(Uncreate(tempPlot.getPlot())) """
    #self.play(distPlot.changePlot(58.5, 11, colour=RED_C))
    #self.play(distPlot.changePlot(60, 14))
    #f = normal.rvs(size=2)
    #print(f)
    #bars = ChartBars(ax, f)
    #self.play(plot.animate.apply_function_to_position(lambda x: x*4))
    #self.play(plot.become(ax.plot(lambda x: normaler(60, 4, x))))


class DistributionPlot(ParametricFunction):
  def __init__(
      self,
      axes: Axes,
      mean = 60,
      sigma = 14,
      colour = WHITE
  ):
    self.plot = axes.plot(lambda x: stat.norm(mean, sigma).pdf(x) * 10*2).set_color(colour)
    self.mean = mean
    self.sigma = sigma
    self.axes = axes

  def changePlot(self, mean, sigma, colour = WHITE):
    newPlot = self.axes.plot(lambda x: stat.norm(mean, sigma).pdf(x) * 10*2)
    self.mean = mean
    self.sigma = sigma
    self.colour = colour
    return self.plot.animate().become(newPlot).set_color(colour)

  def getPlot(self):
    return self.plot
  
  def runFunction(self, t):
    print(self.mean)
    print(self.sigma)
    return (self.axes.c2p(stat.norm(self.mean, self.sigma).pdf(t) * 10*2))





