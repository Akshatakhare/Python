import math

# radius=float(input("Enter the radius : "))
# area= math.pi*radius**2
# print("The area of the circle is : ",area)
# circumference= 2*math.pi*radius
# print("The circumference of the circle is : ",circumference)

def calculate_area(radius):
 """Calculate the area of a circle given its radius."""
 area = math.pi * radius ** 2
 return area
def calculate_circumference(radius):
 """Calculate the circumference of a circle given its radius."""
 circumference = 2 * math.pi * radius
 return circumference
# Example usage
radius=float(input("Enter the radius : "))
area = calculate_area(radius)
circumference = calculate_circumference(radius)
# print(f"radius: {radius}")
print(f"area: {area}")
print(f"Circumference: {circumference}")
