print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print(
    "You awaken on the sun-drenched shores of a mysterious island. A map flutters in your hand, marked with a bold red "
    "X.\nSomewhere on this island, a treasure lies hidden — and it’s yours to find.")

question_1 = input(
    "\nTwo paths lie ahead. One leads left into a lush jungle, the other right into a shadowy ravine.\nDo you go left "
    "or right?\n").lower()

if question_1 == "left":
    print("\nThe jungle opens into a tranquil lake. A raft bobs near the shore, and a stone bench invites you to wait.")
    question_2 = input("Do you swim across or wait patiently?\n").lower()

    if question_2 == "wait":
        print("\nThe mist clears and a hidden temple emerges. Its entrance glows with three enchanted doors.")
        question_3 = input("Which door do you choose? Red, yellow, or blue?\n").lower()

        if question_3 == "red":
            print("🔥 The door bursts into flames. You’re consumed by fire. Game Over.")
        elif question_3 == "blue":
            print("🐾 You step into a den of beasts. Their eyes gleam hungrily. Game Over.")
        elif question_3 == "yellow":
            print("💰 The door creaks open to reveal a golden chest. You’ve found the treasure. You Win!")
        else:
            print("The door vanishes. You’re lost in the temple forever. Game Over.")
    else:
        print("🐟 A trout leaps from the water and knocks you unconscious. Game Over.")
else:
    print("🕳️ The ground crumbles beneath you. You fall into a hidden pit. Game Over.")
