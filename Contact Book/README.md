# 📇 DG Contact Book

A simple command-line **Contact Book** application built in Python using Object-Oriented Programming (OOP). It lets you add, view, search, update, and delete contacts, with data persisted locally in a JSON file.

---

## 🏷️ Project Info

| Label | Detail |
|---|---|
| **Language** | Python 3.x |
| **Type** | Command-Line Interface (CLI) Application |
| **Paradigm** | Object-Oriented Programming |
| **Storage** | Local JSON file (`contacts.json`) |
| **Dependencies** | None (standard library only) |
| **Author** | Dev Gothi |

---

## 📁 Folder Structure

```
Contact Book/
├── contact_book.py   # ContactBook class — all logic in one file
├── README.md         # Project documentation
└── contacts.json     # Auto-generated on first save (stores all contacts)
```

---

## ✨ Features

- ➕ **Add Contact** — Save a new contact with name, phone, and email
- 📖 **View All Contacts** — List every saved contact
- 🔍 **Search Contact** — Find a contact by name
- ✏️ **Update Contact** — Edit an existing contact's phone/email
- 🗑️ **Delete Contact** — Remove a contact by name
- 💾 **Persistent Storage** — All changes are saved automatically to `contacts.json`

---

## 🧩 Class Overview

### `ContactBook`

| Attribute | Description |
|---|---|
| `contacts` | Dictionary storing all contacts, keyed by name |

| Method | Description |
|---|---|
| `main()` | Runs the menu-driven CLI loop |
| `load_contacts()` | Loads contacts from `contacts.json` if it exists |
| `save_contacts()` | Writes current contacts dictionary to `contacts.json` |
| `add_contact()` | Prompts for name, phone, email and adds a new contact |
| `view_contacts()` | Prints all saved contacts |
| `search_contact()` | Looks up and prints a contact by name |
| `update_contact()` | Updates phone/email for an existing contact |
| `delete_contact()` | Removes a contact by name |

Each contact is stored as:
```json
{
  "John Doe": {
    "Phone": "9876543210",
    "Email": "dev@example.com"
  }
}
```

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.x installed
- No external libraries required

### ▶️ Run the Program
```bash
python contact_book.py
```

### 📋 Menu Options
```
1. Add Contacts
2. View all Contacts
3. Search Contacts
4. Update Contacts
5. Delete Contacts
6. Exit
```

---

## ⚙️ How It Works

| Action | Behavior |
|---|---|
| **Add** | Checks the name isn't already used → adds `{Phone, Email}` under that name → saves to file |
| **View** | Loops through the dictionary and prints every contact's details |
| **Search** | Looks up the name directly in the dictionary and prints details if found |
| **Update** | Checks the contact exists → overwrites phone/email → saves to file |
| **Delete** | Checks the contact exists → removes the entry → saves to file |

---

## 🛠️ Possible Improvements

- [ ] Input validation (e.g. phone number format, empty fields)
- [ ] Case-insensitive name search/update/delete
- [ ] Allow duplicate names with unique contact IDs
- [ ] Split into multiple files (models + main) as the project grows
- [ ] Add a "list contacts sorted alphabetically" option
- [ ] Unit tests for `ContactBook` methods

---

## 👤 Author

**Dev Gothi**
B.Tech Electronics and VLSI Engineering, SVNIT Surat
