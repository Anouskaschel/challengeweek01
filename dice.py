import random


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
purchased_boxes = {}

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
    new_place = (old_place + capital) % 100
    return new_place


def camper_item(capital):
    
    while True:
        camper_str = ", ".join(camper)
        print(camper_str)

        camper_item = input("Kies 1 van de volgende items om je camper te construeren: ").lower()

        if camper_item == "chassis":
            print("Je hebt de chassis gekozen.")
            capital -= 60
            break
        elif camper_item == "motor":
            print("Je hebt de motor gekozen.")
            capital -= 20
            break
        elif camper_item == "vier wielen":
            print("Je hebt de vier wielen gekozen.")
            capital -= 5
            break
        elif camper_item == "carrosserie":
            print("Je hebt de carrosserie gekozen.")
            capital -= 20
            break
        elif camper_item == "cabine":
            print("Je hebt de cabine gekozen.")
            capital -= 30
            break
        elif camper_item == "leefruimte":
            print("Je hebt de leefruimte gekozen.")
            capital -= 45
            break
        elif camper_item == "wc":
            print("Je hebt de wc gekozen.")
            capital -= 5
            break
        else:
            print("Kies 1 van de opties.")
            continue

    return capital


def car_accident_box(capital):
    print("Je hebt helaas autopech. Je moet 250 florins betalen.")
    
    capital -= 250
    print("Je budget is nu:", capital)
    
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

    while True:
        choose_accommodation = input("Kies een accommodatie. Als je niks wilt bouwen kies dan n ").lower()
        if choose_accommodation == "tent":
            if property_player and property_player == player:
                print("In dit vakje staat al een tent")
            elif property_player:
                print(f"In dit vakje staat de tent van {property_player}. {player} moet betalen aan {property_player}")
                capital -= 25
                pay_player(25, property_player)
            else:
                print("Je hebt voor de tent gekozen.")
                capital -= 50
                print("Je budget is nu:", capital)
            break
        elif choose_accommodation == "caravan":
            if property_player == player:
                print("In dit vakje staat al een caravan")
            elif property_player:
                print(f"In dit vakje staat de caravan van {property_player}. {player} moet betalen aan {property_player}")
                capital -= 50
                pay_player(50, property_player)
            else:
                capital -= 100
                print("Je hebt voor de caravan gekozen.")
                print("Je budget is nu:", capital)
            break
        elif choose_accommodation == "bungalow":
            if property_player == player:
                print("In dit vakje staat al een bungalow")
            elif property_player:
                print(f"In dit vakje staat de bungalow van {property_player}. {player} moet betalen aan {property_player}")
                capital -= 250
                pay_player(250, property_player)
            else:
                print("Je hebt voor de bungalow gekozen.")
                capital -= 500
                print("Je budget is nu:", capital)
            break
        elif choose_accommodation == "vakantie villa":
            if property_player == player:
                print("In dit vakje staat al een vakantie villa")
            elif property_player:
                print(f"In dit vakje staat de vakantie villa van {property_player}. {player} moet betalen aan {property_player}")
                capital -= 500
                pay_player(500, property_player)
            else:
                print("Je hebt voor de vakantie villa gekozen.")
                capital -= 1000
                print("Je budget is nu:", capital)
            break
        elif choose_accommodation == "n":
            print("Je wilt geen accommodatie bouwen. De volgende speler is aan de beurt.")
            return capital
        else:
            print("Kies 1 van de opties.")
            continue

    purchased_boxes[position] = player
    # print(purchased_boxes)
    return capital


def meaning_box(player, position, capital):
    if position % 5 == 0:
        new_capital = camper_item(capital)

    elif position == 26 or position == 46 or position == 66 or position == 86:
        new_capital = car_accident_box(capital)

    elif position % 10 == 7 and position != 7:
        new_capital = build_accommodation(player, position, capital)

    else:
        return capital
    
    return new_capital


while True:
    move_num += 1
    player_turn = "PLAYER" + " " + str(move_num % 2 - 2)[1:]
    roll = input(f"{player_turn} Roll the dice using r: ")
    if roll == "r":
        dice_one, dice_two, capital = roll_dice()
        dice_roll = f"Dice 1: {dice_one}, Dice 2: {dice_two}"

        if move_num % 2 == 0:
            position_player_two = move_player(position_player_two)
            capital_player_two += capital

            capital_player_two = meaning_box(player_turn, position_player_two, capital_player_two)

            print(f"PLAYER 2:\n {dice_roll} \n New position: {position_player_two} \n New capital: {capital_player_two}")
            print(dice_roll)
            print(f"New position: {position_player_two}")
            print(f"New capital: {capital_player_two}")

        elif move_num % 2 != 0:
            position_player_one = move_player(position_player_one)
            capital_player_one += capital

            capital_player_one = meaning_box(player_turn, position_player_one, capital_player_one)

            print("PLAYER 1: ")
            print(dice_roll)
            print("New position:", position_player_one)
            print("New capital:", capital_player_one)

    elif roll != "r":
        print("Input error")
        move_num -= 1
    else:
        print("Fail")
