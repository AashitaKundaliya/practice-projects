#x = 8
#if (x == 8):
    #print("It works")
#print(2**3)

#Program to find factorial of a number
def fact(n):
        if n==1:
            return 1

        else:
            return n*fact(n-1)


num= int(input("Enter a positive integer number to find it's factorial\n"))
if num==0:
    print("The factorial of the number is 1")
elif num<0:
    print("Please enter a positive number")
else:
    print(fact(num))