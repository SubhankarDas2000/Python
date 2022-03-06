#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

First_Name=str(input("Enter your first name: "))
Last_Name=str(input("Enter your last name: "))
Full_Name=(First_Name + " "+ Last_Name)
print("Your full name is: ",Full_Name)

print("Your full name in reverse order is: ",Full_Name[::-1])
