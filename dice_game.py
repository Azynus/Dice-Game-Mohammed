#MOhammed Sanogo

import random

def roll_dice():
    return [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

def is_tuple_out(dice):
    return dice[0] == dice[1] == dice[2]

# Test dice rolling
dice = roll_dice()
print("Rolled dice:", dice)
if is_tuple_out(dice):
    print("Tuple out! Score: 0")
else:
    print("No tuple out. You can continue.")
    
    
def find_fixed_dice(dice):
    fixed = [False, False, False]
    if dice[0] == dice[1]:
        fixed[0] = fixed[1] = True
    if dice[0] == dice[2]:
        fixed[0] = fixed[2] = True
    if dice[1] == dice[2]:
        fixed[1] = fixed[2] = True
    return fixed

# Test fixed dice
fixed_dice = find_fixed_dice(dice)
print("Fixed dice:", fixed_dice)

def re_roll_dice(dice, fixed):
    for i in range(3):
        if not fixed[i]:  # Only re-roll non-fixed dice
            dice[i] = random.randint(1, 6)
    return dice


# Test re-rolling
while not is_tuple_out(dice):
    print("Current dice:", dice)
    fixed_dice = find_fixed_dice(dice)
    if all(fixed_dice):
        print("All dice are fixed. Ending turn.")
        break
    choice = input("Do you want to re-roll non-fixed dice? (yes/no): ").strip().lower()
    if choice == "no":
        break
    dice = re_roll_dice(dice, fixed_dice)

print("Final dice:", dice)
if is_tuple_out(dice):
    print("Tuple out! Score: 0")
else:
    print("Score for this turn:", sum(dice))


def play_turn():
    dice = roll_dice()
    print("Initial roll:", dice)
    while not is_tuple_out(dice):
        fixed_dice = find_fixed_dice(dice)
        print("Fixed dice:", fixed_dice)
        if all(fixed_dice):
            print("All dice are fixed. Ending turn.")
            break
        choice = input("Do you want to re-roll non-fixed dice? (yes/no): ").strip().lower()
        if choice == "no":
            break
        dice = re_roll_dice(dice, fixed_dice)
        print("New roll:", dice)

    if is_tuple_out(dice):
        print("Tuple out! Score: 0")
    else:
        print("Your score for this turn:", sum(dice))

# Play a single turn
play_turn()
