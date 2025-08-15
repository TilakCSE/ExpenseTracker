import csv
import os
from datetime import datetime

# Define the name of the CSV file to store expenses
CSV_FILE = 'expenses.csv'
# Define the headers for the CSV file
CSV_HEADER = ['date', 'amount', 'category']

def initialize_csv():
    """
    Creates the CSV file with a header row if it doesn't already exist.
    """
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(CSV_HEADER)
        print(f"'{CSV_FILE}' created successfully.")

def add_expense():
    """
    Prompts the user for expense details, validates them, and adds the expense to the CSV file.
    """
    print("\n--- Add a New Expense ---")
    
    # --- Input and Validate Date ---
    while True:
        date_str_input = input("Enter the date (YYYY-MM-DD), or leave blank for today: ")
        
        # Default to today's date if input is blank
        if not date_str_input:
            date_obj = datetime.now()
            break
            
        try:
            # Convert user's string input into a datetime object
            date_obj = datetime.strptime(date_str_input, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            
    # --- Format the datetime object into the required YYYY-MM-DD string ---
    date_str = date_obj.strftime('%Y-%m-%d')
            
    # --- Input and Validate Amount ---
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # --- Input Category ---
    category = input("Enter the category (e.g., Food, Transport, Rent): ")

    # --- Write to CSV ---
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, amount, category])
    
    print("✅ Expense added successfully!")

def view_expenses():
    """
    Reads all expenses from the CSV file and displays them in a formatted table.
    """
    print("\n--- All Expenses ---")
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader) # Skip header row
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            # Print table header
            print(f"{header[0]:<12} | {header[1]:<10} | {header[2]:<20}")
            print("-" * 45)
            
            # Print each expense row
            for row in expenses:
                print(f"{row[0]:<12} | {row[1]:<10} | {row[2]:<20}")

    except FileNotFoundError:
        print(f"'{CSV_FILE}' not found. Please add an expense first.")
    except StopIteration:
        print("No expenses recorded yet.")


def search_expenses():
    """
    Allows the user to search for expenses by date or category and displays the results.
    """
    print("\n--- Search Expenses ---")
    search_by = input("Search by (date/category): ").lower()
    
    if search_by not in ['date', 'category']:
        print("Invalid search option. Please choose 'date' or 'category'.")
        return

    search_term = input(f"Enter the {search_by} to search for: ")
    results = []
    
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            # Determine the column index based on search criteria
            col_index = CSV_HEADER.index(search_by)

            for row in reader:
                if row[col_index].strip().lower() == search_term.strip().lower():
                    results.append(row)
        
        if not results:
            print(f"No expenses found for '{search_term}'.")
            return
            
        # Display results
        print("\n--- Search Results ---")
        print(f"{header[0]:<12} | {header[1]:<10} | {header[2]:<20}")
        print("-" * 45)
        for row in results:
            print(f"{row[0]:<12} | {row[1]:<10} | {row[2]:<20}")

    except FileNotFoundError:
        print(f"'{CSV_FILE}' not found. No expenses to search.")
    except StopIteration:
        print("No expenses recorded to search.")

def calculate_monthly_total():
    """
    Calculates and displays the total expenses for a user-specified month and year.
    """
    print("\n--- Calculate Monthly Total ---")

    # --- Input and Validate Month/Year ---
    while True:
        month_str = input("Enter the month and year (YYYY-MM): ")
        try:
            # Validate format
            month_obj = datetime.strptime(month_str, '%Y-%m')
            break
        except ValueError:
            print("Invalid format. Please use YYYY-MM.")

    total = 0.0
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            
            for row in reader:
                try:
                    expense_date = datetime.strptime(row[0], '%Y-%m-%d')
                    # Check if the expense is in the specified month and year
                    if expense_date.year == month_obj.year and expense_date.month == month_obj.month:
                        total += float(row[1])
                except (ValueError, IndexError):
                    # Skip rows with malformed data
                    continue
        
        print(f"\nTotal expenses for {month_obj.strftime('%B %Y')}: ₹{total:.2f}")

    except FileNotFoundError:
        print(f"'{CSV_FILE}' not found. Cannot calculate total.")
    except StopIteration:
        print("No expenses recorded for this period.")

def main():
    """
    Main function to run the expense tracker CLI. Displays the menu and handles user input.
    """
    initialize_csv() # Ensure the CSV file exists
    
    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add a new expense 📝")
        print("2. View all expenses 📋")
        print("3. Search for expenses 🔍")
        print("4. Calculate monthly total 💰")
        print("5. Exit 👋")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_expenses()
        elif choice == '4':
            calculate_monthly_total()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the script
if __name__ == "__main__":
    main()