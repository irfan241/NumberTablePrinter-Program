"""
NumberTablePrinter Program

This program takes a number as input from the user
and prints its multiplication table from 1 to 10.
"""

# Ask the user to enter a number for the table
n = int(input("Enter a number to get table: "))

# Loop from 1 to 10 to generate the multiplication table
for i in range(1, 11):
    # Print the multiplication result in table format
    print(f"{n} x {i} = {n * i}")
