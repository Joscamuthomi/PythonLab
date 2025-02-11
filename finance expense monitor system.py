import json
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

print("Welcome to our finance expense tracker and monitor \nWe value your pocket")


def get_transaction_data():
    date = input("Enter the date of the transaction (YYYY-MM-DD): ")

   
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please enter in YYYY-MM-DD format.")
        return get_transaction_data()  

    t_type = input("Enter transaction type (e.g., rent, shopping, food, etc.): ")

    while True:
        try:
            amount = float(input("Enter transaction amount (Ksh): "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric amount.")

    return {"date": date, "transaction_type": t_type, "amount": amount}

def load_transaction_data(filename="Transaction_data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_transaction_data(data, filename="Transaction_data.json"):
    existing_data = load_transaction_data()
    existing_data.append(data)
    
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=3)
    
    print("\nData saved to transactions file successfully!")

# Function to group transactions by type and sum amounts
def process_transaction_data(data):
    expense_summary = defaultdict(float)
    
    for transaction in data:
        expense_summary[transaction["transaction_type"]] += float(transaction["amount"])
    
    return expense_summary

# Function to group expenses by date
def process_transactions_by_date(data):
    daily_expenses = defaultdict(float)

    for transaction in data:
        daily_expenses[transaction["date"]] += float(transaction["amount"])

    return dict(sorted(daily_expenses.items()))  


def plot_expenses(expense_summary):
    if not expense_summary:
        print("No data available to plot.")
        return

    transaction_types = list(expense_summary.keys())
    amounts = list(expense_summary.values())

    plt.figure(figsize=(10, 5))
    plt.bar(transaction_types, amounts, color="skyblue")
    plt.xlabel("Transaction Type")
    plt.ylabel("Total Amount (Ksh)")
    plt.title("Expenses by Category")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    plt.show()

# Function to plot expenses as a line graph
def plot_expenses_line(daily_expenses):
    if not daily_expenses:
        print("No data available to plot.")
        return

    dates = list(daily_expenses.keys())
    amounts = list(daily_expenses.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker="o", linestyle="-", color="blue", markersize=6)
    
    plt.xlabel("Date")
    plt.ylabel("Total Expenses (Ksh)")
    plt.title("Daily Expenses Over Time")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    
    plt.show()

transaction_data = get_transaction_data()
save_transaction_data(transaction_data)

show_plot = input("Would you like to see insights? (yes/no): ").strip().lower()
if show_plot == "yes":
    expense_summary = process_transaction_data(load_transaction_data())
    plot_expenses(expense_summary)

show_trend = input("Would you like to see the expense trend over time? (yes/no): ").strip().lower()
if show_trend == "yes":
    daily_expenses = process_transactions_by_date(load_transaction_data())
    plot_expenses_line(daily_expenses)
