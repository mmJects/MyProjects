import turtle

screen = turtle.Screen()
lines_points = [(-295,100),(-295,-100),(-100,295),(100,295)]
angle_degress = [0,0,270,270]

class board:

    center_of_sectors = {1:(-197,197),2:(0,195),3:(197.5, 197.5),4:(-197.5, 0.0),5:(0.0, 0.0),6:(197.5, 0.0),7:(-197.5, -197.5),8:(0.0, -197.5),9:(197.5, -197.5)}
    def __init__(self,h,w):
        screen.setup(h,w)
        self.draw_lines()
    
    def draw_lines(self):
        for i in range(4):
            lines = turtle.Turtle()
            lines.penup()
            lines.goto(lines_points[i])
            lines.setheading(angle_degress[i])
            lines.pendown()
            lines.pensize(3)
            lines.forward(600)

    def draw_markings(self,sign,location):
        if sign == "X":
            x , y = self.center_of_sectors[location]
            self.cross(x,y)
        else:
            x , y = self.center_of_sectors[location]
            self.circle(x,y)


    def circle(self,x,y):
        o_shape = {"coor":(x,y-80),"radius":100}
        o = turtle.Turtle()
        o.penup()
        o.setpos(o_shape["coor"])
        o.pendown()
        o.pensize(2)
        o.hideturtle()
        o.circle(80)

    def cross(self,c_x,c_y):
        x_shpae = {"coor":[(c_x-60,c_y+60),(c_x+60,c_y+60)],"angles":[315,225],"len":170}
        for i in range(2):
            x = turtle.Turtle()
            x.penup()
            x.setpos(x_shpae["coor"][i])
            x.pendown()
            x.pensize(2)
            x.hideturtle()
            x.setheading(x_shpae["angles"][i])
            x.forward(x_shpae["len"])

ttt = board(600,600)
for i in range(1,10):
    if i % 2 == 0:
        ttt.draw_markings("X",i)
    else:
        ttt.draw_markings("O",i)

screen.exitonclick()