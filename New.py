# Create an empty dictionary to store expenses
expenses = {}

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")

    # Create an expense entry
    expense = {"Date": date, "Category": category, "Amount": amount, "Description": description}

    # Add the expense to the dictionary
    expenses[date] = expense

    print("Expense added successfully!")

# Function to display all expenses
def display_expenses():
    if not expenses:
        print("No expenses to display.")
    else:
        print("Date        | Category  | Amount    | Description")
        print("-----------------------------------------------------")
        for date, expense in expenses.items():
            print(f"{expense['Date']} | {expense['Category']} | ${expense['Amount']:.2f}   | {expense['Description']}")

# Main menu
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        display_expenses()
    elif choice == '3':
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")
