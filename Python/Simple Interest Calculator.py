'''
Assignment 4: Simple Interest Calculator
Write a program that calculates the simple interest for a given principal amount, rate of interest, and time period.
The formula for simple interest is: Simple Interest = (principal * rate * time) / 100.
Take principal ,rate , time from user.
'''
principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=int(input("Enter the time in year : "))
simple_int=(principal*rate*time)/100
print("The simple interest is: ",simple_int)
