import tkinter as tk
from tkinter import messagebox, scrolledtext

income_list = []
expense_list = []

# --- Terminal Part ---

def add_income():
    try:
        amount = float(input("Enter income amount: "))
        if amount <= 0:
            print("Only positive numbers allowed!")
            return
        income_list.append(amount)
        print("Income added.")
    except ValueError:
        print("Invalid input!")

def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Only positive numbers allowed!")
            return
        expense_list.append(amount)
        print("Expense added.")
    except ValueError:
        print("Invalid input!")

def show_overview():
    total_income = sum(income_list)
    total_expenses = sum(expense_list)
    balance = total_income - total_expenses
    print(f"Total income: {total_income:.2f}")
    print(f"Total expenses: {total_expenses:.2f}")
    print(f"Balance: {balance:.2f}")
    if balance < 0:
        print("Warning: Budget exceeded!")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Add income")
        print("2. Add expense")
        print("3. Show overview")
        print("4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_overview()
        elif choice == "4":
            print("Program exited.")
            break
        else:
            print("Invalid choice!")

# --- Tkinter GUI Part ---

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Management")

        self.income_list = []
        self.expense_list = []

        self.amount_var = tk.StringVar()
        self.desc_var = tk.StringVar()

        tk.Label(root, text="Amount:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1)
        tk.Label(root, text="Description:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.desc_var).grid(row=1, column=1)

        tk.Button(root, text="Add income", command=self.add_income).grid(row=2, column=0)
        tk.Button(root, text="Add expense", command=self.add_expense).grid(row=2, column=1)

        self.overview = tk.Label(root, text="", justify="left")
        self.overview.grid(row=3, column=0, columnspan=2, sticky="w")

        self.entries = scrolledtext.ScrolledText(root, width=40, height=10)
        self.entries.grid(row=4, column=0, columnspan=2)

        self.update_overview()

    def add_income(self):
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                messagebox.showwarning("Error", "Only positive numbers allowed!")
                return
            description = self.desc_var.get()
            self.income_list.append((amount, description))
            self.entries.insert(tk.END, f"+ {amount:.2f} €: {description}\n")
            self.update_overview()
        except ValueError:
            messagebox.showwarning("Error", "Invalid input!")

    def add_expense(self):
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                messagebox.showwarning("Error", "Only positive numbers allowed!")
                return
            description = self.desc_var.get()
            self.expense_list.append((amount, description))
            self.entries.insert(tk.END, f"- {amount:.2f} €: {description}\n")
            self.update_overview()
        except ValueError:
            messagebox.showwarning("Error", "Invalid input!")

    def update_overview(self):
        total_income = sum(a for a, _ in self.income_list)
        total_expenses = sum(a for a, _ in self.expense_list)
        balance = total_income - total_expenses
        text = (f"Total income: {total_income:.2f} €\n"
                f"Total expenses: {total_expenses:.2f} €\n"
                f"Balance: {balance:.2f} €")
        if balance < 0:
            text += "\nWarning: Budget exceeded!"
        self.overview.config(text=text)

# --- Execution ---

if __name__ == "__main__":
    mode = input("Choose mode (terminal/gui): ").strip().lower()
    if mode == "terminal":
        main()
    elif mode == "gui":
        root = tk.Tk()
        app = BudgetApp(root)
        root.mainloop()
    else:
        print("Invalid mode.")

