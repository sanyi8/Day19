from turtle import Turtle, Screen

screen = Screen()
# set screen size
screen.setup(500,400)
# popup to asks for bet
user_bet = screen.textinput("Make your bet", "which turtle will win the race? Pick a color: ")
print(user_bet)

# TODO - Create 6 turtles with the colors, and position them on the race line
color_list = ["yellow", "green", "red", "blue", "violet", "orange"]
y_start = -100  # starting y axle position


## create objects from class with different attributes
for color in color_list:    # loop through each color in color list
    t_object = Turtle(shape="turtle")
    t_object.penup()
    t_object.color(color)
    t_object.goto(x=-230, y=y_start)
    y_start += 30




screen.exitonclick()
# keep screen open
# screen.mainloop()