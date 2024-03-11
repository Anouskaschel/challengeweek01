
accommodation = [
    "Tent - 50 florins",
    "Caravan - 100 florins",
    "Bungalow - 500 florins",
    "Vakantie villa - 1000 florins"
]

def build_accommodation(player, position, capital, registration):

    profit = 0
    property_player = None
    print("Kies een accomodatie om te bouwen: ")

    while True:

        accommodation_str = "\n".join(accommodation)
        print(accommodation_str)

        choose_accommodation = input("Als je niks wilt bouwen kies dan n \n").lower()

        if choose_accommodation in registration:
            
            property_player = registration[choose_accommodation]["purchased_boxes"].get(position)
            price = registration[choose_accommodation]["price"]

            if property_player and property_player == player:
                print("In dit vakje staat al een tent \n")
            
            elif property_player:
                print(f"In dit vakje staat de {choose_accommodation} van {property_player} \n{player} moet betalen aan {property_player} \n")
                capital -= price // 2
                profit = price // 2

            elif capital < price:
                print(f"Je hebt niet genoeg florins om de {choose_accommodation} te bouwen \n")
            
            else:
                print(f"Je hebt voor de {choose_accommodation} gekozen \n")
                capital -= price
                registration[choose_accommodation]["purchased_boxes"][position] = player
            break
        
        elif choose_accommodation == "n":
            print("Je wilt geen accommodatie bouwen \nDe volgende speler is aan de beurt \n")
            break
        
        else:
            print("\nJe moet één van deze opties kiezen: ")
            continue

    return capital, property_player, profit