# alle Imports
import random
import time

# Variabeln
Ja = True
Nein = False
Liste = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v",
                   "w"  "x", "y", "z","@", "#", "%", "&", "/", "(", ")", "?", "!"]
ListeOhneS = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v",
              "w"  "x", "y", "z"]
passwort = []



# Code
anzahl = int(input("Wieviele Zeichen soll dein Passwort beinhalten?: "))
sonderzeichen = bool(input("Soll dein Passwort Sonderzeichen beinhalten? [Ja/Nein]: "))
if sonderzeichen == True:
    for i in range((anzahl), 0, -1):
        passwort.append(random.choice(Liste))
        time.sleep(0)
    print("Dein generiertes Passwort lautet: ", end="")
    for x in passwort:
        print(x, end="")
    time.sleep(5)

elif sonderzeichen == False:
    for i in range((anzahl), 0, -1):
        passwort.append(random.choice(ListeOhneS))
        time.sleep(0)
    print("Dein generiertes Passwort lautet: ", end="")
    for x in passwort:
        print(x)
    time.sleep(5)

while 1 == True:
    passwort = []
    print()
    erneut = input("Neues Passwort generieren? [Ja/Nein]: ",)
    if erneut == "Ja":
        anzahl = int(input("Wieviele Zeichen soll dein Passwort beinhalten?: "))
        sonderzeichen = bool(input("Soll dein Passwort Sonderzeichen beinhalten? [Ja/Nein]: "))
        if sonderzeichen == True:
            for i in range((anzahl), 0, -1):
                passwort.append(random.choice(Liste))
                time.sleep(0)
            print("Dein generiertes Passwort lautet: ", end="")
            for x in passwort:
                print(x, end="")
            time.sleep(5)

        elif sonderzeichen == False:
            for i in range((anzahl), 0, -1):
                passwort.append(random.choice(ListeOhneS))
                time.sleep(0)
            print("Dein generiertes Passwort lautet: ", end="")
            for x in passwort:
                print(x)
            time.sleep(5)
    elif erneut == "Nein":
        exit()
    else:
        exit()


