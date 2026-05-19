# This program is to calculate BMI of a person.
# the height and the weight is in (meter) and (kg) respectively.
weight = float(input("Enter you weight(in kg): "))
height = float(input("Enter your height (in m): "))

bmi = weight/(height**2)

print("your BMI is = ",bmi)

if 16<=bmi<=25 : print("You have a HEALTHY BMI and A HEALTHY BODY maintain it") #this is an compliment

else : print("you have a highy BMI, consult to a doctor")
