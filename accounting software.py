class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense):
        self.expenses.remove(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]


def main():
    tracker = ExpenseTracker()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter date (e.g., DD/MM/YYYY): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))

            expense = Expense(date, category, description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully!")

        elif choice == "2":
            print("Select the expense to remove:")
            for index, expense in enumerate(tracker.expenses):
                print(f"{index+1}. {expense.description} - {expense.amount}")

            selection = int(input("Enter the expense number to remove: "))
            if 1 <= selection <= len(tracker.expenses):
                expense = tracker.expenses[selection - 1]
                tracker.remove_expense(expense)
                print("Expense removed successfully!")
            else:
                print("Invalid expense number.")

        elif choice == "3":
            total_expenses = tracker.get_total_expenses()
            print(f"Total expenses: rs{total_expenses:.2f}")

        elif choice == "4":
            category = input("Enter the category: ")
            expenses = tracker.get_expenses_by_category(category)
            print(f"Expenses under category '{category}':")
            for expense in expenses:
                print(f"{expense.date} - {expense.description}: ${expense.amount:.2f}")

        elif choice == "5":
            print("Exiting Expense Tracker...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
