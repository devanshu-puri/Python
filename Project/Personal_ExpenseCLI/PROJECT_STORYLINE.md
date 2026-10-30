# Personal Expense Tracker --- Project Storyline

> A development journal documenting how the Personal Expense Tracker
> evolved from a small CLI menu into a modular application with
> persistent storage and multiple expense-management features.


## Project overview

**Project:** Personal Expense Tracker (CLI)\
**Language:** Python\
**Storage:** JSON file\
**Interface:** Command-line menu

### Final project structure

``` text
Personal_ExpenseCLI/
│
├── data/
│   └── expenses.json
│
├── main.py
├── expenses.py
├── storage.py
├── features.txt
└── PROJECT_STORYLINE.md
```

-   `main.py` runs the application, displays the menu, and routes the
    user's choice to the appropriate function.
-   `expenses.py` contains the expense-related operations.
-   `storage.py` contains the functions responsible for loading and
    saving expense data.
-   `data/expenses.json` stores expense records between program runs.
-   `About.txt` about the project


# Phase 1 The first working CLI prototype

## 1.1 Starting point: understand the application

Begin with `main.py` as the central file. It displayed the
application title and a menu containing the planned operations:

1.  Add Expense
2.  View All Expenses
3.  View Total Expenses
4.  Category-wise Summary
5.  Delete Expense
6.  Exit

At this point, some options were only placeholders. That was
intentional: the first milestone was to establish the application's flow
before implementing every feature.


## 1.2 Create the in-memory expense list

We used a Python list to hold expense records while the program was
running:

``` python
expenses = []
```

An expense was represented as a dictionary:

``` python
expense = {
    "amount": 500,
    "category": "food",
    "description": "Lunch",
    "date": "2026-10-27"
}
```

This gave us a useful structure:

-   The **list** stores multiple expenses.
-   Each **dictionary** represents one expense.
-   Dictionary keys describe the fields of an expense.

Conceptually:

``` python
expenses = [
    {
        "amount": 500,
        "category": "food",
        "description": "Lunch",
        "date": "2026-10-27"
    },
    {
        "amount": 1000,
        "category": "electronics",
        "description": "Keyboard",
        "date": "2026-10-30"
    }
]
```

## 1.3 Implement the first operations

We started implementing the basic expense operations:

-   Add an expense to the list.
-   Display all expenses.
-   Calculate the total amount spent.

The key list operation for adding a record was:

``` python
expenses.append(expense)
```


### Limitation discovered

The expense list existed only in the program's memory. When the
application stopped, the list was lost. We would solve that later.

------------------------------------------------------------------------

# Phase 2  Separate the application logic into modules

## 2.1 Why did we split the code?

As the project gained functionality, keeping every function inside
`main.py` made the file responsible for too many things.

We therefore introduced a separate file:

``` text
expenses.py
```

The aim was to give each file a clearer responsibility.

-   `main.py` would manage the application flow and menu.
-   `expenses.py` would contain the functions that perform expense
    operations.


## 2.2 Move expense operations into `expenses.py`

We moved the feature functions into `expenses.py`, including:

``` python
def add_expense(expenses):
    ...
```

``` python
def view_expenses(expenses):
    ...
```

``` python
def view_totalExpenses(expenses):
    ...
```

The names above reflect the naming used during the project. A future
cleanup could standardize `view_totalExpenses` to `view_total_expenses`.

## 2.3 Import the functions into `main.py`

The main file then imported the functions it needed:

``` python
from expenses import (
    add_expense,
    view_expenses,
    view_totalExpenses
)
```

When the user selected a menu option, `main.py` called the corresponding
function:

``` python
if choice == "1":
    add_expense(expenses)
elif choice == "2":
    view_expenses(expenses)
elif choice == "3":
    view_totalExpenses(expenses)
```

An important design detail was that `main.py` passed the same `expenses`
list into each function. The functions worked with that shared list
rather than creating a separate list for each operation.

## 2.4 What each file was responsible for

### `main.py`

-   Display the title and menu.
-   Read the user's menu choice.
-   Call the appropriate feature function.
-   Exit the application when requested.

### `expenses.py`

-   Ask for expense details.
-   Create expense dictionaries.
-   Add records to the list.
-   Display records.
-   Calculate totals.


## 2.5 What Phase 2 taught us

-   How to split code across Python modules.
-   How `import` makes functions available in another file.
-   The difference between defining a function and calling it.
-   How to pass a list into a function.
-   Why a file should have a focused responsibility.

### Limitation discovered

Although the code was now better organized, the records were still
stored only in memory. Modular code does not automatically make data
persistent.

------------------------------------------------------------------------

# Phase 3 --- Add persistent storage with JSON

