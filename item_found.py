

def item_found(capital, owner):

    if owner[-1] == "1":
        global camper_player_one
        
        while True:
            camper_keys = list(camper_player_one.keys())
            random_item = random.choice(camper_keys)
            count_item = camper_player_one[random_item]

            if count_item == 3:
                continue
            else:
                print(f"Je hebt {random_item} gevonden")
                camper_player_one[random_item] += 1
                break

    elif owner[-1] == "2":
        global camper_player_two

        while True:
            camper_keys = list(camper_player_two.keys())
            random_item = random.choice(camper_keys)
    
            if count_item == 3:
                continue
            else:
                print(f"Je hebt {random_item} gevonden")
                camper_player_one[random_item] += 1
                break

    return capital


    elif position % 10 == 9:
        new_capital = item_found(capital, player)