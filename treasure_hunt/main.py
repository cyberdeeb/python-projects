print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.") 

crossroads = input("You have reached a crossroads. One road leads you to the Dark Forest, while the other leads to the Enchanted Garden. Which do you choose?\n").lower()

if crossroads == "enchanted garden":
  print("You are swarmed by giant wasps that view you as an invader. Game Over.")
else:
  item = input("You are approached by a wizard within the Dark Forest. He asks you to choose between two items: a sword or an apple. Which will you choose?\n")
  if item == "apple":
    print("You take a bite of the apple only to realize that it is poison. You die a quick death. Game Over.")
  else:
    door = input("Once you grab the sword you are teleported to a room with two doors. Do you choose the left or right door?\n")
    if door == "right":
      print("You have opened the door and a ball of fire hits you. Game Over.")
    else:
      print("The room shines bright, you see gold piled high. You have found the treasure! You win!")