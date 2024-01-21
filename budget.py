from manim import *
import datetime

class LineGraphExample(Scene):
    def construct(self):
      CL_PAYOUT = 300
      today = datetime.date.today()
      # Events
      scholarship = datetime.date(2024,2,26) 
      DaysUntil_CLstarts = datetime.date(2024,2,26) - today
      DaysUntil_Scholarship = datetime.date(2024,2,26) - today



      xvalues = []
      yvaleus = []
      things = [ # ? things i want to buy
        3269,
        #1218,
      ]
      AcquiredThingIndex = [

      ]
      d = 0
      money = 1300
      while d < 365:

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
           money = money + 1500


        
        xvalues.append(d)
        yvaleus.append(money)
        d = d + 1
        print(money)


      plane = Axes(
          x_range = (0, 250, 20),
          y_range = (0, 6000, 500),
          y_length= 7,
          x_length = 11,
          y_axis_config={
            "include_numbers": True
          } 
      )
      plane.center()

      for i, xv in enumerate(xvalues):
        day = datetime.date.today() + datetime.timedelta(days=i)
        if day.day == 1:
          print(day)
          plane.x_axis.add_labels({i: f"{day.strftime('%B')}"})

      
      line_graph = plane.plot_line_graph(
          x_values = xvalues,
          y_values = yvaleus,
          line_color=GOLD_E,
          vertex_dot_style=dict(stroke_width=0, fill_opacity=0),
          stroke_width = 4,
      )
      self.add(plane)
      lineDots = line_graph["vertex_dots"]

      
      pointsOfChange = []
      for n, xv in enumerate(xvalues):
        d = xvalues
        m = yvaleus
        def dmp(idx):
          return plane.c2p(d[idx], m[idx])

        if n >= len(xvalues)-1:
          break
        if n == 0:
          pointsOfChange.append(dmp(n))
          continue


        if m[n] != m[n+1]:
          pointsOfChange.append(dmp(n))
        if m[n] != m[n-1]:
          pointsOfChange.append(dmp(n))




      Lines = VGroup()
      for idx, p in enumerate(pointsOfChange):
        if idx+1 >= len(pointsOfChange):
          break 
        l = Line(pointsOfChange[idx], pointsOfChange[idx+1])
        Lines.add(l)

       
      self.play(Write(Lines, rate_func=rate_functions.ease_in_expo))
        
      #self.add(plane, line_graph)
      print("finished")