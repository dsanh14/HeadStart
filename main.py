import datetime
from database import create_tables, add_expense, add_income
from visualization import plot_expenses_by_category, plot_income_vs_expenses
from stock_data import get_stock_price

def main():
    # Create database tables if they don't exist
    create_tables()
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expenses by Category")
        print("4. View Income vs Expenses")
        print("5. Check Stock Price")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            source = input("Enter income source: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_income(date, source, amount, description)
            
        elif choice == '3':
            plot_expenses_by_category()
            
        elif choice == '4':
            plot_income_vs_expenses()
            
        elif choice == '5':
            symbol = input("Enter stock symbol (e.g., AAPL): ")
            stock_data = get_stock_price(symbol)
            if stock_data:
                print(f"\nStock: {stock_data['symbol']}")
                print(f"Price: ${stock_data['price']:.2f}")
                print(f"Change: ${stock_data['change']:.2f}")
                print(f"Change %: {stock_data['change_percent']}")
                
        elif choice == '6':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 