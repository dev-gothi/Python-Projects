# DG Library Management System

It is a simple command-line Library Management System built in Python using Object-Oriented Programming. It allows you to manage books, members, and borrowing transactions, with data persisted locally in a JSON file.

## Features

- **Book Management** — Add books and view the full catalog
- **Member Management** — Register members and view all members
- **Search** — Search for a book by title
- **Issue / Return** — Issue books to members and process returns with automatic fine calculation
- **Transaction History** — View all issue/return transactions
- **Persistent Storage** — All data is saved to and loaded from `data.json`

## Project Structure

```
.
├── semi.py       # Core models: Book, Member, Transaction
├── Library.py    # Library class — business logic & data persistence
├── main.py       # CLI entry point
└── data.json     # Auto-generated data store (created on first save)
```

## Classes

### `Book`
Represents a book with `bookid`, `title`, `author`, `genre`, and availability status.

### `Member`
Represents a library member with `memberid`, `name`, `email`, and a list of currently borrowed book IDs.

### `Transaction`
Represents a borrow/return record with issue date, due date (14 days from issue), return date, and calculated fine (₹1/day for late returns).

### `Library`
The system — manages collections of books, members, and transactions, and handles all operations (add, search, issue, return, save/load).

## Getting Started

### Prerequisites
- Python 3.x (no external dependencies required)

### Running the Program

```bash
python main.py
```

You'll be presented with a menu:

```
1. Add Book
2. Add Member
3. Search Books
4. View All Books
5. View All Members
6. Issue Book
7. Return Book
8. View All Transactions
9. Exit
```
Select any option to interact with the system. Data is automatically saved to `data.json` after every change.

## How It Works

- **Issuing a book**: Checks that the member and book exist and that the book is available, then marks it as unavailable, adds it to the member's borrowed list, and creates a new transaction.
- **Returning a book**: Verifies the member has the book borrowed, finds the matching open transaction, marks the book available again, sets the return date, and calculates any late fine.
- **Fines**: ₹1 per day late, calculated automatically on return.

## Author

Dev Gothi
