#Write a Python program to display the first and last colors from the following list.
values = input("Enter colors name separated by comma : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print("The first colour is : ",list[0])
print("The first colour is : ",list[-1])
