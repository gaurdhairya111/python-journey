#this is to calculate a compound interst progra using python
#imputs taken as are
"""
A = Total amount (including interest)
P = Principle interest (you satrted with)
T = time period of the loan
R = rate of interst (per year)
n = frequncy of the interest applied per year
"""

#a = float(input("Enter the amount you have taen as loan : "))
p = float(input("Enter the amount of the principle you have paid : "))
t = float(input("Enter the time period of the loan : "))
r = float(input("Enter the rate of interest : "))
n = int(input("ente the frequency of the increase in the rate of interest in a year : "))

l = n*t 
ci = p*((1+(r/n))**l)

print("Your compund interest is : ", ci)