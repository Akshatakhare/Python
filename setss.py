#SETS

# 1. joining sets
s1= {"Tokyo", "Madrid", "Berlin", "Delhi"}
s2= {"Tokyo","seoul","Madrid","Kabul"}

# 1.1 union and update()                             #ye sb ye bar me nhi dekhnege kyuki set same update krne pr s11 change ho jayega 
print(s1.union(s2))                                    #so if you want to check each one of them toh comment krke check krna 
s1.update(s2)                                          #but for now mene kuch bhi comment ni kra h but fr output ni dekhega sbka
print(s1)

# 1.2  intersection and intersection_update():
print(s1.intersection(s2))


# 1.3 symmetric_difference and symmetric_difference_update():
print(s1.symmetric_difference(s2))

s1.symmetric_difference_update(s2)
print(s1)

# 1.4 difference() and difference_update():
print(s1.difference(s2))

s1.difference_update(s2)
print(s1)


# in-built set methods

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# QUES
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")