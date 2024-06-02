#LIST

# a=["hi", 45,67,78,89,90,12,34]
# print(a[0:9:2])

# list comprehension
# list=[i*i for i in range(10)]   #1
# print(list)

# name=["sona","rohan","Roshmita", "oops!"]    #2
# name_o=[i for i in name if "o" in i]
# print(name_o)

# LIST METHODS
# a1=[12,23,34,34,45,5,6,67,78,89,90,"hi"]
# # length
# print(len(a1))
# print(a1.index(45))
# print(a1[2:8])
# print(a1.count(34))
# a1.append(89) #APPEND ME KYA ADD KRNA HAI VO BTANA
# print(a1) 
# print(len(a1))
# a1.pop(12) #POP ME INDEX VALUE BTANA HAI
# print(a1)
# a1.insert(5,56)
# print(a1)
# # ab sort ke liye string niklna parega therefore
# print(a1.index("hi"))
# a1.pop(12)
# a1.sort()
# print(a1)
# a1.reverse()
# print(a1)

#TUPLES
# s=(1,2,3,4,5,78,6,7,88,90,"koi mil gya",78)
# print(s)

# edit a tuple

color=("red","pink","yellow","blue","black","green")
temp=list(color)
temp.append("orange")
# temp.pop(4)
temp[4]="lavender"
color=tuple(temp)
print(color)

