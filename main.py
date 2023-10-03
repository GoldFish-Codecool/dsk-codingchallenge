count = int(input("How many number would you like to summerize? "))
sum = 0
for i in range(count):
  sum += int(input(f"Enter number {i+1}: "))

print(f"\nThe sum of the numbers is: {sum}")
