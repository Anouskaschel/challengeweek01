
import random

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


def quiz(capital):
    print("Je krijgt een multiplechoice vraag \nHiermee kan je geld verdienen")
    # A random question is put in the variable
    random_question = (random.choice(question))
    correct_answer = random_question[2]
    # Show first the question and after that the choices
    while True:
        print(random_question[0])
        print(random_question[1])
        answer = input("Wat is je antwoord? ").upper()
        # It is true when the user input is the same as the asnwer
        if answer == random_question[2]:
            capital += 200
            print(f"Gefeliciteerd! Je hebt 200 florins verdiend \n")
            break
        else:
            print(f"Helaas het antwoord was {correct_answer} \n")
            break
        
    return capital
