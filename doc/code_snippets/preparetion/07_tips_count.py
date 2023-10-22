
# Input meal price, tip percent, and tax percent
meal_price = float(input("Enter the meal price: "))
tip_percent = int(input("Enter the tip percent: "))
tax_percent = int(input("Enter the tax percent: "))

# Calculate the tip and tax amounts
tip_amount = meal_price * (tip_percent / 100)
tax_amount = meal_price * (tax_percent / 100)

# Calculate the total cost of the meal
total_cost = meal_price + tip_amount + tax_amount

# Round the total cost to the nearest integer
rounded_total_cost = round(total_cost)

# Print the rounded total cost
print("The total cost of the meal is:", rounded_total_cost)