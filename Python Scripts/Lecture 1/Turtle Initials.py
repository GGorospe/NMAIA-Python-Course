# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Instructions:
# In this second exercise, we'll draw our initials in block letters. 

# As always, you should use the cards from the lecture as your reference!

# Turtle Initials Activity: 
# Use your turtle to draw your initials in block letters.
# In this activity, turtle.penup() and turtle.pendown() are important functions.
# As you move between letters, you'll want to "turtle.penup()" so that you don't draw a line connecting each initial.
# When you get to your starting point for your second initial, don't forget to "turtle.pendown()"

# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *

# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle = Turtle()

# EXAMPLE: George's Initials "GG"

# Turn around and prepare to draw the first "G" from the top
turtle.left(180)

# Drawing the first "G"
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(50)

# If we move to the next letter without lifting the pen, there will be a line joining each letter
turtle.penup()

# Moving without drawing a line
turtle.backward(50)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(150)

# Done moving to the start point for the next "G" time for pen down.
turtle.pendown()

# Turn around and prepare to draw the second "G" from the top
turtle.left(180)

# Drawing the first "G"
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(50)


