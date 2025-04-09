import matplotlib.pyplot as plt
import pandas as pd
from database import get_expenses_by_category, get_income_vs_expenses

def plot_expenses_by_category():
    """Create a bar chart of expenses by category"""
    data = get_expenses_by_category()
    if not data:
        print("No expense data available")
        return
    
    df = pd.DataFrame(data, columns=['Category', 'Amount'])
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Amount'])
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_income_vs_expenses():
    """Create a line chart comparing income and expenses over time"""
    data = get_income_vs_expenses()
    if not data:
        print("No income/expense data available")
        return
    
    df = pd.DataFrame(data, columns=['Month', 'Income', 'Expenses'])
    plt.figure(figsize=(12, 6))
    plt.plot(df['Month'], df['Income'], label='Income', marker='o')
    plt.plot(df['Month'], df['Expenses'], label='Expenses', marker='o')
    plt.title('Income vs Expenses Over Time')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show() 