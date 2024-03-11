
camper = [
    "Chassis - 60 florins",
    "Motor - 20 florins",
    "Vier wielen - 5 florins",
    "Carrosserie - 20 florins",
    "Cabine - 30 florins",
    "Leefruimte - 45 florins",
    "WC - 5 florins"
]


def item_shop(capital, camper_items):

    print("Kies 1 van de volgende items om je camper te construeren: ")

    while True:

        camper_str = "\n".join(camper)
        print(camper_str)

        camper_item = input().lower()

        try:
            price = camper_items[camper_item]["price"]
            count_items = []

            if camper_item == "chassis":
                print("Je hebt de chassis gekozen\n")
                capital -= price
                camper_items[camper_item]["count"] += 1
                break
            elif camper_item == "motor":
                print("Je hebt de motor gekozen\n")
                capital -= price
                camper_items[camper_item]["count"] += 1
                break
            elif camper_item == "vier wielen":
                print("Je hebt de vier wielen gekozen\n")
                capital -= price
                camper_items[camper_item]["count"] += 1
                break
            elif camper_item == "carrosserie":
                print("Je hebt de carrosserie gekozen\n")
                capital -= price
                camper_items[camper_item]["count"] += 1
                break
            elif camper_item == "cabine":
                print("Je hebt de cabine gekozen\n")
                capital -= price
                camper_items[camper_item]["count"] += 1
                break
            elif camper_item == "leefruimte":
                print("Je hebt de leefruimte gekozen\n")
                capital -= price
                camper_items[camper_item]["count"] += 1
                break
            elif camper_item == "wc":
                print("Je hebt de wc gekozen\n")
                capital -= price
                camper_items[camper_item]["count"] += 1
                break
        except:
            print("Je moet één van deze opties kiezen: ")
            continue

    for item in camper_items.values():
        count_items.append(item["count"])
      
    if not 0 in count_items:
        print("Je hebt een voledige camper set verzamelt!")
        
        while True:

            camper_construeren = input("Wil jij deze set verkopen voor 400 florins (ja/nee)? ").lower()

            if camper_construeren == "ja":
                capital += 400
                print("\nDit zijn de items die je overhoud: ")
                for item_tup in camper_items.items():
                    item = item_tup[0]
                    camper_items[item]["count"] -= 1
                    count = item_tup[1]["count"]
                    print(f"{item} - hoeveelheid: {count}")
                print()
                break

            elif camper_construeren == "nee":
                print("Je wilt de set niet verkopen \nDe volgende speler is aan de beurt \n")
                break
            else:
                print("Je moet ja of nee kiezen")
                continue
    
    else:
        print(f"Dit zijn de items die je hebt: ")

        for item_tup in camper_items.items():
            item = item_tup[0]
            count = item_tup[1]["count"]
            print(f"{item} - hoeveelheid: {count}")
        print()

    return capital

