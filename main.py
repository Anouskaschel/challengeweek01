
from item_shop import item_shop
from car_accident import car_accident
from build_accommodation import build_accommodation
from quiz import quiz


import random
import time

# REGISTRATION

position_player_one = 0
position_player_two = 0
capital_player_one = 1000
capital_player_two = 1000
move_num = 0

# item_shop
camper_player_one = {"chassis": {"price": 60, "count": 0},
              "motor": {"price": 20, "count": 0}, 
              "vier wielen": {"price": 5, "count": 0},
              "carrosserie": {"price": 20, "count": 0}, 
              "cabine": {"price": 30, "count": 0}, 
              "leefruimte": {"price": 45, "count": 0},
              "wc": {"price": 5, "count": 0}
              }
camper_player_two = {"chassis": {"price": 60, "count": 0},
              "motor": {"price": 20, "count": 0}, 
              "vier wielen": {"price": 5, "count": 0},
              "carrosserie": {"price": 20, "count": 0}, 
              "cabine": {"price": 30, "count": 0}, 
              "leefruimte": {"price": 45, "count": 0},
              "wc": {"price": 5, "count": 0}
              }

# build_accomodation
builded_accommodations = {"tent": {"price": 50, "purchased_boxes": {}},
    "caravan": {"price": 100, "purchased_boxes": {}},
    "bungalow": {"price": 500, "purchased_boxes": {}},
    "vakantie villa": {"price": 1000, "purchased_boxes": {}}
}


def print_board():
    for i in range(1, 101):
        print("[{:3}]".format(i), end=" ")
        if i % 10 == 0:
            print()


def roll_dice():

    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    capital = dice_one + dice_two
    return dice_one, dice_two, capital


def move_player(old_place):

    new_place = (old_place + capital) % 100
    return new_place


def meaning_of_box(player, position, capital):

    if position % 5 == 0:
        if player[-1] == "1":
            global camper_player_one
            new_capital = item_shop(capital, camper_player_one)

        elif player[-1] == "2":
            global camper_player_two 
            new_capital = item_shop(capital, camper_player_two)

    elif position == 26 or position == 46 or position == 66 or position == 86:
        new_capital = car_accident(capital)

    elif position % 10 == 7 and position != 7:
        new_capital, property_player, profit = build_accommodation(player, position, capital, builded_accommodations)

        if not property_player:
            pass
        elif property_player[-1] == "1":
            global capital_player_one
            capital_player_one += profit
        elif property_player[-1] == "2":
            global capital_player_two
            capital_player_two += profit

    elif position % 10 == 8 and position != 18 and position != 38 and position != 58 and position != 78:
        new_capital = quiz(capital)

    else:
        return capital
    
    return new_capital

if __name__ == "__main__":

    print_board()

    while True:
        move_num += 1
        player_turn = "SPELER" + " " + str(move_num % 2 - 2)[1:]
        roll = input(f"\n{player_turn} gebruik r om twee dobbelstenen te rollen: ").lower()

        if roll == "r":
            dice_one, dice_two, capital = roll_dice()
            dice_roll = f"Je hebt {dice_one} en {dice_two} gedobbeld"

            if move_num % 2 == 0:
                position_player_two = move_player(position_player_two)
                old_capital = capital_player_two
                capital_player_two += capital

                print(f"\n{dice_roll} \nJe positie is nu {position_player_two} \n")

                time.sleep(1)
                capital_player_two = meaning_of_box(player_turn, position_player_two, capital_player_two)

                print(f"Je oude budget was {old_capital} florins \nJe budget is nu {capital_player_two} florins ")

            elif move_num % 2 != 0:
                position_player_one = move_player(position_player_one)
                old_capital = capital_player_one
                capital_player_one += capital

                print(f"\n{dice_roll} \nJe positie is nu {position_player_one} \n")

                time.sleep(1)
                capital_player_one = meaning_of_box(player_turn, position_player_one, capital_player_one)

                print(f"Je oude budget was {old_capital} florins \nJe budget is nu {capital_player_one} florins ")
        elif roll == "q":
            exit()
        else:
            print("Invoer fout")
            move_num -= 1
