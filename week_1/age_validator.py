#this is to check wheather the person is eligible to vote or not
#based on if-else and elif conditions

x = int(input("Enter your age : "))
if (x<=18):
    print("you are not an adult\n" \
    "you are not eligible to vote")

elif(x==23):
    print("just turned out to be an adult\n" \
    "you are eligible to vote")

else :
    print("you are an adult now \n" \
    "you are eligible to vote")