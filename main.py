from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

Turtles = []
y_coord = -100

for n in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[n])
    tim.penup()
    tim.goto(x=-230, y=y_coord)
    Turtles.append(tim)
    y_coord += 40

screen.exitonclick()