import datetime
import calendar


class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"


def main():
    print("📊 Welcome to the Expense Tracker!")
    file_path = "expenses.csv"
    monthly_budget = 2000

    # Capture and record a new expense
    new_expense = gather_expense_details()
    record_expense(new_expense, file_path)

    # Analyze and summarize expenses from the file
    generate_summary(file_path, monthly_budget)


def gather_expense_details():
    print("💡 Log a New Expense")
    name = input("What is the expense for? ")
    amount = float(input("Enter the cost: "))
    categories = [
        "🍽️ Food",
        "🏠 Housing",
        "🚌 Transportation",
        "🎉 Entertainment",
        "✨ Other",
    ]

    while True:
        print("Choose a category for your expense:")
        for idx, category in enumerate(categories, start=1):
            print(f"  {idx}. {category}")
        
        try:
            selection = int(input(f"Select a category [1-{len(categories)}]: ")) - 1
            if 0 <= selection < len(categories):
                selected_category = categories[selection]
                return Expense(name=name, category=selected_category, amount=amount)
            else:
                print("❌ Invalid selection. Try again!")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def record_expense(expense, file_path):
    print(f"📝 Saving {expense} to {file_path}")
    with open(file_path, "a") as file:
        file.write(f"{expense.name},{expense.amount},{expense.category}\n")


def generate_summary(file_path, budget):
    print("📊 Generating Expense Summary")
    expenses = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                name, amount, category = line.strip().split(",")
                expenses.append(Expense(name, category, float(amount)))
    except FileNotFoundError:
        print(f"❌ No expense file found at {file_path}. Starting fresh.")
        return

    # Calculate totals by category
    category_totals = {}
    for expense in expenses:
        if expense.category in category_totals:
            category_totals[expense.category] += expense.amount
        else:
            category_totals[expense.category] = expense.amount

    # Display totals by category
    print("📂 Expenses by Category:")
    for category, total in category_totals.items():
        print(f"  {category}: ${total:.2f}")

    # Calculate and display overall totals
    total_spent = sum(exp.amount for exp in expenses)
    remaining_budget = budget - total_spent
    print(f"💰 Total Spent: ${total_spent:.2f}")
    print(f"💸 Remaining Budget: ${remaining_budget:.2f}")

    # Estimate daily spending budget
    today = datetime.datetime.now()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    days_left = days_in_month - today.day
    if days_left > 0:
        daily_budget = remaining_budget / days_left
        print(f"📅 Daily Budget for Remaining {days_left} Days: ${daily_budget:.2f}")
    else:
        print("📅 The month is over! Time to review next month's budget.")


if __name__ == "__main__":
    main()
