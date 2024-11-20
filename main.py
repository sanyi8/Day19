from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)
#tim.shape("turtle")
screen = Screen()

def move_forwards():
    tim.forward(50)

def move_left():
    tim.left(30)

def move_right():
    tim.right(30)

def move_back():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# keyboard setup
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "s", fun = move_back)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "c", fun = clear)

screen.listen()
screen.bgcolor("azure3")
# onkey method listens for space and than call move_forward()
# screen.onkey(key="space", fun=move_forwards)

# keep screen open
screen.mainloop()