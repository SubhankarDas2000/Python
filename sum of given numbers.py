#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))
third_num=int(input("Enter third number: "))
add=first_num+second_num+third_num
sum_sum=first_num*3
if first_num!=second_num:
    print("The sum of the given numbers is : ",add)

else:
    print("The sum of given numbers is : ",sum_sum)

