from manim import *
import datetime

CL_PAYOUT = 300
SCHOLARSHIP_PAYOUT = 1500
STARTING_MONEY = 1400

class LineGraphExample(Scene):
    def construct(self):
      today = datetime.date.today()
      # Events
      scholarship = datetime.date(2024,2,26) 
      DaysUntil_CLstarts = datetime.date(2024,2,26) - today
      DaysUntil_Scholarship = datetime.date(2024,2,26) - today

      things = [
        3269,
        1218,
      ]
      AcquiredThingIndex = [

      ]
      def NoLivingExpenses(d, money): 

        for thing in things:
          if money > thing and things.index(thing) == 0:
            money = money - thing
            things.pop(0)
            AcquiredThingIndex.append(d)

        # if (d % 7 == 0) and (d > 30) and len(things) == 0: # once i pay for petrol
        #   money = money - 120
        
        CLstart = d-DaysUntil_CLstarts.days # This is 0 when centrelink starts, increasing every day
        if (CLstart % 14 == 0) and (CLstart > 0):
          money = money + CL_PAYOUT
        
        if (DaysUntil_Scholarship.days-d == 0):
          money = money + SCHOLARSHIP_PAYOUT
        
        return money
      
      def LivingExpenses(d, money):
        m = NoLivingExpenses(d, money)
        if (d % 7 == 0) and len(things) == 0:
          m = m - 80
        return m
        
      def GenerateMoney(totalDays, money, func):
        # Func must take parameter "d", and 'money'
        d = 0
        xval = []
        yval = []
        while d < totalDays:
          money = func(d, money) 
          xval.append(d)
          yval.append(money)
          print(yval)
          d = d + 1
        return xval, yval
      days = 365 # d > 0
      xvalues, yvalues = GenerateMoney(days, STARTING_MONEY, NoLivingExpenses)
      

      
      plane = Axes(
          x_range = (0, 150, 20),
          y_range = (0, 6000, 1000),
          y_length= 6,
          x_length = 11,
          y_axis_config={
            "include_numbers": True
          },
          x_axis_config={
            "include_ticks": False
          }
      )
      plane.center()

      for i, xv in enumerate(xvalues): # Add Labels with the month
        day = datetime.date.today() + datetime.timedelta(days=i)
        if day.day == 1: # ? checking if first day of month
          plane.x_axis.add_labels({i: f"{day.strftime('%b')}"})
          

      
      # line_graph = plane.plot_line_graph(
      #     x_values = xvalues,
      #     y_values = yvalues,
      #     line_color=GOLD_E,
      #     vertex_dot_style=dict(stroke_width=0, fill_opacity=0),
      #     stroke_width = 4,
      # )
      self.play(Write(plane))
      #lineDots = line_graph["vertex_dots"]

      
      def getPointsAtChanges(xval, yval): # from x,y returns points before AND after a change in y
        points = []
        for n, yv in enumerate(yval):
          x = xval
          y = yval
          def dmp(idx):
            return plane.c2p(x[idx], y[idx])

          if n >= len(xvalues)-1:
            break
          if n == 0: # Append the first point
            points.append(dmp(n))
            continue

          
          if y[n] != y[n+1]: # Checks the next y will change
            points.append(dmp(n)) 
          if y[n] != y[n-1]: # Whether the previous y was a change
            points.append(dmp(n))
        return points

      def ConnectThePoints(points): # Connects a array of points to form a VGroup of Lines
        Lines = VGroup()
        for idx, p in enumerate(points):
          if idx+1 >= len(points):             
            break # Prevents list index not found error
          l = Line(points[idx], points[idx+1])   
          Lines.add(l)
        return Lines

      pointsOfChange = getPointsAtChanges(xvalues, yvalues) 

      def xyToLineChart(xvals, yvals): # Goes from x,y as days,money to a VGroup of Lines
        OnlyThePointsAtChanges: [Point] = getPointsAtChanges(xvals, yvals)
        Lines: VGroup = ConnectThePoints(OnlyThePointsAtChanges)
        return Lines
      
      LinesNoLivingExpenses = xyToLineChart(xvalues, yvalues)
      self.play(Write(LinesNoLivingExpenses, rate_func=rate_functions.ease_in_quad))
      Liv_x, Liv_y = GenerateMoney(days, STARTING_MONEY, LivingExpenses)
      
      # LinesLivingExpenses = xyToLineChart(Liv_x, Liv_y)
      # self.play(Write(LinesLivingExpenses))

       
      #self.add(plane, line_graph)
      print("finished")


