import random
while 1:
  print("1. roll the dice or 2. stop the game")
  number = int(input("choose 1 or 2\n"))
  if number==1:
    num = random.randint(1,6)
    print(num)
  elif number==2:
    break
  else:
    print("enter the value from 1 or 2")
