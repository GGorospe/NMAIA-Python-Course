# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Turtle Shape Library Activity Instructions: 
# In this activity we'll create a library of fuctions that draw unique shapes.
# This file contains several functions, right now they don't have any code inside of them.
# Your assignment is to put code inside that draws the shape listed in the function name.
# Pay special attention to the argument name, example: "side_length", you'll want to use that in your code.
# Goal: Fill in the function declarations wth code that draws the given shape

# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *
import random
import math

# TODO: Add code that draws a square where "side_length" is the input argument to the function.
def draw_square(side_length):
     <<< replace this line with code to draw a square of side_length >>>


# TODO: Add code that draws an equilateral triangle of "side_length" length on each side.
def draw_triangle(side_length):
    <<< replace this line with code to draw a triangle with sides of side_length >>>
    
# TODO: Study George's code on how to draw a circle. Do not change the code.
def draw_circle(diameter):
    """
    George's code
    Draws a circle with the given 'diameter' by drawing
    a 30-sided polygon.
    """
    NUM_SIDES = 30
    turn_angle = 360/NUM_SIDES
    # GEOMETRY LESSON:
    # 1. We need the total distance around the circle (the circumference).
    #    Formula: C = π * diameter
    circumference = math.pi * diameter
    
    # 2. We are drawing a polygon with NUM_SIDES (60) sides.
    #    To find the length of each side, we divide the total
    #    circumference by the number of sides.
    side_length = circumference / NUM_SIDES
    
    # 
    # 3. Now, we just loop 60 times:
    #    - Move forward by the small side_length
    #    - Turn by the small turn_angle
    
    for _ in range(NUM_SIDES):
        turtle.forward(side_length)
        turtle.right(turn_angle)

# TODO: Add code that will draw a polygon with any number of sides and side length as specified in the input arguments
def draw_polygon(num_sides, side_length):
    <<< replace this line with code to draw a polygon of num_sides with side_length >>>
    
# CHALLENGING:
# TODO: Add code to create a crescent moon or curved moon with the shape approximately like a banana.
# TIPS: Study the George's circle code from above. Start out by drawing 70% of a full circle.
def draw_crescent_moon(diameter):
    <<< replace this line with code to draw a crescent moon >>>

        
# TODO: add code to draw a star of any side length as specified by the "side_length" input argument 
def draw_star(side_length):
    <<< replace this line with code to draw a star >>>
    
    


# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle = Turtle()


# The following section calls each of the functions.
# You can use the "#" to comment out any of the functions you haven't completed.
turtle.backward(300)
draw_square(100)
turtle.forward(100)
draw_triangle(100)
turtle.forward(100)
draw_circle(100)

turtle.forward(100)
draw_polygon(5, 60)
turtle.forward(90)
draw_crescent_moon(100)
turtle.forward(100)
draw_star(150)