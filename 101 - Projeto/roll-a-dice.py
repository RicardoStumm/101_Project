import random
import os

response = 'y'

while response == 'y':
    no = random.randint(1, 6)
    response = input(str("Quer jogar o dado? y para sim n para não: "))
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[     ]")
        print("[ * * ]")
        print("[     ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[ * * ]")
        print("[  *  ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[  *  ]")
        print("[ * * ]")
        print("[  *  ]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[ * * ]")
        print("[  *  ]")
        print("[ * * ]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[ * * ]")
        print("[ * * ]")
        print("[ * * ]")
        print("[-----]")
