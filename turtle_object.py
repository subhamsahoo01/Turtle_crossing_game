import turtle as t

class TurtleObject(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, -280)
        self.shape("turtle")
        self.setheading(90)

    def move_turtle(self):
        self.forward(20)