## 3.1 The problem: data disappeared after exit

We noticed that the program could display expenses during a run, but the
data did not reliably survive after closing and reopening the
application.

The reason was:

``` python
expenses = []
```

This creates a fresh empty list whenever the program starts. The
application needed a way to:

1.  Load previously saved expenses when it starts.
2.  Save the updated list when an expense is added or deleted.

This led to the introduction of file-based storage.

## 3.2 Introduce a data folder and JSON file

We created:

``` text
data/
└── expenses.json
```

The initial contents of `expenses.json` were:

``` json
[]
```

An empty JSON array represents an empty list of expenses.

We chose JSON because it can represent lists and dictionaries in a
readable format and Python provides a built-in `json` module for working
with it.

## 3.3 Introduce `storage.py`

Instead of placing file-reading and file-writing code inside the feature
functions, we created a separate module:

``` text
storage.py
```

Its responsibility was to handle persistence.

The initial implementation was:

``` python
import json

def load_expenses():
    with open("data/expenses.json", "r") as file:
        expenses = json.load(file)
    return expenses


def save_expenses(expenses):
    with open("data/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
```

### What the functions do

**`load_expenses()`**

-   Opens the JSON file in read mode (`"r"`).
-   Uses `json.load()` to convert JSON data into Python data.
-   Returns the loaded list.

**`save_expenses(expenses)`**

-   Opens the JSON file in write mode (`"w"`).
-   Uses `json.dump()` to write the Python list as JSON.
-   Uses `indent=4` to make the file easier for a person to read.

## 3.4 Make a small change in `main.py`

Previously, `main.py` created a new empty list:

``` python
expenses = []
```

We changed it to load the saved records:

``` python
from storage import load_expenses

expenses = load_expenses()
```

This is performed once when the application starts. The returned list is
then passed to the feature functions.

## 3.5 Make a small change in `expenses.py`

We imported the save function:

``` python
from storage import save_expenses
```

Inside `add_expense()`, after creating the dictionary, we added it to
the list and saved the updated list:

``` python
expenses.append(expense)
save_expenses(expenses)
```

The order matters:

1.  Create the expense dictionary.
2.  Append it to the list.
3.  Save the updated list.

During debugging, we found that the `expenses.append(expense)` line had
initially been missed. The program created the dictionary but saved the
unchanged, empty list. Adding the missing line fixed the issue.

The same persistence principle must be followed when deleting an
expense: modify the list first, then save the updated list.

## 3.6 Debugging the file path

We encountered a `FileNotFoundError` even though the folder structure
looked correct.

The cause was the current working directory. Python was launched with:

``` text
C:\CodeSpace\Project
```

But the project and its `data` folder were inside:

``` text
C:\CodeSpace\Project\Personal_ExpenseCLI
```

A relative path such as:

``` python
open("data/expenses.json", "r")
```

is resolved relative to the process's current working directory. It is
not automatically resolved relative to the location of `storage.py`.

We diagnosed this by printing:

``` python
import os
print(os.getcwd())
```

We then configured the VS Code Code Runner working-directory setting to
use the directory of the file being executed, so that the relative path
resolved as expected.

**Important lesson:** A correct relative path can still fail if the
program is launched from a different working directory.

For a later robustness improvement, we can make the storage path
independent of the launch directory by deriving it from `__file__`. We
deliberately kept the initial implementation simple while learning the
underlying concept.

## 3.7 What Phase 3 taught us

-   The difference between in-memory data and persistent data.
-   How to read and write JSON using Python's `json` module.
-   How to use `open()` and file modes.
-   Why `json.load()` and `json.dump()` are different.
-   Why the order of append and save operations matters.
-   How a working directory affects relative file paths.
-   How separate modules can cooperate: `main.py` loads, feature
    functions modify, and `storage.py` persists.

### Toddler-level explanation

The Python list is like a whiteboard. You can write expenses on it while
the program is running.

The JSON file is like a notebook. When the program starts, it reads the
notebook. When the list changes, it copies the updated information into
the notebook.

Without saving to the notebook, the whiteboard disappears when the
program closes.

------------------------------------------------------------------------

# Phase 4 --- Add category-wise summary

## 4.1 The requirement

After adding, viewing, and totaling expenses, we wanted to answer a more
useful question:

**How much money have we spent in each category?**

For example, if the records are:

  Category        Amount
  ------------- --------
  food              ₹500
  electronics     ₹1,000
  food              ₹300
  electronics     ₹2,000

The summary should be:

``` text
========== CATEGORY-WISE SUMMARY ==========

Food           : ₹800.00
Electronics    : ₹3000.00
```

## 4.2 Understand the data structure

