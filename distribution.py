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
    sigma = ValueTracker(0.14)
    normal = stat.norm(0.6, sigma.get_value())
    ax = Axes(
      x_range=[0, 1, 0.1],
      y_range=[0, 4, 0.2],
      tips=False,
      axis_config={"include_numbers": True, },
      x_axis_config={
        "numbers_with_elongated_ticks": [0.6],
        "include_numbers": False,
        },
    )

    #distPlot = DistributionPlot(
    #  x_range=[0, 1, 0.1],
    #  y_range=[0, 10, 1],
    #  tips=False,
    #  axis_config={"include_numbers": True, },
    #  x_axis_config={
    #    "numbers_with_elongated_ticks": [0.6],
    #    "include_numbers": False,
    #    },
    #    mean=0.6,
    #    sigma=0.14,
    #    #colour=BLUE_C
    #  )

    #plot = ax.plot(lambda x: normal.pdf(x) * 10**2 )
    #plot = ax.plot(lambda x: normaler(60, 14, x))
    classes = [[0.545, 0.19, RED_A], [0.642, 0.14, YELLOW_A], [0.632, 0.133, RED_D], [0.66, 0.136, GREEN_A]]
    #plot.add_updater(lambda m: m.become(ax.plot(lambda x: stat.norm(60, sigma.get_value()).pdf(x) * 10**2)))
    self.play(Write(ax))
    #self.play(Create(plot))
    #self.play(AnimationGroup(Create(distPlot.getPlot())))
    normalD(mean=0.6, sigma=0.14)
    rv = stat.norm(scale=0.14, loc=0.6)
    #f = ax.plot(lambda x: rv.cdf(x))
    fun = always_redraw(lambda: ax.plot(lambda x: rv.pdf(x)))
    #ax.plot
    xNumbers = ax.get_x_axis().get_number_mobject(60)
    self.play(Create(fun))

    #self.play(Write(xNumbers))
    #f = ax.plot(distPlot)
    #self.play(Create(f))
    #focaiDot = Dot(distPlot.runFunction(25))
    #self.play(Write(focaiDot))
    
    #anims = AnimationGroup
   
#    for i in classes:
#       tmp = DistributionPlot(ax, i[0], i[1], i[2])
#       self.play(LaggedStart(#
#         TransformFromCopy(distPlot.getPlot(), tmp.getPlot()),
#         lag_ratio=0,
#         run_time=1.35
#       ))

    
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


def normalD(mean, sigma):
  return lambda x: stat.norm(mean, sigma).pdf(x)

class DistributionPlot(Axes):
  def __init__(
      self,
      x_range: Sequence[float] | None = None,
      y_range: Sequence[float] | None = None,
      x_length: float | None = round(config.frame_width) - 2,
      y_length: float | None = round(config.frame_height) - 2,
      axis_config: dict | None = None,
      x_axis_config: dict | None = None,
      y_axis_config: dict | None = None,
      tips: bool = True,
      #axes: Axes,
      mean = 0.6,
      sigma = 0.14,

  ):
    self.function = lambda x: stat.norm(mean, sigma).pdf(x)
    self.mean = mean
    self.sigma = sigma
    #self.axes = axes
    Axes.__init__(x_range, y_range, x_length, y_length, axis_config, x_axis_config, y_axis_config, tips)

"""   def changePlot(self, mean, sigma, colour = WHITE):
    newPlot = self.axes.plot(lambda x: stat.norm(mean, sigma).pdf(x))
    self.mean = mean
    self.sigma = sigma
    self.colour = colour
    return self.plot.animate().become(newPlot).set_color(colour)

  def getPlot(self):
    return self.plot
  
  def runFunction(self, t):
    print(self.mean)
    print(self.sigma)
    return (self.axes.c2p(stat.norm(self.mean, self.sigma).pdf(t))) """





