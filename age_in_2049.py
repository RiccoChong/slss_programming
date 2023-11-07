# Age_in_2049_program
# Ricco Chong
# Block: B

# Ask the user what age they are
# Input the information
print("HEY, i will help calculate your age in 2049! ")

age = [
    "First, how old are you? "
]

for question in age:
    print(question)

# Output what age they will be in 2049
user_age = int(input().strip(",.?! "))
total_age = user_age + 26

print(f"You will be {total_age} in 2049")