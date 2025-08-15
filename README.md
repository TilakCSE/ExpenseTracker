
# Expense Tracker CLI

A simple command-line application to **log daily expenses**, view summaries, and store them in a file or database.  
Built with **[Python]** or **[Java]**, this project is perfect for tracking your spending habits while practicing programming fundamentals.

---

## 📌 Features
- **Add Expense**: Record the date, category, amount, and description of your spending.
- **View All Expenses**: Display a list of all recorded transactions.
- **View Summary**:
  - Total spent today
  - Total spent this month
  - Spending breakdown by category
- **Data Persistence**:
  - Save expenses to a file (CSV/TXT) or database (SQLite/H2).
- **Export Data** (optional): Export all expenses as a CSV file.
- **Color-coded Output** *(optional)* for a better CLI experience.

---

## 🛠️ Tech Stack
- **Language**: Python or Java
- **Libraries**:
  - Python: `pandas`, `colorama`
  - Java: `java.time`, `H2 Database` (optional)
- **Database**: SQLite or file-based storage

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/expense-tracker-cli.git
cd expense-tracker-cli
````

### 2️⃣ Run the Program

#### Python

```bash
python expense_tracker.py
```

---

## 📂 Project Structure

```
expense-tracker-cli/
│
├── expense_tracker.py  # Main program
├── expenses.txt        # Data file
├── README.md           # Project documentation
```

---

## 📸 Screenshot


![CLI Screenshot](sample_screenshot.png)

---

## 📌 Example CLI Output

```text
===== Expense Tracker =====
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit

Enter choice: 1
Date (YYYY-MM-DD): 2025-08-15
Category: Food
Amount: 250
Description: Lunch with friends
Expense added successfully!
```

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements or new features.

---

## 📜 License

This project is licensed under the MIT License.

---

## 💬 Author

**Tilak Chauhan**
[LinkedIn](https://www.linkedin.com/in/tilak-chauhan-0817a3344/) | [GitHub](https://github.com/TilakCSE)

