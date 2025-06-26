income_list = []
expense_list = []

def add_income(amount):
    if amount <= 0:
        raise ValueError("Only positive numbers allowed!")
    income_list.append(amount)

def add_expense(amount):
    if amount <= 0:
        raise ValueError("Only positive numbers allowed!")
    expense_list.append(amount)

def get_overview():
    total_income = sum(income_list)
    total_expenses = sum(expense_list)
    balance = total_income - total_expenses
    return total_income, total_expenses, balance