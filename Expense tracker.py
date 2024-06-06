import datetime

class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.date.today()

    def __repr__(self):
        return f"{self.date} - {self.category}: ${self.amount} ({self.description})"
    
expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date() if date_input else None

    expense = Expense(amount, category, description, date)
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(expense)


def filter_expenses():
    category = input("Enter category to filter by (or leave blank): ")
    start_date_input = input("Enter start date (YYYY-MM-DD) or leave blank: ")
    end_date_input = input("Enter end date (YYYY-MM-DD) or leave blank: ")

    filtered = expenses
    if category:
        filtered = [e for e in filtered if e.category == category]
    if start_date_input:
        start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()
        filtered = [e for e in filtered if e.date >= start_date]
    if end_date_input:
        end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d").date()
        filtered = [e for e in filtered if e.date <= end_date]

    if not filtered:
        print("No matching expenses found.")
        return

    for expense in filtered:
        print(expense)

def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_expenses()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
