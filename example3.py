# a python program to calculate the angles of a triangle
import math
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
# calculate the semi-perimeter
s = (side1 + side2 + side3) / 2
# calculate the area
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
# calculate the angles
angle1 = math.degrees(math.acos((side2**2 + side3**2 - side1**2) / (2 * side2 * side3)))
angle2 = math.degrees(math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3)))
angle3 = 180 - angle1 - angle2
print("Angles of the triangle are: %.2f, %.2f, %.2f" %(angle1, angle2, angle3))
# Path: example6.py
# //write a python program to calculate the volume of a cube
side = float(input("Enter the side of the cube: "))
volume = side * side * side
print("Volume of the cube is: %.2f" %volume)
# Path: example7.py
# //write a python program to calculate the volume of a cuboid
length = float(input("Enter the length of the cuboid: "))
breadth = float(input("Enter the breadth of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
volume = length * breadth * height
print("Volume of the cuboid is: %.2f" %volume)
# Path: example8.py
# //write a python program to calculate the volume of a cylinder
import math
radius = float(input("Enter the radius of the base: "))
height = float(input("Enter the height of the cylinder: "))
volume = math.pi * radius * radius * height
print("Volume of the cylinder is: %.2f" %volume)
# Path: example9.py
# //write a python program to calculate the volume of a cone
import math
radius = float(input("Enter the radius of the base: "))
height = float(input("Enter the height of the cone: "))
volume = (1/3) * math.pi * radius * radius * height
print("Volume of the cone is: %.2f" %volume)
# Path: example10.py
# //write a python program to calculate the volume of a sphere
import math
radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * radius * radius * radius
print("Volume of the sphere is: %.2f" %volume)
# Path: example11.py