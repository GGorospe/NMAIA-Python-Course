# New Mexico Artificial Intelligence Academy
# Python for Students and Robots Course
# Author: George Gorospe, September 2025

# Turtle Racing Activity Instructions: 
# In this activity we'll create a two turtles and use a function race()
# to move each turtle forward by a random amount until one turtle reaches the finish line.

# Goal: Fill in the function declaration and complete the race code

# Often in python scripts, we start by importing libraries 
# IMPORTANT: the turtle import line (next) must be included at the top of all your turtle graphics scripts.
from turtle import *
import random
import math

# Use the turtle library to create a turtle we can draw with::
# Notice the caps! Capital T for Turtle() is a library, this is the Turtle Graphics code library we use in our script
# Small case turtle, is the actual turtle we'll command and move around our canvas.
turtle_1 = Turtle()

# Step 1. Draw the finish line - George's code, do not edit
turtle_1.penup()
turtle_1.forward(600)
turtle_1.right(90)
turtle_1.pendown()
turtle_1.pencolor("red")
turtle_1.forward(200)
turtle_1.backward(400)
turtle_1.forward(200)
turtle_1.left(90)
turtle_1.penup()
turtle_1.backward(600)

# Step 2. Race Setup
#    A. Moving turtle_1 back to the starting line - George's code, do not edit
turtle_1.penup()
turtle_1.backward(600)
turtle_1.left(90)
turtle_1.pendown()
turtle_1.pencolor("green")
turtle_1.forward(100)
turtle_1.right(90)
turtle_1.forward(100)

#   B. Creating turtle_2 and moving to the staring line - George's code, do not edit
turtle_2 = Turtle()
turtle_2.penup()
turtle_2.backward(600)
turtle_2.right(90)
turtle_2.pendown()
turtle_2.pencolor("blue")
turtle_2.forward(100)
turtle_2.left(90)
turtle_2.forward(100)

# Step 3. Create the race(arg) function.
#    1. Declare the race(turtle) function, in this function our argument is turtle,
#        this can represent either turtle when we call the function later.
#    2. Generate a random integer between 2 and 25, store the value in the "move" variable
#        While the turtles are racing, they'll move by this random amount.
#    3. Use the turtle.forward(move) function to command the turtle to move forward

# TODO: Use the instructions to fill in this function:
# In this function, the input argument will be the turtle you want to move, either turtle_1 or turtle_2
# TODO: 1. Declare the race(turtle) function, in this function our argument is turtle.
<<< replace this line with your declaration of the race(turtle) function, do not forget the ":"! >>
    # 1. Generate a random integer between 2 and 25, store the value in the "move" variable
    # Use the random library's randint(arg1,arg2) function to create a random number between 2, 25
    # for example, num = random.randin(1, 10) creates a random number and saves it to num
    # You need to create a random number and save it to move, your limits are 2 and 25.
    <<< replace this line with code to collect a random number and safe it to move >>> 
    
    # 2. Move the turtle forward by the random value you just created
    <<< replace this line with a call to the turtle.forward() function, use the move variable as your argument >>>
    
    
# Now that we've created the race(turtle) function, we'll use a while loop to make the turtles race.
# Step 4. Create a while loop
# In the race, we need to check the position of each turtle. This is done with the turtle.pos() function
# The turtle.pos() function returns two points, x and y, in a tuple (x, y),
# we need to collect these for each turtle.

# Your while loop will continue until either turtle_1_x or turtle_2_x values are less than 600
# TODO: get the position of each turtle on the global coordinate system.
# I have provided the pattern for turtle_1. repeat this pattern for turtle 2, changing 1 --> 2
(turtle_1_x, turtle_1_y) = turtle_1.pos() # We are only interested in the x position: turtle_1_x
<<< replace this line with the code to collect turtle_2 position, save to turtle_2_x and turtle_2_y >>>

# TODO: complete the TWO conditional statements for the while loop:
# Conditional statement #1: turtle_1_x is less than 600
# Conditional statement #2: turtle_2_x is less than 600
while <<< replace this with conditional statement 1 >>> and <<< replace this with conditional statement 2 >>>:
    
    # TODO: Call the race function on turtle_1, then call the race function on turtle_2
    # Call the race function for turtle_1 first
    <<< replace this line with a call to the race function, pass turtle_1 as the argument >>>
    
    # Call the race function for the turtle_2 next
    <<< replace this line with a call to the race function, pass turtle_2 as the argument >>>
    
    # Check the position of each turtle now that we've moved them forward
    # Since our turtles are moving forward, their x position is increasing
    # The x position of either turtle should eventually be greater than 600
    # This will cause the while loop to end
    (turtle_1_x, turtle_1_y) = turtle_1.pos()
    (turtle_2_x, turtle_2_y) = turtle_2.pos()
    
# Step 5. Use an if statement to print out which turtle won the race
# TODO: Write an "if statement" to declare a winner for the race.
# if turtle_1_x is greater than 600, then print: "Turtle_1 won the race!"
# elif turtle_2_x is greater than 600, then print: "Turtle_2 won the race!"
<<< reaplace this line wtih an if statement for turtle_1 >>>

<<< replace this line with an elif statement for turtle_2 >>>