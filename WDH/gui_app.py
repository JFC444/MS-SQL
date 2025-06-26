import tkinter as tk
from tkinter import messagebox, scrolledtext
from budget_logic import add_income, add_expense, get_overview, income_list, expense_list

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Management")

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
            add_income(amount)
            description = self.desc_var.get()
            income_list[-1] = (amount, description)
            self.entries.insert(tk.END, f"+ {amount:.2f} €: {description}\n")
            self.update_overview()
        except Exception as e:
            messagebox.showwarning("Error", str(e))

    def add_expense(self):
        try:
            amount = float(self.amount_var.get())
            add_expense(amount)
            description = self.desc_var.get()
            expense_list[-1] = (amount, description)
            self.entries.insert(tk.END, f"- {amount:.2f} €: {description}\n")
            self.update_overview()
        except Exception as e:
            messagebox.showwarning("Error", str(e))

    def update_overview(self):
        total_income, total_expenses, balance = get_overview()
        text = (f"Total income: {total_income:.2f} €\n"
                f"Total expenses: {total_expenses:.2f} €\n"
                f"Balance: {balance:.2f} €")
        if balance < 0:
            text += "\nWarning: Budget exceeded!"
        self.overview.config(text=text)