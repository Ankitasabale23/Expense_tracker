import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

    category = input("Enter category (Food/Travel/Bills/Other): ").strip()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in rupees: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n========== ALL EXPENSES ==========")
    for expense in expenses:
        print(
            f"Date: {expense['Date']} | "
            f"Category: {expense['Category']} | "
            f"Description: {expense['Description']} | "
            f"Amount: Rs. {float(expense['Amount']):.2f}"
        )


def show_summary():
    category_totals = {}
    total_spending = 0.0
    count = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            amount = float(expense["Amount"])
            category = expense["Category"]

            total_spending += amount
            count += 1
            category_totals[category] = (
                category_totals.get(category, 0) + amount
            )

    if count == 0:
        print("No expenses available for summary.")
        return

    print("\n========== SPENDING SUMMARY ==========")
    print(f"Number of expenses: {count}")
    print(f"Total spending: Rs. {total_spending:.2f}")

    print("\nCategory-wise spending:")
    for category, total in category_totals.items():
        print(f"{category}: Rs. {total:.2f}")

    print("======================================")


def main():
    initialize_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Spending Summary")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 4.")


if __name__ == "__main__":
    main()