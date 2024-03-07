# import random

# capital_player_one = 0
# capital_player_two = 0
# start_budget = 1000

# def print_board():
#     for i in range(1, 101):
#         print("[{:3}]".format(i), end=" ")
#         if i % 10 == 0:
#             print()

# # Example usage:
# print_board()

# def roll_dice():
#     dice_one = random.randint(1, 6)
#     dice_two = random.randint(1, 6)
#     capital = dice_one + dice_two
#     return dice_one, dice_two, capital


# dice_one, dice_two, capital = roll_dice()
# capital_player_one += capital

# dice_one, dice_two, capital = roll_dice()
# capital_player_two += capital

# # def move_player():
# #     old_place = 0
# #     new_place = old_place + capital
# #     return old_place, new_place

# # old_place, new_place = move_player()

# roll = input("Roll the dice using r")
# if roll == "r":
#     roll_dice()
#     old_place = 0
#     i = old_place
#     while i < 101:
#         # print("number", capital)
#         new_place = old_place + capital
#         print(new_place)
#         # print(new_place[1])
# else:
#     print("Fail")
new_place = 5
budget = 1000

camper = [
    "Chassis - 60 florins",
    "Motor - 20 florins",
    "Vier wielen - 5 florins",
    "Carrosserie - 20 florins",
    "Cabine - 30 florins",
    "Leefruimte - 45 florins",
    "WC - 5 florins",
]

if new_place % 5 == 0:
    camper_item = input("Kies 1 van de volgende items om je camper te construeren: ")
    for i in camper:   
        print(i)
        if camper_item.lower() == "chassis":
            print("Je hebt de chassis gekozen.")
            budget = budget - 60
        elif camper_item.lower() == "motor":
            print("Je hebt de motor gekozen.")
            budget = budget - 20
        elif camper_item.lower() == "vier wielen":
            print("Je hebt de vier wielen gekozen.")
            budget = budget - 5
        elif camper_item.lower() == "carrosserie":
            print("Je hebt de carrosserie gekozen.")
            budget = budget - 20
        elif camper_item.lower() == "cabine":
            print("Je hebt de cabine gekozen.")
            budget = budget - 30
        elif camper_item.lower() == "leefruimte":
            print("Je hebt de leefruimte gekozen.")
            budget = budget - 45
        elif camper_item.lower() == "wc":
            print("Je hebt de wc gekozen.")
            budget = budget - 5
        else:
            print("Kies 1 van de opties.")
elif new_place == 26 or new_place == 46 or new_place == 66 or new_place == 86:
    print("Je hebt helaas autopech. Je moet 250 florins betalen.")
    budget = budget - 250
    print("Je budget is nu:", budget)
else:
    print("Fail")