import csv

class ExpenseTracker:
    def __init__(self, file_path):
        """
        Initialize the ExpenseTracker with a file path for data storage.

        Args:
            file_path (str): Path to the CSV file to store expenses.
        """
        self.file_path = file_path
        self.expenses = []

    def add_expense(self, item, amount):
        """
        Add an expense to the tracker.

        Args:
            item (str): The item or description of the expense.
            amount (float): The amount of the expense.

        Returns:
            None
        """
        self.expenses.append({'item': item, 'amount': amount})
        self._save_to_csv()

    def total_expenses(self):
        """
        Calculate the total expenses.

        Returns:
            float: Total amount of expenses.
        """
        total = sum(item['amount'] for item in self.expenses)
        return total

    def list_expenses(self):
        """
        List all expenses.

        Returns:
            None
        """
        for expense in self.expenses:
            print(f"{expense['item']}: ${expense['amount']}")

    def _save_to_csv(self):
        """
        Save expenses to the CSV file.
        
        Returns:
            None
        """
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['item', 'amount'])
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

    def load_from_csv(self):
        """
        Load expenses from the CSV file.
        
        Returns:
            None
        """
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append({'item': row['item'], 'amount': float(row['amount'])})
        except FileNotFoundError:
            # If the file doesn't exist, it will be created when adding expenses.
            pass

def main():
    """
    Main function to run the expense tracker program.
    
    Returns:
        None
    """
    file_path = 'expenses.csv'
    tracker = ExpenseTracker(file_path)
    tracker.load_from_csv()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(item, amount)
            print("Expense added successfully!")

        elif choice == '2':
            print("\nList of Expenses:")
            tracker.list_expenses()

        elif choice == '3':
            total = tracker.total_expenses()
            print(f"\nTotal Expenses: ${total}")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
