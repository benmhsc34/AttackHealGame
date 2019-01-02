import random

print("ARE YOUR EADY TO RUMMMBLE?")
Player1 = input("Input Player 1 name : ")
Player2 = input("Input Player 2 name : ")

random_damage = 0
random_attack = random.randint(0,1)
random_attack = bool(random_attack)
HP1 = 250
HP2 = 250
HP1 = int(HP1)
HP2 = int(HP2)

#1st attack
def bengame():
  random_attack = random.randint(0,1)
  random_attack = bool(random_attack)
  HP1 = 250
  HP2 = 250 

  Player1turn1 = True
  print(Player1,", take your position")

  while Player1turn1:
    Decision1P1 = input("\nDo you Attack (up to 100) or Heal (up to 50)?\n")
    if Decision1P1 == "Attack":
      if random_attack == True:
        random_damage=random.randint(1,100)
        HP2 = HP2 - random_damage
        text11 = "\n{}, your opponent has {} Health Points left\n"
        print(text11.format(random_damage, HP2))
        Player1turn1 = False
      else:
        print("\nYou tried throwing a knife but missed completely\n")
        Player1turn1 = False
    elif Decision1P1 == "Heal":
      if random_attack == True:
        random_damage=random.randint(1,50)
        HP1 = HP1 - random_damage
        text11 = "\nYou have healed up {} HP, you now have {}HP\n"
        print(text11.format(random_damage, HP1))
        Player1turn1 = False
      else:
        print("\n You tried to heal but were too scared of the needle\n")
        Player1turn1 = False
    else:
      print("\nPlease choose one or the other\n")
      Player1turn1 = False
  if HP2<=0:
    print("Game ends")
  else:
    
  
#2eme attaque
    print("\n" + Player2,", get ready for your payback")
    Player2turn1 = True
    while Player2turn1:
      Decision1P1 = input("\nDo you Attack (up to 100) or Heal (up to 50)?\n")
      if Decision1P1 == "Attack":
        if random_attack == True:
          random_damage=random.randint(1,100)
          HP1 = HP1 - random_damage
          text11 = "\n{}, your opponent has {} Health Points left\n"
          print(text11.format(random_damage, HP2))
          Player2turn1 = False
        else:
          print("\nYou tried throwing a rock, but it didn't reach him due to your lack of strength\n")
          Player2turn1 = False
      elif Decision1P1 == "Heal":
        if random_attack == True:
          random_damage=random.randint(1,50)
          HP2 = HP2 + random_damage
          text11 = "\nYou have healed up {} HP, you now have {}HP\n"
          print(text11.format(random_damage, HP2))
          Player2turn1 = False
        else:
          print("\n You forgot your bandages at home,you couldn't healup after all\n")
          Player2turn1 = False
      else:
        print("\nPlease choose one or the other\n")
      Player2turn1 = False
  if HP1<=0:
    print(Player2,"you have killed",Player1)
  else:
    bengame()
    
Player1turn1 = True
print(Player1,", take your position")

while Player1turn1:
    Decision1P1 = input("\nDo you Attack (up to 100) or Heal (up to 50)?\n")
    if Decision1P1 == "Attack":
      if random_attack == True:
        random_damage=random.randint(1,100)
        HP2 = HP2 - random_damage
        text11 = "\n{}, your opponent has {} Health Points left\n"
        print(text11.format(random_damage, HP2))
        Player1turn1 = False
      else:
        print("\nyou tried throwing a knife but missed completely\n")
        Player1turn1 = False
    elif Decision1P1 == "Heal":
      if random_attack == True:
        random_damage=random.randint(1,50)
        HP1 = HP1 + random_damage
        text11 = "\nyou have healed up {} HP, you now have {}HP\n"
        print(text11.format(random_damage, HP1))
        Player1turn1 = False
      else:
        print("\n you tried to heal but were too scared of the needle")
        Player1turn1 = False
    else:
      print("Please choose one or the other")
      Player1turn1 = False
if HP2<=0:
    print(Player1,"you have killed",Player2)
else:
    
  
#2eme attaque

    print(Player2,", get ready for your payback")
    Player2turn1 = True
    while Player2turn1:
      Decision1P1 = input("\nDo you Attack (up to 100) or Heal (up to 50)?\n")
      if Decision1P1 == "Attack":
        if random_attack == True:
          random_damage=random.randint(1,100)
          HP1 = HP1 - random_damage
          text11 = "\n{}, your opponent has {} Health Points lef\nt"
          print(text11.format(random_damage, HP2))
          Player2turn1 = False
        else:
          print("\nYou tried throwing a rock, but it didn't reach him due to your lack of strength\n")
          Player2turn1 = False
      elif Decision1P1 == "Heal":
        if random_attack == True:
          random_damage=random.randint(1,50)
          HP2 = HP2 + random_damage
          text11 = "\nyou have healed up {} HP, you now have {}HP\n"
          print(text11.format(random_damage, HP2))
          Player2turn1 = False
        else:
          print("\n You forgot your bandages at home,you couldn't healup after all\n")
          Player2turn1 = False
      else:
        print("Please choose one or the other")
      Player2turn1 = False
if HP1<=0:
    print(Player2,"you have killed",Player1)
else:
    bengame()
