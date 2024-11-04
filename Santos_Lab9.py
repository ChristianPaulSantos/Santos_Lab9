# Function to print a right-angled triangle of numbers
num_rows = int(input("Enter the number of rows: "))
number = 1

for i in range(1, num_rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()