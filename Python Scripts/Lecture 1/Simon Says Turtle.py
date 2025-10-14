# Simon Says, Turtle Does Game
# This game was created for the NMAIA's "Python for Students & Robots" course
# About: Students are asked to recreate a random path with their turtle.

import turtle
import random
import time

# --- 1. Game Setup ---
# Create the screen and two turtles: a leader and a player.
screen = turtle.Screen()
screen.title("Simon Says, Turtle Does Game!")

# Create Simon, or the "leader" turtle that will draw the path.
leader = turtle.Turtle()
leader.shape("turtle")
leader.color("blue")
leader.pensize(3)
leader.speed("slow") # Slow down the leader so the path is easy to see.

# Create the "player" turtle that the user will control.
player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.pensize(3)
player.penup() # Lift the pen initially
player.goto(0, 0) # Make sure it starts at the same spot
player.pendown()
player.hideturtle() # Hide the player turtle until it's their turn.

# --- 2. Print Instructions ---
print("--- Welcome to Simon Says, Turtle Does Game! ---")
print("A blue turtle will draw a random path.")
print("Your job is to remember the path and guide the red turtle using commands.")
print("---------------------------------------")

# --- 3. Get the Number of Moves ---
# Ask the user how many moves the leader turtle should make.
# We use a try-except block to handle cases where the user types text instead of a number.
try:
    num_moves_str = input("How many moves should the leader make? (e.g., 5): ")
    num_moves = int(num_moves_str)
except ValueError:
    print("That's not a valid number. We'll use 5 moves.")
    num_moves = 5

# --- 4. Leader's Turn: Generate and Draw the Path ---
# This is where the leader turtle moves randomly.

# Define the possible moves. We use strings to represent them.
possible_moves = ["left", "right"]
move_sequence = [] # This empty list will store the random path.

print("\nWatch the blue turtle carefully!")
time.sleep(1) # Pause for a moment before starting.

for i in range(num_moves):
    # Selecting moves at random, always one move forward, then one turn.
    if i % 2 != 0:
        move = "forward"
    else:
        # Randomly choose one of the moves from our list.
        move = random.choice(possible_moves)
        
    # Add the chosen move to our sequence list to "remember" it.
    move_sequence.append(move)
    if move == "forward":
        leader.forward(50)
    if move == "left":
        leader.left(90)
    elif move == "right":
        leader.right(90)

# The leader's path is done. Hide the leader to avoid confusion.
leader.hideturtle()
player.showturtle() # Now it's the player's turn, so show their turtle.

# --- 5. Player's Turn: Follow the Path ---
# Now, we challenge the player to enter the same sequence of moves.
print("\n--- Your Turn! ---")
input("Press Enter to continue...")
leader.clear()
print("Enter the commands to make the red turtle follow the same path.")
print("Commands: 1 = Forward, 2 = Left, 3 = Right")
print("--------------------")

game_over = False
for move_number, correct_move in enumerate(move_sequence):
    # 'enumerate' gives us both the index (move_number) and the item (correct_move).
    
    try:
        player_input_str = input(f"Enter command for move #{move_number + 1}: ")
        player_command_num = int(player_input_str)
    except ValueError:
        print("Invalid input! You must enter a number. Game Over.")
        game_over = True
        break # Exit the loop immediately.

    # Convert the player's number command into a move string.
    player_move = ""
    if player_command_num == 1:
        player_move = "forward"
    elif player_command_num == 2:
        player_move = "left"
    elif player_command_num == 3:
        player_move = "right"
    
    # Check if the player's move matches the correct move from the sequence.
    if player_move == correct_move:
        print("Correct!")
        # Execute the move for the player's turtle.
        if player_move == "forward":
            player.forward(50)
        elif player_move == "left":
            player.left(90)
        elif player_move == "right":
            player.right(90)
    else:
        print(f"Wrong move! The correct move was '{correct_move}'. Game Over.")
        game_over = True
        break # Exit the loop immediately.

# --- 6. End of Game ---
# After the loop, check if the game ended because of a wrong move or because the player won.
if not game_over:
    print("\nCongratulations! You followed the path perfectly!")
    player.color("gold") # Change color to gold for winning.

print("\nClick on the turtle window to close it.")
turtle.exitonclick()
