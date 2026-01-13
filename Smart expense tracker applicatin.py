import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Expense:
    def __init__(self, amount, category, note):
        self.amount = amount
        self.category = category
        self.note = note



class ExpenseTracker:
    def __init__(self):
        self.expenses = []  

    def add_expense(self):
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Invalid amount! Try again.")
            return
        
        category = input("Enter category (Food, Travel, Shopping, Other): ")
        note = input("Enter note/description: ")

        expense = Expense(amount, category, note)
        self.expenses.append(expense)

        print("Expense added successfully!\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses added yet.\n")
            return
        
        print("\n--- Expense List ---")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. ₹{e.amount} | {e.category} | {e.note}")
        print()

    def generate_dataframe(self):
        data = {
            "Amount": [e.amount for e in self.expenses],
            "Category": [e.category for e in self.expenses],
            "Note": [e.note for e in self.expenses]
        }
        df = pd.DataFrame(data)
        return df

    def total_expense(self):
        if not self.expenses:
            print("No expenses to calculate.\n")
            return
        amounts = np.array([e.amount for e in self.expenses])
        print(f"\nTotal Expense = ₹{amounts.sum():.2f}\n")

    def visualize_expenses(self):
        if not self.expenses:
            print("Add expenses before visualization.\n")
            return
        
        df = self.generate_dataframe()

        print("\nGenerating charts...")

        # Bar Plot - Category vs Amount
        sns.barplot(x="Category", y="Amount", data=df)
        plt.title("Expenses by Category")
        plt.show()

        # Pie Chart
        df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Expense Distribution")
        plt.ylabel("")
        plt.show()



def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== SMART EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expense")
        print("4. Visualize Expenses Graphically")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expense()

        elif choice == "4":
            tracker.visualize_expenses()

        elif choice == "5":
            df = tracker.generate_dataframe()
            df.to_csv("expenses.csv", index=False)
            print("Saved to expenses.csv successfully.\n")

        elif choice == "6":
            print("Thank you! Exiting application.")
            break

        else:
            print("Invalid choice! Try again.\n")

main()