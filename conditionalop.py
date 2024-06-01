# #Conditional operators
# a=int(input("Enter the value:"))

# print(a>19)
# print(a>=19)
# print(a<=19)
# print(a!=19)
# print(a<19)

#IF ELSE

#1. Write a program aboutchild marriage take inout from the user
# age=int(input("Enter your age: "))
# if(age<21):
#     print("Child Marriage")
# else:
#     print("cooking seekhi?hanji!!")

# print("Muje bhi krni h yar shaadi")

# ELIF STATEMENTS

# Write a program dividing the pens among three colors- red, blue, black

# pen=input("Color : ")
# if(pen=="blue"):
#     print("its a blue pen.")
# elif(pen=="red"):
#     print("It is a red pen.")
# elif(pen=="Black"):
#     print("it is a black pen.")
# else:
#     print("We don't consider it as a pen.")

#NESTED IF
s=int(input("enter:"))
if (s < 0):
    print("Number is negative.")
elif (s > 0):
    if (s <= 10):
        print("Number is between 1-10")
    elif (s > 10 and s <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")