'''''
Input the radius of the circle: 1.1
The area of the circle with radius 1.1 is:3.8013271108436504
'''''

x = float(input("Enter Radius of the Circle:  "))
from math import pi
area = pi*x**2
print("Area of the circle is: ")
print(area)









'''
# write a Python program to accept a filename from the user and print 
the extension of that.
'''
filename = input("Input the Filename: ")
f_extns = filename.split(".")

print("The extension of the file is : " + str(f_extns[-1]))
