# key pair hote hai

dic={"name":"akshata", "key":"value","han":True}
print(dic)
print(dic.items())
print(dic["name"])
print(dic.get("han"))
print(dic.keys())
print(dic.values())

# dictinoary methods
ep1={234:34,345:90,908:80,596:96}
ep2={890:89,465:78,526:75}
# update
# ep1.update(ep2)
# print(ep1)

# clear
print(ep1.clear())
print(ep1)

# popout
# ep2.pop(526)
# print(ep2)

ep2.popitem()
print(ep2)

