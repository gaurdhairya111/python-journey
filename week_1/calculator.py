#this program is to create a simple calculator that can perform basic arithmetic operations
#the user will be prompted to enter two numbers and the operation they want to perform
#the program will then perform the operation and display the result

a = float(input("enter the value of your first variable: "))
b = float(input("enter the value of the second variable: "))

# addition
addition = a+b

#subtraction
sub = a-b

#multiplication
multi = a*b

# division
div = a/b

# modulus
modulus = a%b

#floor division
floor_division = a//b

# exponent 
exo = a**b


print("Sum = ",addition,"\n") 
print("Subtraction =",sub,"\n")
print("Multiplication = ",multi,"\n")
print("Division = ",div,"\n")
print("modulus of the function is: ",modulus,"\n")
print("floor division: ",floor_division,"\n")
print("Exponent: ",exo,)
