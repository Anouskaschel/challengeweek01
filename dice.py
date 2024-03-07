import random

place_player_one = 0
place_player_two = 0
capital_player_one = 0
capital_player_two = 0
move_num = 0

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

def move_player(old_place):
    new_place = old_place + capital
    return new_place

while True:
    move_num += 1
    player_turn = str(move_num % 2 - 2)[1:]
    roll = input(f"PLAYER {player_turn} Roll the dice using r: ")
    if roll == "r":
        dice_one, dice_two, capital = roll_dice()
        dice_roll = f"Dice 1: {dice_one}, Dice 2: {dice_two}"
        # print(f"Capital: {capital}")
        if move_num % 2 == 0:
            place_player_two = move_player(place_player_two)
            capital_player_two += capital

            print("PLAYER 2: ")
            print(dice_roll)
            print(place_player_two)

        elif move_num % 2 != 0:
            place_player_one = move_player(place_player_one)
            capital_player_one += capital

            print("PLAYER 1: ")
            print(dice_roll)
            print(place_player_one)

    elif roll != "r":
        print("Input error")
    else:
        print("Fail")