The original `expenses` variable is a list of dictionaries. We loop
through the list to inspect one expense at a time:

``` python
for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
```

We then introduced a second dictionary to accumulate totals:

``` python
category_totals = {}
```

In this new dictionary:

-   The category is the key.
-   The accumulated amount is the value.

## 4.3 Group and accumulate

The central logic is:

``` python
if category in category_totals:
    category_totals[category] += amount
else:
    category_totals[category] = amount
```

If the category already exists, add to its current total. Otherwise,
create a new key with the first amount.

For the example above, the dictionary develops like this:

``` python
{}
{"food": 500}
{"food": 500, "electronics": 1000}
{"food": 800, "electronics": 1000}
{"food": 800, "electronics": 3000}
```

We can then display the summary by iterating over the dictionary:

``` python
for category, total in category_totals.items():
    print(f"{category.capitalize():<15}: ₹{total:.2f}")
```

We also considered the empty-list case so that the program can show a
useful message when there are no expenses.

## 4.4 Connect the feature to the menu

We added the function to the imports in `main.py` and replaced the
placeholder for option 4 with a function call.

This preserved the same architecture: `main.py` routes the user's
choice, while `expenses.py` performs the calculation.

## 4.5 What Phase 4 taught us

-   How to group records by a shared field.
-   How to use a dictionary as an accumulator.
-   How to check for an existing dictionary key with `in`.
-   How to update an existing value.
-   How to use `.items()` to loop through dictionary key-value pairs.
-   How to reuse a data structure for a new feature without changing the
    stored record format.

### Toddler-level explanation

Imagine a separate piggy bank for every category. Each time you
encounter a food expense, put its amount in the Food piggy bank. Each
electronics expense goes into the Electronics piggy bank. At the end,
count the money in each bank.

------------------------------------------------------------------------

# Phase 5 --- Add delete expense

## 5.1 The requirement

The application could add and display expenses, but users also needed to
remove a record.

We decided to keep the existing list-of-dictionaries structure. We did
**not** convert the list into a dictionary of dictionaries just to make
deletion possible.

The displayed expense number is generated when the list is displayed. It
is not a permanent ID stored inside the expense.

## 5.2 Display numbering with `enumerate()`

Our display function uses:

``` python
for index, expense in enumerate(expenses, start=1):
    print(f"Expense: {index}")
```

`enumerate()` gives each record a temporary display number starting at
1.

Python list indices, however, start at 0:

    Number shown to the user   Python list index
  -------------------------- -------------------
                           1                   0
                           2                   1
                           3                   2

Therefore, when a user chooses an expense number, we convert it:

``` python
index = to_delete - 1
```

## 5.3 Remove and persist the record

The deletion flow is:

1.  Check whether the list is empty.
2.  Display the current expenses.
3.  Ask the user for the expense number.
4.  Check that the number is within the valid range.
5.  Convert the displayed number to a list index.
6.  Remove the record.
7.  Save the updated list to JSON.

The core operations are:

``` python
index = to_delete - 1
deleted_expense = expenses.pop(index)
save_expenses(expenses)
```

`pop(index)` removes the item at that position and returns the removed
dictionary.

Saving after the deletion is essential. Otherwise, the old record would
still be present in the JSON file and could return the next time the
application starts.

## 5.4 Connect deletion to `main.py`

We import the deletion function and call it when the user selects option
5:

``` python
elif choice == "5":
    delete_expense(expenses)
```

The storage module does not need a new deletion function. The feature
modifies the list, and the existing `save_expenses()` function writes
the updated list.

## 5.5 Current limitation to remember

The simple implementation validates the numeric range, but converting
input directly with `int()` can raise a `ValueError` if the user types
text such as `abc`.

We have identified this as an improvement for the input-validation
phase. A more advanced version could also use permanent unique IDs so
that an expense can be referenced independently of its current list
position.

## 5.6 What Phase 5 taught us

-   How to remove an item from a list with `pop()`.
-   How to map user-facing numbering to zero-based list indices.
-   How to validate a selection against `len(expenses)`.
-   How to save a deletion so it persists after restarting.
-   Why temporary display numbers and permanent record IDs are different
    concepts.

### Toddler-level explanation

Imagine three toys in a row. You label them 1, 2, and 3 for a person.
Python internally calls those positions 0, 1, and 2. If the person asks
to remove toy 2, convert that number to position 1, remove it, and
update the inventory notebook.

------------------------------------------------------------------------

# Current architecture --- How the pieces work together

``` text
                    USER
                     |
                     v
                  main.py
             (menu and control flow)
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Add/View   Summary    Delete
          \          |          /
           \         |         /
            v        v        v
                 expenses.py
             (expense operations)
                     |
                     v
                 storage.py
              (load and save)
                     |
                     v
             data/expenses.json
               (persistent data)
```

