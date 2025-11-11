# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Turtle Bubble Activity Instructions: 
#In this activity we'll create a fuction to place circles randomly within the canvas.
# Goal: Create a program that:
#1. Includes a draw_bubble() function that:
#    * Uses turtle.penup() to avoid lines between circles
#    * Moves the turtle to a random position on the canvas
#    * Uses turtle.pendown() to prepare the turtle to draw a circle
#    * Draws a circle of random diameter (between 20 and 100)

#2. Outside of your function you should use a while loop to repeatedly call the draw_bubble() function until number_circles, a user set variable is achieved.

#I have provided the basic structure for your code.
#Fill in the sections marked: ### Replace with your code

# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *
import random

# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle = Turtle()
# Set the turtle speed to fast
turtle.speed(10)

### Begin the Turtle Bubbles Activity #### STEP 1: define the draw_bubble() function
def draw_bubble():
  # A. Use turtle.penup() to avoid drawing a line between your bubbles
  <<< replace this line with the pen up command >>>

  # B. Generate random coordinates for the bubble, we need to randomly choose a x and y within the canvas
  # For this, we'll use the random.randint(arg1, arg2) function, 
  # Where arg1 is the lower limit and arg2 is the upper limit for the random number
  # Follow this pattern for x which has limits [-750, 750]
  x = random.randint(-750,750)
  # Copy the pattern from x, now for y, which has limits [-600, 600]
  <<< replace this line with the random int for the y axis >>>

  # C. use your random coordinates with the turtle.goto(x,y) function
  <<< replace this line with the goto function using the x and y coordinates from earlier >>>

  # D. Use turtle.pendown() to prepare the turtle to draw a circle
  <<< replace this line with the turtle pen down function >>>

  # E. Generate a random diameter for the bubble between 20 and 100 (LIMITS)
  # Again, we'll be using random.randint(arg1, arg2) to generate the diameter
  # I suggest something like: diameter = random.randint(lower_limit, higher_limit)
  <<< replace this line with the diameter generation command >>>

  # F. Draw the bubble with the turtle.circle(arg) function.
  # In this function arg is the diameter of the circle.
  <<< replace this line with the turtle circle function using the diameter from above >>>


# STEP 2: Setup your while loop
# Check your notes from the last lecture on while loops
# A. Create a variable like num_dots which will be part of our conditional statement
num_dots = 15 # you can make this more

# B. Create a variable index that will help us count how many circles we've drawn
# The initial value should be zero since we haven't drawn anything yet
index = 0

# C. Declare your while loop and form the conditional statement: while your index is less than the number of dots desired, the loop should continue
while index < num_dots:
  # 1. Increase your index by 1 (increment)
  index = index + 1

  # 2. Call your draw_bubble() function
  <<< replace this with a call to your draw_bubble function >>>