# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Turtle Loop Art Activity Instructions: 
# In this activity we'll really get comfortable using loops and see how powerful they can be.
# Goal: Create a program that uses at least three nested lops to create unique art. 

# Remember: a nested loop is one loop inside of another loop. 
# The indention or the spaces before your lines of code becomes very important here, since python uses those indentions to know what to include in the loop
# Example:
for changing_variable_1 in range(4): # First for loop
    # Code in the first loop has one indention
    print("changing_variable_1 has the value: " + str(changing_variable_1))
  
    # Next, we start for loop #2, this is the first nested loop (two indentions)
    for changing_variable_2 in range(10):
        # Code in the second loop has two indentions
        print("__ changing_variable_2 has the value: " + str(changing_variable_2))
    
        # Next, we start for loop #3, this is the second nested loop (three indentinos)
        for changing_variable_3 in range(4):
            # Code in the thrid loop has three indentions
            print("____ changing_vraiable_3 has the value: " + str(changing_variable_3))
      


# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *

# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle = Turtle()


# Here follow the pattern from above, starting with one loop.
# In your first loop instruct the turtle to move a little. Then start another for loop. Remember to change the name of your changing variable for each loop.