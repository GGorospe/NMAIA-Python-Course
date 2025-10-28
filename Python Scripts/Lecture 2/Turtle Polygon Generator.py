# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Polygon Generator Activity Instructions: 
# In this activity we'll use two important tools: user input and for loops to create a polygon generation tool.
# Goal: Create a program that:
# 1. Asks the user how many sides the polygon should have.
# 2. Asks the user what length each side should have.
# 3. Uses this information within a for loop to draw the desired polygon

# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *

# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle = Turtle()

# USER INPUT EXAMPLE: FOLLOW THIS PATTERN IN STEP 1 & 2:
# Using the input function: the input function will prompt the user with a message, the part between the "".
# The value that the user inputs is stored in a variable, in this case, age.
age = input("What is your age? ") # The putput from this line, is assigned to the variable "age" but it is a string and should be cast to an integer.
age = int(age) # Very simple, but important line. This changes the string, example "15" to a integer, 15. These are two different things.
# NOTE: failure to cast the input to an int() will cause a "type error"

# STEP 1: Ask the user how many sides the polygon should have: Remember, we have to convert the input value to an integer or number, "5" isn't a number to the computer but 5 is!
num_sides = input("Don't forget to change this!!") # the data type from input here is a "string"
# 1a cast the value to an integer using int(arg) where arg is your variable, follow the pattern from above.

# STEP 2: Ask the user how what length each side should be:
length = input("Don't forget to change this too! ")
# 2a cast teh value to an integer using int(arg) where arg is your variable, follow the pattern from above.


# STEP 3: Using a for loop, draw the polygon:
# 3a - first calculate the inside angle at each corner. We do this by dividing 360 by the number of sides in the polygon
angle = ????

# 3b - setup the for loop to draw the polygon using three important variables: num_sides, length, and angle variabless.
# num_sides - the desired number of sides in the polygon will be the value we use for our for loop, it will cycle once for each side, moving forward then turning.
# length - the desired length of each side. This value will be used in turtle.forward(length)
# angle - the calculated interior angle between each side of the polygon. For the polygon to be complete, these angle should all sum to 360.
for changing_variable in range(???):
    # In each cycle of the for loop we would like to do two things: turn and move forward.
    # Below add two lines, one for turning and one for moving forward. Don't forget to indent properly!