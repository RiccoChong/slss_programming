# Pumpkin Drawing
# Author: Ricco Chong
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

#left eye
carver.setposition(-50, 30)
carver.dot(30)

# Right eye
carver.setposition(50, 30)
carver.dot(30)

# mouth
carver.setpos(-40, -20)
carver.down()
carver.right(90)
carver.circle(40, 180)
carver.up()

turtle.done()