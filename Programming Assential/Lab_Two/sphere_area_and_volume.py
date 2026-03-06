import math

radius=float(input("Please enter the radius of a sphere: "))
sphere_area=4*math.pi*radius*radius
sphere_volume=(4/3)*math.pi*radius*radius*radius

print("Area of sphere is = %.2f"%sphere_area)
print("Volume of sphere is = %.2f"%sphere_volume)