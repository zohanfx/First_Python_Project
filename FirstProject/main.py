# Write your code here
print('''
Earned Amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80
''')

# Write your code here
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake
print("Income: ", income)

# Staffs expenses
print("Staff Expenses: ")
staff_expenses = input()

# Other expenses
print("Other Expenses: ")
other_expenses = input()

print("Net income: $" + str(income - int(staff_expenses) - int(other_expenses)))