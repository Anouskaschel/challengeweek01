
import random


capital_player_one = 0
capital_player_two = 0


def roll_dice():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    capital = dice_one + dice_two
    return dice_one, dice_two, capital


dice_one, dice_two, capital = roll_dice()
capital_player_one += capital

dice_one, dice_two, capital = roll_dice()
capital_player_two += capital

