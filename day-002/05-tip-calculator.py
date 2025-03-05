print("Welcome to the tip calculator!")  # Mensagem antes das entradas

total = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))  # Inteiro

total_bill = total + total * (tip / 100)
split_amount = round(total_bill / total_people, 2)

print(f"Each person should pay: ${split_amount}")

