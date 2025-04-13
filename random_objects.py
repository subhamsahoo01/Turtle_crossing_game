import turtle as t
import random
class RandomObjects(t.Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen

        self.timmies=[]




    def create_objects(self):
        for i in range(0,random.randint(1,2)):

            timmy=t.Turtle()

            timmy.penup()
            timmy.speed(1)
            timmy.shape("square")
            timmy.shapesize(0.5,1.5)
            timmy.color("black")
            timmy.setposition(300,random.randint(-250,300))
            timmy.setheading(180)
            self.timmies.append(timmy)
            print("hello")


    def move_objects(self,a):
        for items in self.timmies:
            items.forward(a)
            # if items.xcor()<-280:
            #     items.setx(300)
            #     items.sety(random.randint(-300,300))

        # self.screen.ontimer(self.move_objects,100000)