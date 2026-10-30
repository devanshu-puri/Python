from storage import load_expenses

from expenses import add_expense, view_expenses, view_totalExpenses, category_wise_summary,delete_expenses

print("====================================")
print("         Personal Expense Tracker    ")
print("=====================================")

menu = {
    "1": "Add Expense",
    "2": "View All Expenses",
    "3": "View Total Expenses",
    "4": "Category-wise Summary",
    "5": "Delete Expense",
    "6": "Exit"
}

expenses = load_expenses()

while True:
    print("\n============MAIN MENU==================")

    for key,value in menu.items():
        print(f"{key}. {value}")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        view_totalExpenses(expenses)

    elif choice == "4":
        category_wise_summary(expenses)

    elif choice == "5":
        delete_expenses(expenses)

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")

