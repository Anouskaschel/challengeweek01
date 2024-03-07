import random

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
new_place = 24
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

accommodation = [
    "Tent - 50 florins",
    "Caravan - 100 florins",
    "Bungalow - 500 florins",
    "Vakantie villa - 1000 florins"
]

question = [
    ["Hoeveel continenten zijn er?", "A. 4\nB. 5\nC. 6", "C"],
    ["Wat is het element AU?", "A. Goud\n B. Zilver\n C. Brons", "A"],
    ["Hoeveel poten heeft een spin", "A. 8\nB. 7\nC. 6", "A"],
    ["In welk jaar begon de Tweede Wereldoorlog?", "A. 1938\nB. 1939\nC. 1940", "B"],
    ["Wie heeft het schilderij 'Meisje met de parel' geschilderd?", "A. Vincent van Gogh\nB. Piet Mondriaan\nC. Johannes Vermeer", "C"],
    ["Wat is het getal 333 in hexadecimaal?", "A. 14B \n B. 14C \n C. 14D", "C"],
    ["In welk land is het gebruikelijk om borden in een restaurant te gooien?", "A. Griekenland\nB. Frankrijk\nC. Portugal", "A"],
    ["Hoe noem je iemand uit India?", "A. Indiaan\nB. Indiër\nC. Indiander", "B"],
    ["Welk land wordt ook wel het land van de glimlach genoemd?", "A. Thailand\nB. China\nC. Japan", "A"],
    ["Wat is de hoofdstad van Gelderland?", "A. Nijmegen\nB. Apeldoorn\nC. Arnhem", "C"],
    ["Welke Nederlandse stad wordt ook wel de sleutelstad genoemd?", "A. Leiden\nB. Utrecht\nC. Amsterdam", "A"],
    ["Hoeveel kleuren zitten er in een regenboog?", "A. 6\nB. 7\nC. 8", "B"],
    ["Wat is de beste combinatie van vijf kaarten in een spel poker?", "A. Straight flush\nB. Royal Flush\nC. FOur of a kind", "B"],
    ["Wat is de naam van de grootste vulkaan in Italië?", "A. Pompeii\nB. Stromboli\nC. Etna", "C"],
    ["Wat is het Romeinse cijfer 'C'?", "A. 10\nB. 100\nC. 1000", "B"]
]

def camper_item():

    camper_item = input("Kies 1 van de volgende items om je camper te construeren: ").lower()
    if camper_item == "chassis":
        print("Je hebt de chassis gekozen.")
        budget = budget - 60
    elif camper_item == "motor":
        print("Je hebt de motor gekozen.")
        budget = budget - 20
    elif camper_item == "vier wielen":
        print("Je hebt de vier wielen gekozen.")
        budget = budget - 5
    elif camper_item == "carrosserie":
        print("Je hebt de carrosserie gekozen.")
        budget = budget - 20
    elif camper_item == "cabine":
        print("Je hebt de cabine gekozen.")
        budget = budget - 30
    elif camper_item == "leefruimte":
        print("Je hebt de leefruimte gekozen.")
        budget = budget - 45
    elif camper_item == "wc":
        print("Je hebt de wc gekozen.")
        budget = budget - 5
    else:
        print("Kies 1 van de opties.")
    return budget

def build_accommodation():
    budget = 1000

    choose_accommodation = input("Kies een accommodatie. Als je niks wilt bouwen kies dan n ").lower()
    if choose_accommodation == "tent":
        print("Je hebt voor de tent gekozen.")
        budget = budget - 50
        
        print("Je budget is nu:", budget)
    elif choose_accommodation == "caravan":
        print("Je hebt voor de caravan gekozen.")
        budget = budget - 100
        print("Je budget is nu:", budget)
    elif choose_accommodation == "bungalow":
        print("Je hebt voor de bungalow gekozen.")
        budget = budget - 500
        print("Je budget is nu:", budget)
    elif choose_accommodation == "vakantie villa":
        print("Je hebt voor de vakantie villa gekozen.")
        budget = budget - 1000
        print("Je budget is nu:", budget)
    elif choose_accommodation == "n":
        print("Je wilt geen accommodatie bouwen. De volgende speler is aan de beurt.")
    else:
        print("Kies 1 van de opties.")
    return budget


if new_place % 5 == 0:
    choose_item = input("Je mag een stuk van de camper construeren.")
    for i in camper:   
        print(i)
        camper_item()
elif new_place == 26 or new_place == 46 or new_place == 66 or new_place == 86:
    print("Je hebt helaas autopech. Je moet 250 florins betalen.")
    budget = budget - 250
    print("Je budget is nu:", budget)
elif new_place == 7 or list(str(new_place))[1] == "7":
    print("Je kan een accommodatie bouwen.")
    for i in accommodation:
        print(i)
        build_accommodation()
elif new_place == 24:
    print("Je krijgt een multiplechoice vraag. Hiermee kan je geld verdienen.")
    # A random question is put in the variable
    random_question = (random.choice(question))
    correct_answer = random_question[2]
    # Show first the question and after that the choices
    print(random_question[0])
    print(random_question[1])
    answer = input("Wat is je antwoord? ").upper()
    # It is true when the user input is the same as the asnwer
    if answer == random_question[2]:
        budget += 200
        print("Gefeliciteerd! Je hebt 200 florins verdiend.")
    else:
        print(f"Helaas het antwoord was {correct_answer}.")
else:
    print("Fail")
