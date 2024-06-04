# EXCEPTIONAL HANDLING CONTINUED
# FINNALLY STATEMENT KE SATH

try:
    l=[1,5,9,6,7]
    i=int(input("Enter the required index: "))
    print(l[i])
except :
    print("Invalid Input")
finally:
    print("always executed")

print("mai bhi hunga bhai execute hmesha")
# 
#

# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")
# finally:
#     print("This block is always executed.")

