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

rect = Rect(80,fill=True)
rect.draw()
rect = Rect(120,fill = True)
rect.draw('purple')
rect = Rect(40,fill = False)
rect.draw()

screen.mainloop()