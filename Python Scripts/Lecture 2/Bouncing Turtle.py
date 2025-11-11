# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Bouncing Turtle Activity Instructions: 
# In this activity we'll use if statements to manage the behavior of the turtle and let it make its own decisions.
# Goal: Create a program that checks the turtle's position and redirects the turlte if it is outside of the given boundary.

# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *
import random

# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle = Turtle()



# Drawing the boundary for the turtle, don't change this part of the code.
boundary_side = 300
turtle.write("(x=0, y=0)", align="center", font=("Arial", 16, "normal"))
turtle.penup()
turtle.forward(boundary_side/2)
turtle.write("Right Wall: x = 150", align="left", font=("Arial", 16, "normal"))
turtle.left(90)
turtle.pendown()
turtle.forward(boundary_side/2)
turtle.left(90)
turtle.forward(boundary_side)
turtle.write("Top Wall: y = 150", align="left", font=("Arial", 16, "normal"))
turtle.left(90)
turtle.forward(boundary_side/2)
turtle.write("Left Wall: x = -150", align="right", font=("Arial", 16, "normal"))
turtle.forward(boundary_side/2)
turtle.penup()
turtle.forward(30)
turtle.write("Bottom Wall: y = -150", align="left", font=("Arial", 16, "normal"))
turtle.backward(30)
turtle.pendown()
turtle.left(90)
turtle.forward(boundary_side)
turtle.left(90)
turtle.forward(boundary_side/2)
turtle.right(90)
turtle.penup()
turtle.backward(boundary_side/2)
turtle.pendown()


# ADD YOUR CODE BELOW:
# Create 4 "if" statements, one for each wall.
# Inside each if statement do the following:
# 1. print("Oh no! I hit the **** wall") change the *** for the wall you hit!
# 2. change the turtle heading using the turtle.setheading(arg) function
#   right wall: 225 + random.randint(-10,10)
#   left wall: 45 + random.randint(-10,10)
#   top wall: 315 + random.randint(-10,10)
#   bottom wall: 135 + random.radint(-10,10)
# 3. Add to the bounce: bounce = bounce + 1
# 4. Print the bounce number
total = 10
bounce = 0
turtle.setheading(random.randint(0,360))
while bounce < total: # A while loop, continues until the we reach a total of 10 bounces
    # Step 1: Move the turtle forward by one step, the turtle will continue to move forward
    forward(1)

    #Step 2: get the new location of the turtle
    # This function gets the x and y position of the turtle
    x, y = turtle.pos()
    
    # Step 3: 4 if statements - one for each wall
    # I've written the first if statement for you
    # Follow this pattern for the other three walls
    if x >= 150: # If the turtle hits the right wall x >=150
        print("Oh no! I hit the right wall!")
        turtle.setheading(225 + random.randint(-10, 10))
        bounce = bounce + 1
        print("Bounce Number " + str(bounce)) 

    # Write a if statement for the case where the turtle hits the left wall at when x is less than or equal to -150.
        # Follow the pattern from the right wall
        # Make sure to change the turtle heading using the turtle.setheading(arg) function
        #   left wall: 45 + random.randint(-10,10)


    # Write a if statement for the case where the turtle hits the top wall at when y is greater than or equal to 150.
        # Follow the pattern from the right wall
        # Make sure to change the turtle heading using the turtle.setheading(arg) function
        #   top wall: 315 + random.randint(-10,10)


    # Write a if statement for the case where the turtle hits the top wall at when y is greater than or equal to 150.
        # Follow the pattern from the right wall
        # Make sure to change the turtle heading using the turtle.setheading(arg) function
        #   bottom wall: 135 + random.randint(-10,10)
        
  