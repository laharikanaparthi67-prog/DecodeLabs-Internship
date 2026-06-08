total = 0  # accumulator to store total expenses

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == 'done':
        break

    # convert input to number and add to total
    total = total + float(expense)

print("\nTotal Spent:", total)