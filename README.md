#MOhammed Sanogo

# Dice Game

## Overview
This is a command-line dice game where players roll dice to maximize their score while avoiding "tuple out."



## Features 

1) Dice Rolling: Rolls three dice per turn and displays the results.

2) Tuple Out Detection: If all three dice show the same number, the player "tuples out" and scores zero points.

3) Fixed Dice: If two dice have the same value, they are marked as "fixed" and cannot be re-rolled.

4) Re-rolling: You can re-roll any dice that are not fixed until they choose to stop or tuple out.

5) Scoring: you earn points based on the sum of all three dice at the end of their turn .


## How to Use the Program
Prerequisites
To run this program, ensure you have Python 3.x installed on your system.

# Running the Program

1) Save the File: Save the code in a file named dice_game.py.

2) Open Terminal: Navigate to the directory where dice_game.py is saved by running:
EX:
cd path/to/your/file

3) Run the Game:
python dice_game.py



# How to Play the Game

1) Initial Roll: The program rolls three dice and displays the result.

2) Fixed Dice: If two dice match, they are marked as "fixed" and cannot be re-rolled.

3) Re-rolling Non-Fixed Dice:
A) The program will prompt you to re-roll any non-fixed dice.
B) Enter yes to re-roll or no to stop and finalize your score.

4) Score Calculation:
A) If you stop, your score is the sum of all three dice.
B) If you roll three matching numbers (tuple out), you score zero points.

Example Game Interaction
Initial roll: [1, 2, 2]
Fixed dice: [False, True, True]
Do you want to re-roll non-fixed dice? (yes/no): yes
New roll: [4, 2, 2]
Fixed dice: [False, True, True]
Do you want to re-roll non-fixed dice? (yes/no): no
Your score for this turn: 8

## Error Handling
The program handles invalid inputs:
If you enter an invalid response,the program will prompt you again until valid input is provided.

## Why this README is Helpful
This README is designed to provide clear, instructions for using the Dice Game. 
It explains:
How to set up and run the program.
The rules of the game.
What to expect during gameplay.

This ensures that even users with minimal coding knowledge can understand how to play the game.
