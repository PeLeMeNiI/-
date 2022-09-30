from ctypes import sizeof
import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
class DrawShape():
    def draw(self,color = 'red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()


class Rect(DrawShape):
    def __init__(self,size,fill=False):
        self.size = size
        self.sides = 4
        self.angle = 90
        self.fill = fill

    def draw(self,x,y,color = False):
        if self.fill:
            t.color(color)
            t.begin_fill()
        t.penup()
        t.goto(0,0)
        t.goto(x,y)
        t.pendown()
        for f in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()


#rect = Rect(80,fill=True)
#rect.draw()
#rect = Rect(120,fill = True)
#rect.draw('purple')
#rect = Rect(40,fill = False)
#rect.draw()

class Triangle(DrawShape):
    def __init__(self,size,fill = False):
            self.size = size
            self.sides = 3
            self.angle = 120
            self.fill = fill

class Circle():
    def __init__(self,fill=True):
        self.fill = fill

    def draw(self,x,y,size,color):
        t.penup()
        t.goto(x,y)
        t.pendown()
        if self.fill:
            t.color(color)
            t.begin_fill()
        t.circle(size)

        if self.fill:
            t.end_fill()
#triangle = Triangle(40,fill = False)
#triangle.draw()

#triangle1 = Triangle(100,fill = True)
#triangle1.draw('purple')





#rectangle = Rect(40,fill = True)
#rectangle.draw(0,80,color='red')
#rectangle.draw(0,40,color='yellow')
#rectangle.draw(0,0,color='green')
teleshka = Rect(90,fill = True)
circle1 = Circle()
teleshka.draw(0,90,color = 'yellow')
teleshka.draw(90,90,color = 'yellow')
#t.pendown(x,y)
#t.goto(0, 0)
circle1.draw(0,0,60,color = 'purple')
circle1.draw(0,30,30,color = 'black')
circle1.draw(180,0,60,color = 'purple')
circle1.draw(180,30,30,color = 'black')
screen.mainloop()


