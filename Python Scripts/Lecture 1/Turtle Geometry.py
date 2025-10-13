# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Instructions:
# In this exercise, we'll start with examples of turtle movement. 
# You should use the cards from the lecture as your reference!
# In the code, green lines with "#" are called comments, the code compiler ignores these when it runs the code.
# Run the code to see the turtle move.

# Turtle Geometry Activity: 
# Use your turtle to draw a square. If you're successful, draw a triangle next. 
# You can clear the canvas using the following line: (reference the cards) turtle.clear() turtle.reset()

# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *

# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle = Turtle()

# EXAMPLE: Move the turtle forward
turtle.forward(100)

# Example: Turn the turtle right by 90 degrees
turtle.right(90)

# Example: Move the turtle backwards
turtle.backward(100)

# Example: turn the turtle left by 45 degrees
turtle.left(45)
turtle.forward(100)

# You can use turtle.reset() to clear the screen and reset the turtle

# Write your code here to draw a box or a triangle.