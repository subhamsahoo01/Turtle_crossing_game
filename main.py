import turtle as t

import random_objects
import turtle_object
import time
import random


screen=t.Screen()
screen.tracer(0)
screen.listen()
screen.setup(600,600)
Turtle_Object=turtle_object.TurtleObject()
Random_Objects=random_objects.RandomObjects(screen)
screen.onkey(Turtle_Object.move_turtle,"Up")
game_speed=5





game_is_on=True

while game_is_on:

    screen.update()
    time.sleep(0.1)


    Random_Objects.move_objects(game_speed)
    if random.randint(1, 6) == 1:
        Random_Objects.create_objects()
    for _ in Random_Objects.timmies:
        if Turtle_Object.distance(_)<20:
            game_is_on=False
    if Turtle_Object.ycor()>290:
        game_speed+=2
        Turtle_Object.setposition(0,-280)


        # break








screen.exitonclick()
