# Logical Operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# Set ticket price based on age 
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")    
    elif age >= 45 and age <=55:# Free ride for people between 45 and 55
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else: 
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want to have a photo taken? Type Y for Yes and N for No.")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")