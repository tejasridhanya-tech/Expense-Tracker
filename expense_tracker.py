# Expense Tracker
# Mini Project using Lists and Calculations

expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Display Total Spending")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append([name, amount])
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpense List")
            print("---------------------------")
            for expense in expenses:
                print(expense[0], " - ₹", expense[1])

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense[1]

        print("\nTotal Spending = ₹", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice.")
