#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n=int(input("Enter one integer value : "))
if n<0:
    print("It is an invalid input!!!!!")
else:
    n
    calculation=n+(n*n)+(n*n*n)+(n*n*n*n)
    print("The input is valid and the calculation is :",calculation)
