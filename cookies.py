# Cookies
# Author: Ricco Chong
# 21 November 2023

import turtle

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")

# Draw outline of cookie
baker_turtle.penup()
baker_turtle.goto(-5, -30)
baker_turtle.pendown()
baker_turtle.circle(30)
baker_turtle.penup()

# Add chips
baker_turtle.color("black")

# Center
baker_turtle.goto(0,0)
baker_turtle.stamp()

# Top-right chip, bottom-rigt, bottom-left, top-left
baker_turtle.goto(10,10)
baker_turtle.stamp()
baker_turtle.goto(10,-10)
baker_turtle.stamp()
baker_turtle.goto(-10,-10)
baker_turtle.stamp()
baker_turtle.goto(-10,10)
baker_turtle.stamp()

turtle.done()