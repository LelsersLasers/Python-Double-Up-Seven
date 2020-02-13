import random

Moves = ["block", "reload", "shoot"]
bullets = 0
attack = 100
theirHp = 100
yourHp = 100
heal = 100
theirBullets = 0
again = True
turn = 0

while again:
  themBlocking = False
  youBlocking = False
  turn = turn + 1

  if turn == 1:
    theirTurn = "reload"
  else:
    if theirBullets == 0:
      theirTurn = random.choice(Moves[0], Moves[1])
    elif theirBullets > 4:
      theirTurn = random.choice([Moves[0], Moves[2]])
    else:
      theirTurn = random.choice(Moves)
    if theirTurn == "block":
      themBlocking = True
  
  yourAttack = input("Which move do you want to do: (press 'r' to reload, press 'a' to attack, and press 'b' to block): ")
  
  if yourAttack == 'r':
    bullets = bullets + 1
    canAttack = True
    print("You reload and now have " + str(bullets) + " bullets.")
  
  elif yourAttack == 'a':
    if bullets == 0:
      print("You try to shoot but you have no Ammo!")
    else:
      print("You shoot!!")
      bullets = bullets - 1
      if themBlocking:
        print("They blocked it!")
      else:
        theirHp = theirHp - attack
  
  else: #if yourAttack == 'b': 
    print("You are blocking!")
    youBlocking = True
   
  if theirTurn == "reload":
    theirBullets = theirBullets + 1
    print("They reload and now have " + str(theirBullets) + " bullets.")
  
  elif theirTurn == "shoot":
    print("They shoot!")
    theirBullets = theirBullets - 1
    if youBlocking:
      print("You blocked it!")
    else:
      yourHp = yourHp - attack
  
  else:
    print("They block")

  if theirHp == yourHp and yourHp == 0:
    yourHp = 100
    theirHp = 100
  elif theirHp == 0 or yourHp == 0:
    again = False
  print("Your HP: " + str(yourHp))
  print("Their HP: " + str(theirHp))
  print("")

print("")
if theirHp < yourHp:
  print("You have won!")
else:
  print("You have lost!")
  
