
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox


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
    """ Fetches all expenses from the CSV file and returns them as a list """
    expenses = []
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(f"{row[0]} | {row[1]} | {row[2]} | ${float(row[3]):.2f}")  # Format each row and convert the amount to a float
    except FileNotFoundError:
        messagebox.showwarning("No Data", "No expenses found. Add some first!")
    return expenses  # Return the list of formatted expenses
        
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
        return f"Total spending for {month}/{year}: ${total:.2f}"
    except FileNotFoundError:
        return "No expenses found. Add some first!"
    
      
        
class BudgetTrackerApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")
        
        # Create and place widgets
        

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=2, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=2, column=1)

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.grid(row=3, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=3, column=1)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=4, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=4, column=1)

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=5, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.grid(row=6, column=0, columnspan=2)

        self.month_label = tk.Label(root, text="Month (1-12):")
        self.month_label.grid(row=7, column=0)
        self.month_entry = tk.Entry(root)
        self.month_entry.grid(row=7, column=1)

        self.year_label = tk.Label(root, text="Year (e.g., 2025):")
        self.year_label.grid(row=8, column=0)
        self.year_entry = tk.Entry(root)
        self.year_entry.grid(row=8, column=1)

        self.summary_button = tk.Button(root, text="Monthly Summary", command=self.show_monthly_summary)
        self.summary_button.grid(row=9, column=0, columnspan=2)

        self.transaction_listbox = tk.Listbox(root, width=50, height=10)
        self.transaction_listbox.grid(row=10, column=0, columnspan=2)

    def add_expense(self):
        """ Add expense based on the user input in the entry fields """
        date = self.date_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if date and category and description and amount:
            try:
                add_expense(date, category, description, amount)
                messagebox.showinfo("Success", "Expense added successfully!")
                self.clear_inputs()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def view_expenses(self):
        """ Display all expenses in the listbox """
        expenses = view_expenses()
        self.transaction_listbox.delete(0, tk.END) # Clear the Listbox before insterting new items
        for expense in expenses:
            self.transaction_listbox.insert(tk.END, expense) # Insert expense at the end of the listbox

    def show_monthly_summary(self):
        """ Show the monthly summary in a message box """
        try:
            month = int(self.month_entry.get())
            year = int(self.year_entry.get())
            summary = monthly_summary(month, year)
            messagebox.showinfo("Monthly Summary", summary)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid month and year.")
    

    def clear_inputs(self):
        """ Clear the input fields after adding an expense """
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        
if __name__ == "__main__":
   root = tk.Tk()
   app = BudgetTrackerApp(root)
   root.mainloop()