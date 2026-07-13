# 🐍 Python-Projects

A collection of beginner-to-intermediate Python projects built using Object-Oriented Programming (OOP) concepts. Each project is a standalone command-line application with its own folder, code, and documentation.

---

## 🏷️ Repository Info

| Label | Detail |
|---|---|
| **Language** | Python 3.x |
| **Type** | CLI Application Collection |
| **Paradigm** | Object-Oriented Programming |
| **Dependencies** | None (standard library only) |
| **Author** | Dev Gothi |

---

## 📁 Repository Structure

```
Python-Projects/
├── Library Management System/
│   ├── semi.py
│   ├── Library.py
│   ├── main.py
│   └── README.md
├── Contact Book/
│   ├── contact_book.py
│   └── README.md
├── ATM System/
│   ├── atm.py
│   └── README.md
├── LICENSE
└── README.md          # (this file)
```

---

## 📚 Projects

### 1️⃣ [Library Management System](./Library%20Management%20System)
A CLI-based library management system to manage books, members, and borrowing transactions.

| | |
|---|---|
| **Features** | Add/view books & members, search books, issue/return books, track transactions, auto-calculate late fines |
| **Classes** | `Book`, `Member`, `Transaction`, `Library` |
| **Storage** | `data.json` |

---

### 2️⃣ [Contact Book](./Contact%20Book)
A CLI-based contact manager to save and organize personal/professional contacts.

| | |
|---|---|
| **Features** | Add/view/search/update/delete contacts, case-insensitive search, alphabetically sorted view |
| **Classes** | `ContactBook` |
| **Storage** | `contacts.json` |

---

### 3️⃣ [ATM System](./ATM%20System)
A CLI-based ATM simulator supporting PIN-protected banking operations.

| | |
|---|---|
| **Features** | Set PIN, check balance, deposit, withdraw (with insufficient-balance check), supports multiple independent accounts |
| **Classes** | `Atm` |
| **Storage** | In-memory only |

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.x installed
- No external libraries required for any project

### ▶️ Running a Project
Navigate into the desired project folder and run its main file:

```bash
cd "Library Management System"
python main.py
```

```bash
cd "Contact Book"
python contact_book.py
```

```bash
cd "ATM System"
python atm.py
```

---

## 🛠️ General Roadmap

- [ ] Add unit tests across all projects
- [ ] Add input validation consistently across all projects
- [ ] Add `.gitignore` for generated data files (`data.json`, `contacts.json`)
- [ ] Add more projects as learning progresses

---

## 👤 Author

**Dev Gothi**
B.Tech Electronics and VLSI Engineering, SVNIT Surat
