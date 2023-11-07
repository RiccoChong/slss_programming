# McDonald's program
# Name: Ricco Chong
# Date: Nov 6 2023

# introduce the bot to the user
print("Hello! Welcome to McDonald's, i'm Bob and i'll be taking your order!")

# Ask the user questions and input their answer
burger = input("Would you like a burger for $5?  (Yes/No)").lower().strip("!?,.")
fries = input ("Would you like to add fries to your meal for 3$?  (Yes/No)").lower().strip("!?,.")

# Give different answers depending on the user's answer
total_price = 0
one_burger = 5
one_fries = 3
none = 0

if burger == "yes":
    total_price += one_burger
elif fries == "yes":
    total_price += one_fries
else:
    none += total_price

# Input 14% tax onto the final frice
# Print the final price
print(total_price * 0.14)
