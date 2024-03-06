import random

capital_player_one = 0
capital_player_two = 0

def print_board():
    for i in range(1, 101):
        print("{:3}".format(i), end=" ")
        if i % 10 == 0:
            print()

# Example usage:
print_board()

def roll_dice():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    capital = dice_one + dice_two
    return dice_one, dice_two, capital


dice_one, dice_two, capital = roll_dice()
capital_player_one += capital

dice_one, dice_two, capital = roll_dice()
capital_player_two += capital

def move_player():
    old_place = 0
    new_place = old_place + capital
    return old_place, new_place

roll = input("Roll the dice using r")
if roll == "r":
    try:
        roll_dice()
        move_player()
        # print(new_place)
    except Exception as e:
        print("An error occurred:", e)
else:
    print("Fail")

