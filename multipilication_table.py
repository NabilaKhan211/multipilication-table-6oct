# Veda Technology - Task 6
# Multiplication Table Generator

print("===== MULTIPLICATION TABLE =====")

try:
    number = int(input("Enter a number: "))
    limit = int(input("Enter the limit: "))
except ValueError :
    print("Please enter whole numbers only")
    exit()

if limit < 1:                                
    print("Limit must be at least 1")        
    exit()          

print(f"\nMultiplication Table of {number}")
print("-" * 30)

for i in range(1, limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")

print("-" * 30)
