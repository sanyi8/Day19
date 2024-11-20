import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# set screen size
screen.setup(500,400)
# popup to asks for bet
user_bet = screen.textinput("Make your bet", "which turtle will win the race? Yellow, Orange, Red, Green, Blue, purple, Orange? Pick a color: ").lower()
print(user_bet)
y_start = -100  # starting y axle position

color_list = ["yellow", "green", "red", "blue", "purple", "orange"]
all_turtles = []

## create objects from class with different attributes
for color in color_list:    # loop through each color in color list
    t_object = Turtle(shape="turtle")
    t_object.penup()
    t_object.color(color)
    t_object.goto(x=-230, y=y_start)
    y_start += 30
    all_turtles.append(t_object)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # random_distance = random.randint(0,10)
        if turtle.xcor() > 230: # screen should be 250-half of turtle size: 20
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
# keep screen open
# screen.mainloop()