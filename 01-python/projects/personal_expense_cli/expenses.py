from storage import save_expenses

def add_expense(expenses):

    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter expense descripton: ")
    date = input("Enter Date(yyyy-mm-dd) : ")

    expense = {
        "amount" : amount,
        "category": category,
        "description": description, 
        "date":date
    }
    expenses.append(expense) 

    save_expenses(expenses)
    print("\n Expense added Successfully!")
    print("Your expenses: ", expenses)


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return 
    print("\n================ Expense History =================")

    for index, expense in enumerate(expenses, start=1):

        print(f"\nExpense    : {index}")
        print(f"Amount       :  ₹{expense['amount']:.2f}")
        print(f"Category     : {expense['category']}")
        print(f"Description  : {expense['description']}")
        print(f"Date         : {expense['date']}")
        print("--------------------------")

def view_totalExpenses(expenses):
    if not expenses:
        print("\nNo expenses found")
        return 
    

    total = 0
    for expense in expenses:
        total += expense['amount']

    print(f"\n============ TOTAL: {total}")
    print("--------------------------")


def category_wise_summary(expenses):
    category_total = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    print(category_total)


def delete_expenses(expenses):
    if not expenses:
            print("\nNo expenses found")
            return 

    view_expenses(expenses)
    to_delete = int(input("Enter what expense to delete"))

    if 1<= to_delete <= len(expenses):
        index = to_delete -1

        delete_expense = expenses.pop(index)

        save_expenses(expenses)
        print("\nExpense deleted successfully!")
        print("Deleted expense:", delete_expense)
    else:
        print("\nInvalid expense number.")