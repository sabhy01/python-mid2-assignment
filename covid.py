import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

FILENAME = "expenses.csv"
BUDGET_LIMIT = 10000  # Set monthly budget

# Load or initialize
if os.path.exists(FILENAME):
    df = pd.read_csv(FILENAME, parse_dates=['Date'])
else:
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])

def save_data():
    df.to_csv(FILENAME, index=False)
    print("Data saved.")

def log_expense():
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    date = datetime.today() if date_str == '' else datetime.strptime(date_str, "%Y-%m-%d")
    category = input("Category (e.g., Food, Travel): ")
    amount = float(input("Amount spent: "))
    note = input("Note (optional): ")
    global df
    df = pd.concat([df, pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Note": note
    }])], ignore_index=True)
    print("Expense added.")
    save_data()
    check_budget(date)

def check_budget(date):
    monthly_total = df[(df['Date'].dt.month == date.month) & (df['Date'].dt.year == date.year)]['Amount'].sum()
    if monthly_total > BUDGET_LIMIT:
        print("** ALERT: You’ve exceeded your monthly budget! **")
    else:
        print(f"Total spent this month: ₹{monthly_total} / ₹{BUDGET_LIMIT}")

def monthly_summary():
    df['Month'] = df['Date'].dt.to_period('M')
    summary = df.groupby('Month')['Amount'].sum()
    print("\n--- Monthly Summary ---")
    print(summary)
    summary.plot(kind='bar', title='Monthly Expenses', ylabel='Amount (₹)')
    plt.tight_layout()
    plt.show()

def weekly_summary():
    df['Week'] = df['Date'].dt.to_period('W')
    summary = df.groupby('Week')['Amount'].sum()
    print("\n--- Weekly Summary ---")
    print(summary)
    summary.plot(kind='line', marker='o', title='Weekly Expenses', ylabel='Amount (₹)')
    plt.tight_layout()
    plt.show()

def category_chart():
    summary = df.groupby('Category')['Amount'].sum()
    summary.plot(kind='pie', autopct='%1.1f%%', title='Spending by Category')
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def export_csv():
    filename = input("Enter filename to export as: ")
    df.to_csv(filename, index=False)
    print("Data exported to", filename)

def import_csv():
    global df
    filename = input("Enter CSV filename to import: ")
    if os.path.exists(filename):
        imported = pd.read_csv(filename, parse_dates=['Date'])
        df = pd.concat([df, imported], ignore_index=True)
        save_data()
        print("Imported successfully.")
    else:
        print("File not found.")

def menu():
    while True:
        print("\n---- Expense Tracker ----")
        print("1. Log Expense")
        print("2. Monthly Summary")
        print("3. Weekly Summary")
        print("4. Category Chart")
        print("5. Import CSV")
        print("6. Export CSV")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1': log_expense()
        elif choice == '2': monthly_summary()
        elif choice == '3': weekly_summary()
        elif choice == '4': category_chart()
        elif choice == '5': import_csv()
        elif choice == '6': export_csv()
        elif choice == '0': break
        else: print("Invalid option.")

menu()