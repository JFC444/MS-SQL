from budget_logic import add_income, add_expense, get_overview

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Add income")
        print("2. Add expense")
        print("3. Show overview")
        print("4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            try:
                amount = float(input("Enter income amount: "))
                add_income(amount)
                print("Income added.")
            except Exception as e:
                print(e)
        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: "))
                add_expense(amount)
                print("Expense added.")
            except Exception as e:
                print(e)
        elif choice == "3":
            total_income, total_expenses, balance = get_overview()
            print(f"Total income: {total_income:.2f}")
            print(f"Total expenses: {total_expenses:.2f}")
            print(f"Balance: {balance:.2f}")
            if balance < 0:
                print("Warning: Budget exceeded!")
        elif choice == "4":
            print("Program exited.")
            break
        else:
            print("Invalid choice!")