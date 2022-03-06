# Write a Python program which accepts the radius of a circle from the user and compute the area.

r=float(input("Enter the radious of circle: "))
area=3.142*r*r
if r>0:
    print("The area of circle is : ", area)
else:
    print("Given radious is invalid!!!!")

    
