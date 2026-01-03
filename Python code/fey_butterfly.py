import turtle 
from turtle import *
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fey  Butterfly")
screen.setup(width=900, height=900)


pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.color("#4210b7")
pen.pensize(2)

screen.tracer(0, 0)
#to trace the drawing process

POINTS = 5000
UPDATE_EVERY = 8
DELAY = 0.002
MARGIN = 0.88

raw = []
min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")
#precompute points to determine bounding box

for k in range(POINTS):
    t = k /50
    #for scaling
    r = math.exp(math.cos(t)) - 2 * math.cos(4 * t) + (math.sin(t / 12)) ** 5
    #cartesian coordinates of the fey butterfly
    x0 = math.sin(t) * r
    y0 = math.cos(t) * r

    raw.append((x0, y0))
    
    if x0 < min_x:
        min_x = x0
    if x0 > max_x:
        max_x = x0
    if y0 < min_y:
        min_y = y0
    if y0 > max_y:
        max_y = y0

# Determine scaling factor to fit the window.
width = max_x - min_x
height = max_y - min_y

usable_width = screen.window_width() * MARGIN
usable_height = screen.window_height() * MARGIN

scale = min(usable_width/width, usable_height/height)

#centre alignment of the drawing
cx = (min_x + max_x) / 2
cy = (min_y + max_y) / 2

pen.penup()
x0, y0 = raw[0]
pen.goto((x0-cx) * scale, (y0 - cy) * scale)
pen.pendown()


# Draw the points
#in chunks so we can see the process
#small delay to see the drawing happening

for i, (x0, y0) in enumerate(raw, start=1):
    pen.goto((x0 - cx) * scale, (y0 - cy) * scale)


    if i % UPDATE_EVERY == 0:
        screen.update()
        time.sleep(DELAY)

screen.update()
turtle.done()

#here x0 and y0 are the computed coordinates of the butterfly points
#we scale and center them before drawing
#so the drawing fits nicely within the window
#cx and cy are the center offsets
#scale is the scaling factor to fit the drawing within the window
# (x0 - cx) * scale gives the final x coordinate to draw
# (y0 - cy) * scale gives the final y coordinate to draw
# i % UPDATE_EVERY == 0; means only adter 8 seconds show the drawing
