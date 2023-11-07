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
      y_range=[0, 4500, 1000],
      tips=False
    )
    years = {}
    for x in range(2015, 2023):
      years[x] = x
    ax.x_axis.add_labels(years)
    pIIP = list(map(lambda p: ax.c2p(float(p), float(IIP[p])), IIP))
    aIIP = list(map(lambda p: ax.c2p(float(p), float(AIA[p])), AIA))
    fIIP = list(map(lambda p: ax.c2p(float(p), float(FIA[p])), FIA))
    print(pIIP)
    self.add(ax)
    mapper = lambda m: list(map(lambda p: Dot(p), m))
    FIAGroup = VGroup(*mapper(fIIP))
    AIAGroup = VGroup(*mapper(aIIP))
    IIPGroup = VGroup(*mapper(pIIP))
    self.play(Write(AIAGroup.set_color(BLUE)), Write(FIAGroup.set_color(ORANGE)), )
    for i in range(1, 8):
      year = i + 2015
      brace = BraceBetweenPoints(aIIP[i], fIIP[i])
      AIAamount = lambda y: float(AIA[str(y)])
      FIAamount = lambda y: float(FIA[str(y)])
      print(FIA[str(year)])
      decimal = DecimalNumber((AIAamount(year) - FIAamount(year))).scale(0.65).next_to(brace, LEFT)
      
      self.play(Write(brace), Write(decimal))
      #self.play(TransformFromCopy(VGroup(FIAGroup[i], AIAGroup[i]), IIPGroup[i]))
      IIPDot = IIPGroup[i]
      if (AIAamount(year) - FIAamount(year) < AIAamount(year-1) - FIAamount(year-1)):
        IIPDot.set_color(RED_E)
      else:
        IIPDot.set_color(GREEN_C)
      self.play(ReplacementTransform(VGroup(brace, decimal), IIPDot))
      



         






