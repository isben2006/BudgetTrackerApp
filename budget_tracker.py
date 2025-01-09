
import csv
from datetime import datetime

DATA_FILE = "expenses.csv"

def add_expense(date, category, description, amount):
    """ adds an expense to DATA_FILE 
    """
    expense = [date, category, description, float(amount)]
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)
    print("Expense added successfully!")
    
def view_expenses():
    """ displays all the expenses
    """
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("Date\t\tCategory\tDescription\tAmount")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("No expenses found. Add some first!")
        
def monthly_summary(month, year):
    """ displays a summary of a specific month expenses
    """
    try:
        total = 0
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                expense_date = datetime.strptime(row[0], "%Y-%m-%d")
                if expense_date.month == month and expense_date.year == year:
                    total += float(row[3])
        print(f"Total spending for {month}/{year}: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses found. Add some first!")
        
def main():
    """ displays the main menu to the user
    """
    print("Welcome to Budget Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Rent): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(date, category, description, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2025): "))
            monthly_summary(month, year)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()