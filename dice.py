import random
import time


position_player_one = 0
position_player_two = 0
capital_player_one = 1000
capital_player_two = 1000
move_num = 0
budget = 1000
camper = [
    "Chassis - 60 florins",
    "Motor - 20 florins",
    "Vier wielen - 5 florins",
    "Carrosserie - 20 florins",
    "Cabine - 30 florins",
    "Leefruimte - 45 florins",
    "WC - 5 florins"
]
accommodation = [
    "Tent - 50 florins",
    "Caravan - 100 florins",
    "Bungalow - 500 florins",
    "Vakantie villa - 1000 florins"
]
purchased_boxes = {}
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
    ["Wat is het Romeinse cijfer 'C'?", "A. 10\nB. 100\nC. 1000", "B"],
    ["Welke Nederlandse provincie heeft de meeste inwoners?", "A. Noord-Holland\nB. Zuid-Holland\nC. Utrecht", "B"],
    ["Uit hoeveel zetels bestaat de Eerste kamer?", "A. 75\nB. 100\nC. 125", "A"],
    ["Wat is het grootste dier op aarde?", "A. Blauwe vinvis\nB. Potvis\nC. Walvishaai", "A"],
    ["Welke kleur cap heeft de keeper bij waterpolo?", "A. Rood\nB. Zwart\nC. Blauw", "A"],
    ["In welk jaar ging de film Shrek in premiere?", "A.1999\nB. 2000\nC. 2001", "C"]
]


def print_board():
    for i in range(1, 101):
        print("{:3}".format(i), end=" ")
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


def camper_item(capital):
    
    print("Kies 1 van de volgende items om je camper te construeren: ")

    while True:

        camper_str = "\n".join(camper)
        print(camper_str)

        camper_item = input().lower()

        if camper_item == "chassis":
            print("Je hebt de chassis gekozen\n")
            capital -= 60
            break
        elif camper_item == "motor":
            print("Je hebt de motor gekozen\n")
            capital -= 20
            break
        elif camper_item == "vier wielen":
            print("Je hebt de vier wielen gekozen\n")
            capital -= 5
            break
        elif camper_item == "carrosserie":
            print("Je hebt de carrosserie gekozen\n")
            capital -= 20
            break
        elif camper_item == "cabine":
            print("Je hebt de cabine gekozen\n")
            capital -= 30
            break
        elif camper_item == "leefruimte":
            print("Je hebt de leefruimte gekozen\n")
            capital -= 45
            break
        elif camper_item == "wc":
            print("Je hebt de wc gekozen\n")
            capital -= 5
            break
        else:
            print("Je moet één van deze opties kiezen: ")
            continue

    return capital


def car_accident_box(capital):
    print("Je hebt helaas autopech \nJe moet 250 florins betalen \n")
    
    capital -= 250
    
    return capital


def pay_player(cost, owner):
    if owner[-1] == "1":
        global capital_player_one 
        capital_player_one += cost
    elif owner[-1] == "2":
        global capital_player_two 
        capital_player_two += cost


def build_accommodation(player, position, capital):

    property_player = purchased_boxes.get(position)

    print("Kies een accomodatie om te bouwen: ")

    while True:

        accommodation_str = "\n".join(accommodation)
        print(accommodation_str)

        choose_accommodation = input("Als je niks wilt bouwen kies dan n \n").lower()

        if choose_accommodation == "tent":
            if property_player and property_player == player:
                print("In dit vakje staat al een tent")
            elif property_player:
                print(f"In dit vakje staat de tent van {property_player} \n{player} moet betalen aan {property_player}")
                capital -= 25
                pay_player(25, property_player)
            elif capital < 50:
                print("Je hebt niet genoeg florins om de bungalow te bouwen")
            else:
                print("Je hebt voor de tent gekozen")
                capital -= 50
            break
        elif choose_accommodation == "caravan":
            if property_player == player:
                print("In dit vakje staat al een caravan")
            elif property_player:
                print(f"In dit vakje staat de caravan van {property_player} \n{player} moet betalen aan {property_player}")
                capital -= 50
                pay_player(50, property_player)
            elif capital < 100:
                print("Je hebt niet genoeg florins om de bungalow te bouwen")
            else:
                capital -= 100
                print("Je hebt voor de caravan gekozen")
            break
        elif choose_accommodation == "bungalow":
            if property_player == player:
                print("In dit vakje staat al een bungalow")
            elif property_player:
                print(f"In dit vakje staat de bungalow van {property_player} \n{player} moet betalen aan {property_player}")
                capital -= 250
                pay_player(250, property_player)
            elif capital < 500:
                print("Je hebt niet genoeg florins om de bungalow te bouwen")
            else:
                print("Je hebt voor de bungalow gekozen")
                capital -= 500
            break
        elif choose_accommodation == "vakantie villa":
            if property_player == player:
                print("In dit vakje staat al een vakantie villa")
            elif property_player:
                print(f"In dit vakje staat de vakantie villa van {property_player} \n{player} moet betalen aan {property_player}")
                capital -= 500
                pay_player(500, property_player)
            elif capital < 1000:
                print("Je hebt niet genoeg florins om de vakantie villa te bouwen")
            else:
                print("Je hebt voor de vakantie villa gekozen")
                capital -= 1000
            break
        elif choose_accommodation == "n":
            print("Je wilt geen accommodatie bouwen \nDe volgende speler is aan de beurt \n")
            return capital
        else:
            print("Je moet één van deze opties kiezen: ")
            continue

    purchased_boxes[position] = player
    return capital


def quiz(capital):
    print("Je krijgt een multiplechoice vraag \nHiermee kan je geld verdienen")
    # A random question is put in the variable
    random_question = (random.choice(question))
    correct_answer = random_question[2]
    # Show first the question and after that the choices
    print(random_question[0])
    print(random_question[1])
    answer = input("Wat is je antwoord? ").upper()
    # It is true when the user input is the same as the asnwer
    if answer == random_question[2]:
        capital += 200
        print(f"Gefeliciteerd! Je hebt 200 florins verdiend \n")
    elif answer != "A" or answer != "B" or answer != "C":
        print("Invoer fout \nKies A, B of C")
    else:
        print(f"Helaas het antwoord was {correct_answer} \n")
    
    return capital

def meaning_box(player, position, capital):
    if position % 5 == 0:
        new_capital = camper_item(capital)

    elif position == 26 or position == 46 or position == 66 or position == 86:
        new_capital = car_accident_box(capital)

    elif position % 10 == 7 and position != 7:
        new_capital = build_accommodation(player, position, capital)

    elif position % 10 == 8 and position != 18 and position != 38 and position != 58 and position != 78:
        new_capital = quiz(capital)

    else:
        return capital
    
    return new_capital


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
            capital_player_two = meaning_box(player_turn, position_player_two, capital_player_two)

            print(f"Je oude budget was {old_capital} florins \nJe budget is nu {capital_player_two} florins ")

        elif move_num % 2 != 0:
            position_player_one = move_player(position_player_one)
            old_capital = capital_player_one
            capital_player_one += capital

            print(f"\n{dice_roll} \nJe positie is nu {position_player_one} \n")

            time.sleep(1)
            capital_player_one = meaning_box(player_turn, position_player_one, capital_player_one)

            print(f"Je oude budget was {old_capital} florins \nJe budget is nu {capital_player_one} florins ")

    else:
        print("Invoer fout")
        move_num -= 1
