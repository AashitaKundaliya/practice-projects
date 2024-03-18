import random
print("The game will choose a random number by itself unknown to everyone. you will be given 5 chances and 5 hints "
      "to guess the number correctly.")
print("With each hint, 10 points will be deducted. Maximum points that can be aquired "
      "are 50. GOOD LUCK!!!")

while True:
      num = int(input("Enter a number\n"))
      flag = 0
      if num > 1:
            for i in range(2,num):
                  if (num % i) == 0:
                        flag = 1
                        break

      if flag == 1 :
            print("The number is composite")
      else:
            print("The number is prime")
      break


'''
while True:
      num = int(input(" enter a number\n"))
      if num%2 ==0:
            print("The number is even")
            break
      else:
            print("The number is odd")
            break
'''

