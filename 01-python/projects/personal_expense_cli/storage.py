import json
import os

def load_expenses():
    with open("data/expenses.json", "r") as file:
        expenses = json.load(file)
    return expenses 

def save_expenses(expenses):
    print("Saving to:", os.path.abspath("data/expenses.json"))
    with open("data/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Saved successfully!")
    
