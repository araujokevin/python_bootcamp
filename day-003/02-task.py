#Introducing the Modulo

#Check Odd or Even

#Prompt the user to enter a number and convert the input into an integer
number_to_check = int(input("What is the number you want to check?"))

#Use the modulus operator (%) to check if the number is odd or even
#If the remainder when divided by 2 is not zero (!= 0), the number is odd
if number_to_check % 2 != 0:
    #Print a message indicating that the number is odd
    print("This number is Odd!")
else:
    #If the remainder is zero, the number is even
    print("This number is Even")
