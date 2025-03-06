# Pizza Order Practice  

# Congratulations! You've got a job at Python Pizza! Your first task is to build an automatic pizza order program.  
# Based on a user's order, work out their final bill. Use the input() function to get the user's preferences  
# and then add up the total for their order to tell them how much they have to pay.  

# Small pizza (S): $15  
# Medium pizza (M): $20  
# Large pizza (L): $25  

# Add pepperoni for small pizza (Y or N): +$2  
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for small pizza (Y or N): +$1  
print("Welcome to Python Pizza Deliveries!")  
size = input("What size pizza do you want? S, M, or L: ")  
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")  
extra_cheese = input("Do you want extra cheese? Y or N: ") 

# TODO: Work out how much they need to pay based on their size choice.  
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")


# TODO: Work out how much to add to their bill based on their pepperoni choice.  
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# TODO: Work out their final amount based on whether they want extra cheese.  
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
