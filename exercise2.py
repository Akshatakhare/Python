#create a program that greets the user according to the timezone
t=int(input("Enter the Timezone:"))

if(t<=11):
    print("Good Morning")
elif(t>=12 and t<16):
    print("Good Afternoon")
elif(t>=16 and 21>t):
    print("Good Evening")
else:
    print("Good Nightt \nSweet dreams")