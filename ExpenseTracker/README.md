# 💰 DG Expense Tracker

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Handling-150458?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey?style=flat-square)

I have designed a command-line expense tracker built with **Python** and **Pandas**. Add, view, delete, and summarize expenses, set category-wise budget limits with automatic overspend warnings, and export summary reports — all with persistent CSV/JSON storage.

---

## ✨ Features

- ➕ **Add Expense** — log date, category, amount, and description
- 📋 **View Expenses** — view all expenses or filter by category
- 📊 **View Summary** — total spend and category-wise breakdown
- ❌ **Delete Expense** — remove an entry by index, with clean re-indexing
- 🎯 **Budget Limits** — set a spending limit per category, get warned when exceeded
- 📄 **Export Summary** — save total + category breakdown to a text report
- 💾 **Persistent Storage** — expenses saved to CSV, budgets saved to JSON, so data survives between runs

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — data storage, filtering, and aggregation (`groupby`, `concat`, boolean masking)
- **JSON** — budget persistence
- **OS module** — file existence checks

---

## 📂 Project Structure

```
expense_tracker/
├── main.py           # CLI menu loop — entry point
├── expense.py         # ExpenseTracker class — core logic
├── expenses.csv        # auto-generated expense data
├── budget.json          # auto-generated category budgets
└── summary_report.txt    # generated when exporting a summary
```

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas
```

### Run
```bash
python main.py
```

### Menu Options
```
1. Add Expense
2. View Expenses
3. View Summary
4. Delete Expense
5. Set Budget
6. Export Summary
7. Exit
```

---

## 🎯 What I Learned

This project was built as a hands-on way to strengthen Python fundamentals — OOP design, Pandas data manipulation, and file-based persistence :

- Structuring a stateful class around a Pandas DataFrame
- Correctly using `pd.concat()` with `ignore_index` vs `.drop().reset_index()`
- Reading/writing CSV and JSON for persistent storage
- Building a clean CLI menu loop with input validation in mind

---


## 👤 Author

**Dev Gothi**
B.Tech Electronics & VLSI Engineering, SVNIT Surat
[GitHub](https://github.com/dev-gothi)
