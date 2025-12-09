<h1 align="center">💸 Expense Tracker CLI</h1>

<p align="center">
  Keep your money in check... or at least pretend to.  
  A simple, fast, no-nonsense CLI to track your daily expenses.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/CLI-Tool-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/JSON-Storage-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Polars-CSV_Export-red?style=for-the-badge">
</p>

---

## 🎬 Demo

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDJqa2FzZ2h0bjB2djZodTlrc3U1aHhkYzBjbnkzMW53cHcwZGt6YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/U7Mqz6lKPjlQZEAWJE/giphy.gif" width="600">
</p>

> *Actual footage of you deleting your expenses before your mom sees them.*

---

## 🚀 Features

- ➕ Add expenses  
- 🗑️ Delete expenses  
- 📋 List all expenses  
- 📊 Total summary  
- 📅 Monthly summary  
- 💾 JSON storage  
- 📤 Export expenses to CSV using Polars  

---

## 🏗️ Installation

Clone this masterpiece:

```bash
git clone https://github.com/Average-Chief/Expense_Tracker_CLI.git
cd expense-tracker-cli
```
## 💻 Usage

```bash
python main.py -h #Shows the help section.
python main.py add -d "Description" -a (amount) #Adds an expense.
python main.py add -d "Description" -a (amount) #Adds another expense with ID 2.
python main.py list #Lists all the expenses.
python main.py total #Total sum of the expenses.
python main.py delete --id 1 #Deletes the expense where ID is 1.
python main.py summary -m 12 #Total expenses in the month 12th month.
python main.py export -f (filename.csv) #Allows the users to export expenses to a CSV file.
```

Project Link: https://roadmap.sh/projects/expense-tracker