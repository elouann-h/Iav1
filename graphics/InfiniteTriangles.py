from turtle import *
from random import *
from time import *

penup()
speed(0)
hideturtle()
# the coordinates (x,y) of three points that are equidistant from each other
p1 = (-200, -100)
p2 = (0, 200)
p3 = (200, -100)

dot_size = 2
dot_color = "black"
dots = 25000

setpos(p1)
dot(3, "red")
setpos(p2)
dot(3, "red")
setpos(p3)
dot(3, "red")


# generates a point included in the triangle
def generate_point():
    # generate a random number between 0 and 1
    r1 = random()
    r2 = random()
    # if the sum of the two numbers is greater than 1, we subtract 1
    if r1 + r2 > 1:
        r1 = 1 - r1
        r2 = 1 - r2
    # the coordinates of the point are calculated
    x = r1 * p1[0] + r2 * p2[0] + (1 - r1 - r2) * p3[0]
    y = r1 * p1[1] + r2 * p2[1] + (1 - r1 - r2) * p3[1]
    return x, y


def middle_of_points(a, b):
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    return x, y


percent = dots / 100
last_time = time()
last_amount_of_dots = 0


def time_left(current):
    global last_time, last_amount_of_dots
    current_time = time()
    time_per_dot = (current_time - last_time) / (current - last_amount_of_dots)
    last_dot_speed = (current - last_amount_of_dots) / (current_time - last_time)
    time_left_ = (dots - current) * time_per_dot
    last_time = current_time
    last_amount_of_dots = current
    print("Dots placed: {} ({}%), Time left: {} seconds".format(current, round(current / percent), round(time_left_)))
    print("Last speed: {} dots per second".format(round(last_dot_speed)), end="\n\n")


last_dot = generate_point()
for i in range(1, dots + 1):
    if (i / percent) % 5 == 0:
        time_left(i)
    setpos(last_dot)
    dot(dot_size, dot_color)
    origin = eval("p{}".format(randint(1, 3)))
    last_dot = middle_of_points(last_dot, origin)

while True:
    continue