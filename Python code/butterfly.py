#We use a parameter t (an angle), then define:

#r = e^cos(t) − 2cos(4t) − sin^5(t/12)

#Then convert to x,y like this:

#x = sin(t) * r
#y = cos(t) * r

#So as t runs around the circle, the radius stretches and squishes in a #very dramatic way. Result: butterfly.

import turtle
import math
import time


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Big Butterfly")
screen.setup(width=900, height=900)

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.color("#ff69b4")
pen.pensize(2)

POINTS = 5000
STEP_DIVISOR = 50
MARGIN = 0.88


#draw in chunks so we can see the process

UPDATE_EVERY = 8

#small delay to see the drawing happening
DELAY_SECONDS = 0.002



# We'll update the screen manually so you can see the process.
screen.tracer(0, 0)

# Precompute points  so we can auto-scale to fit the window.
raw_points = []
min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")
#all the points are computed first to determine the bounding box



for k in range(POINTS):
    t = k / STEP_DIVISOR
    r = math.exp(math.cos(t)) - 2 * math.cos(4 * t) - (math.sin(t / 12)) ** 5
    x0 = math.sin(t) * r
    y0 = math.cos(t) * r
    raw_points.append((x0, y0))
    if x0 < min_x:
        min_x = x0
    if x0 > max_x:
        max_x = x0
    if y0 < min_y:
        min_y = y0
    if y0 > max_y:
        max_y = y0


# Determine scaling factor to fit the window.
# We leave a margin around the edges.
#so the drawing is not right up against the window edge.

width = max_x - min_x
height = max_y - min_y

usable_w = screen.window_width() * MARGIN
usable_h = screen.window_height() * MARGIN

scale = min(usable_w / width, usable_h / height)

# Center the butterfly.
cx = (min_x + max_x) / 2
cy = (min_y + max_y) / 2

pen.penup()
first_x, first_y = raw_points[0]
pen.goto((first_x - cx) * scale, (first_y - cy) * scale)
pen.pendown()


#draw the butterfly in scaled coordinates as batched updates
for k, (x0, y0) in enumerate(raw_points, start=1):
    pen.goto((x0 - cx) * scale, (y0 - cy) * scale)
    if k % UPDATE_EVERY == 0:
        screen.update()
        time.sleep(DELAY_SECONDS)

screen.update()
turtle.done()