The application follows this broad flow:

1.  `main.py` calls `load_expenses()` when the application starts.
2.  The returned list is passed to feature functions.
3.  A feature function reads or modifies that list.
4.  When a feature changes the list, it calls `save_expenses()`.
5.  The JSON file stores the updated records for the next run.

## Responsibility summary

  File                   Main responsibility
  ---------------------- --------------------------------------------
  `main.py`              Menu, user choice, application flow
  `expenses.py`          Add, view, total, category summary, delete
  `storage.py`           Load and save expense data
  `data/expenses.json`   Persistent expense records

------------------------------------------------------------------------

# Development lessons --- The mindset behind the project

The most important part of this project is not the number of functions.
It is the sequence of problems we solved.

  ----------------------------------------------------------------------------
  What we noticed         Change we made               Why it mattered
  ----------------------- ---------------------------- -----------------------
  We needed a runnable    Built the menu in `main.py`  Established the
  starting point                                       application flow

  The main file was       Moved feature functions into Separated
  becoming crowded        `expenses.py`                responsibilities

  Data disappeared after  Added JSON storage           Made data persistent
  exit                                                 

  The JSON file could not Checked the working          Understood relative
  be found                directory                    paths

  A new expense was not   Added                        Ensured the updated
  being saved             `expenses.append(expense)`   list was persisted
                          before saving                

  We needed spending      Added a category accumulator Learned grouping and
  totals by category      dictionary                   aggregation

  Users needed to remove  Added deletion using `pop()` Completed the core
  records                 and saved afterward          CRUD-like operations
  ----------------------------------------------------------------------------

## A useful rule we followed

**Do not introduce a new file, abstraction, or technique just because it
is common in professional projects. Introduce it when the project has a
clear need for it.**

For example:

-   We did not start with three files. We started with a simple
    prototype.
-   We separated the feature logic when `main.py` became responsible for
    too much.
-   We introduced storage when we discovered that in-memory data was not
    enough.
-   We reused the storage functions when implementing deletion instead
    of creating unnecessary new file-handling code.

This is incremental development: build something small, observe its
limitations, and make the next change to solve a real problem.

------------------------------------------------------------------------

# Next improvement phases --- Not yet part of the completed core

The following are sensible next steps. They should be treated as future
work rather than assumed to be implemented already.

## Phase 6 --- Input validation

Potential improvements:

-   Reject non-numeric amounts.
-   Reject zero or negative expense amounts, if that is the chosen
    business rule.
-   Validate dates in `YYYY-MM-DD` format.
-   Reject blank categories and descriptions.
-   Handle non-numeric deletion choices without crashing.

## Phase 7 --- Storage and error handling

Potential improvements:

-   Handle a missing JSON file.
-   Handle an empty or malformed JSON file.
-   Make the storage path independent of the working directory.
-   Avoid losing existing data if a write fails.

## Phase 8 --- Code cleanup and maintainability

Potential improvements:

-   Standardize function names, for example `view_total_expenses`.
-   Use consistent formatting and messages.
-   Remove temporary debugging output.
-   Avoid duplicated code where a shared function is appropriate.
-   Add docstrings and comments where they clarify intent.

## Phase 9 --- Testing and documentation

Potential improvements:

-   Test every menu option.
-   Test empty-list cases.
-   Test invalid user input.
-   Test adding, deleting, exiting, and restarting.
-   Write a README with setup instructions, features, and example usage.
-   Add a few automated tests once the functions are stable.

------------------------------------------------------------------------

# Final milestone checklist

Use this checklist as the project evolves.

## Core functionality

-   [ ] Add an expense.
-   [ ] View all expenses.
-   [ ] Calculate total expenses.
-   [ ] Show category-wise totals.
-   [ ] Delete an expense.
-   [ ] Exit cleanly.

## Persistence

-   [ ] Load expenses when the application starts.
-   [ ] Save after adding an expense.
-   [ ] Save after deleting an expense.
-   [ ] Confirm records remain correct after restarting.

## Reliability and polish

-   [ ] Handle invalid numeric input.
-   [ ] Validate dates and required fields.
-   [ ] Handle missing or malformed storage data.
-   [ ] Test edge cases.
-   [ ] Write a project README.

------------------------------------------------------------------------

## Closing note

This project began as a simple menu and a list. It gradually became a
modular CLI application with JSON persistence and expense-management
features.

When revisiting the project, read the phases in order. Try to remember
the problem that existed before each change. That is the key lesson:
**good software is often built through a sequence of small,
understandable improvements---not by trying to design the final system
all at once.**
