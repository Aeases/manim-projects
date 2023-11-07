import scipy.stats as stat
from manim import *
text_color = "#CECDC3"
import csv
IIP = dict()
FIA = dict()
AIA = dict()
ALL = [IIP, FIA, AIA]

""" def dataToPoint(data: dict, ax: Axes()):
  points = list()
  for x in data:
    print(data[x])
    point = ax.c2p(int(x), float(data[x]))
    points.append(point)
  return(points) """
def dataToPoint(data: dict):
  for x in data:
    print(data[x])
    point = ax.c2p(int(x), float(data[x]))
    points.append(point)
  return(points)


with open("IIPAustralia.csv") as IIPdata:
  print(IIPdata)
  d = csv.reader(IIPdata, delimiter=',')
  for dp in d:
    if int(dp[0]) >= 2015:
      IIP[dp[0]] = "".join(dp[1].split(","))
      AIA[dp[0]] = "".join(dp[2].split(","))
      FIA[dp[0]] = "".join(dp[3].split(","))
  

class InternationalInvestmentPosition(Scene):
  def construct(self):


    ax = Axes(
      x_range=[2014, 2022, 1],
      y_range=[0, 2000, 100],
      tips=False
    )
    years = {}
    for x in range(2015, 2023):
      years[x] = x
    ax.x_axis.add_labels(years)
    pIIP = list(map(lambda p: ax.c2p(float(p), float(IIP[p])), IIP))
    print(pIIP)
    self.add(ax)
    dot = Dot(pIIP[0])
    self.add(dot)
    for point in pIIP:
      self.play(Write(ArcBetweenPoints(pIIP[0], point)))
        






