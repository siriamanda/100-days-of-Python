from turtle import Turtle, Screen, colormode         # Import the classes from the turtle module
import random

siri = Turtle()
siri.shape("turtle")
# siri.color("red")

# Draw a square

# for i in range(4):
#    siri.right(90)
#    siri.forward(100)

# Draw a dotted line

# for i in range(15):
#    siri.forward(10)
#    siri.penup()
#    siri.forward(10)
#    siri.pendown()

# Draw a triangle, square, pentagon, hexagon etc.

colors = ["MediumBlue", "DeepSkyBlue", "RoyalBlue", "SkyBlue", "Orange", "Peru", "MediumSeaGreen",
          "CornflowerBlue", "MidnightBlue", "DarkBlue", "LightSkyBlue", "LightCoral", "Tomato"]
# full_circle = 360
# corners = [3, 4, 5, 6, 7, 8, 9]

# for i in range(7):
#    angle = full_circle / corners[i]
#    color = random.choice(colors)
#    siri.color(color)

#    for x in range(corners[i]-1):
#        siri.right(angle)
#        siri.forward(100)

#    siri.right(angle)
#    siri.penup()
#    siri.forward(100)
#    siri.pendown()

# Draw a random walk

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


# directions = [0, 90, 180, 270]
# siri.pensize(15)
# siri.speed("fastest")

# for i in range(300):
#    angle = random.choice(directions)
#    color = random_color()
#    siri.color(color)
#    siri.setheading(angle)
#    siri.forward(20)

# Draw a spirograph

siri.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        siri.color(random_color())
        siri.circle(80)
        siri.left(size_of_gap)

draw_spirograph(5)


# Draw a Hirst painting



screen = Screen()
screen.exitonclick()

